from network import U2NET

import os
import requests
from PIL import Image
import cv2
import argparse
import numpy as np
from io import BytesIO

import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

from collections import OrderedDict

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def load_checkpoint(model, checkpoint_path):
    if not os.path.exists(checkpoint_path):
        print("----No checkpoints at given path----")
        return
    model_state_dict = torch.load(checkpoint_path, map_location=torch.device("cpu"))
    new_state_dict = OrderedDict()
    for k, v in model_state_dict.items():
        name = k[7:]  # remove `module.`
        new_state_dict[name] = v

    model.load_state_dict(new_state_dict)
    print("----checkpoints loaded from path: {}----".format(checkpoint_path))
    return model

def get_palette(num_cls):
    """ Returns the color map for visualizing the segmentation mask.
    Args:
        num_cls: Number of classes
    Returns:
        The color map
    """
    n = num_cls
    palette = [0] * (n * 3)
    for j in range(0, n):
        lab = j
        palette[j * 3 + 0] = 0
        palette[j * 3 + 1] = 0
        palette[j * 3 + 2] = 0
        i = 0
        while lab:
            palette[j * 3 + 0] |= (((lab >> 0) & 1) << (7 - i))
            palette[j * 3 + 1] |= (((lab >> 1) & 1) << (7 - i))
            palette[j * 3 + 2] |= (((lab >> 2) & 1) << (7 - i))
            i += 1
            lab >>= 3
    return palette

class Normalize_image(object):
    """Normalize given tensor into given mean and standard dev

    Args:
        mean (float): Desired mean to substract from tensors
        std (float): Desired std to divide from tensors
    """

    def __init__(self, mean, std):
        assert isinstance(mean, (float))
        if isinstance(mean, float):
            self.mean = mean

        if isinstance(std, float):
            self.std = std

        self.normalize_1 = transforms.Normalize(self.mean, self.std)
        self.normalize_3 = transforms.Normalize([self.mean] * 3, [self.std] * 3)
        self.normalize_18 = transforms.Normalize([self.mean] * 18, [self.std] * 18)

    def __call__(self, image_tensor):
        if image_tensor.shape[0] == 1:
            return self.normalize_1(image_tensor)

        elif image_tensor.shape[0] == 3:
            return self.normalize_3(image_tensor)

        elif image_tensor.shape[0] == 18:
            return self.normalize_18(image_tensor)

        else:
            assert "Please set proper channels! Normlization implemented only for 1, 3 and 18"

def apply_transform(img):
    transforms_list = []
    transforms_list += [transforms.ToTensor()]
    transforms_list += [Normalize_image(0.5, 0.5)]
    transform_rgb = transforms.Compose(transforms_list)
    return transform_rgb(img)

def generate_mask(input_image, net, palette, device = 'cpu'):

    img = input_image
    img_size = img.size
    img = img.resize((768, 768), Image.BICUBIC)
    image_tensor = apply_transform(img)
    image_tensor = torch.unsqueeze(image_tensor, 0)

    alpha_out_dir = os.path.join('./output/alpha')
    cloth_seg_out_dir = os.path.join('./output/cloth_seg')

    os.makedirs(alpha_out_dir, exist_ok=True)
    os.makedirs(cloth_seg_out_dir, exist_ok=True)

    with torch.no_grad():
        output_tensor = net(image_tensor.to(device))
        output_tensor = F.log_softmax(output_tensor[0], dim=1)
        output_tensor = torch.max(output_tensor, dim=1, keepdim=True)[1]
        output_tensor = torch.squeeze(output_tensor, dim=0)
        output_arr = output_tensor.cpu().numpy()

    classes_to_save = []

    # Check which classes are present in the image
    for cls in range(1, 4):  
        if np.any(output_arr == cls):
            classes_to_save.append(cls)

    # Save alpha masks
    for cls in classes_to_save:
        alpha_mask = (output_arr == cls).astype(np.uint8) * 255
        alpha_mask = alpha_mask[0]  
        alpha_mask_img = Image.fromarray(alpha_mask, mode='L')
        alpha_mask_img = alpha_mask_img.resize(img_size, Image.BICUBIC)
        alpha_mask_img.save(os.path.join(alpha_out_dir, f'{cls}.png'))

    # Save final cloth segmentations
    cloth_seg = Image.fromarray(output_arr[0].astype(np.uint8), mode='P')
    cloth_seg.putpalette(palette)
    cloth_seg = cloth_seg.resize(img_size, Image.BICUBIC)
    cloth_seg.save(os.path.join(cloth_seg_out_dir, 'final_seg.png'))
    return cloth_seg

def load_seg_model(checkpoint_path, device='cpu'):
    net = U2NET(in_ch=3, out_ch=4)
    net = load_checkpoint(net, checkpoint_path)
    net = net.to(device)
    net = net.eval()

    return net

def save_transparent_image(image_path, alpha_path, output_path):
    original_image = cv2.imread(image_path)
    alpha_masks = []

    alpha_mask_path = os.path.join(alpha_path)
    alpha_mask = cv2.imread(alpha_mask_path, cv2.IMREAD_GRAYSCALE)
    alpha_mask = cv2.resize(alpha_mask, (original_image.shape[1], original_image.shape[0]))
    alpha_masks.append(alpha_mask)

    combined_alpha_mask = np.max(alpha_masks, axis=0)    # Combine alpha mask
    
    transparent_image = cv2.merge([original_image, combined_alpha_mask])   # Apply alpha mask to the original image

    cv2.imwrite(output_path, transparent_image)   # Save the transparent image

def image_view(image, mask, result):
    
    img = mpimg.imread(image)
    masked = mpimg.imread(mask)
    transparent = mpimg.imread(result)
    
    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(1,3,1)
    ax.imshow(img)
    ax.set_title('Original Image')
    ax1 = fig.add_subplot(1,3,2)
    ax1.imshow(masked)
    ax1.set_title('Alpha Mask')
    ax2 = fig.add_subplot(1,3,3)
    ax2.imshow(transparent)
    ax2.set_title('Cropped Cloth Image')
    plt.show()

def download_image(url, save_path):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(save_path)
    return save_path

def main(args):

    alpha_out = './output/alpha/1.png'
    downloaded_image_path = './input_image.png'

    device = 'cuda:0' if args.cuda else 'cpu'

    # Download the image
    image_name = download_image(args.image_url, downloaded_image_path).split('/')[-1]
    output_path = f'./output/{image_name}'

    # Create an instance of your model
    model = load_seg_model(args.checkpoint_path, device=device)

    palette = get_palette(4)

    img = Image.open(downloaded_image_path).convert('RGB')
    generate_mask(img, model, palette)
    
    save_transparent_image(downloaded_image_path, alpha_out, output_path)

    image_view(downloaded_image_path, alpha_out, output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Help to set arguments for Cloth Segmentation.')
    parser.add_argument('--image_url', type=str, required=False, help='URL of the input image')
    parser.add_argument('--cuda', action='store_true', help='Enable CUDA (default: False)')
    parser.add_argument('--checkpoint_path', type=str, default='C:\\Users\\dhars\\Cloth-Semantic-Segmentation\\cloth_segm.pth', help='Path to the checkpoint file')
    args = parser.parse_args()

    # Set the URL directly here
    if not args.image_url:
        args.image_url = "https://myntra-products.s3.amazonaws.com/original/coll6_1.png"

    main(args)
