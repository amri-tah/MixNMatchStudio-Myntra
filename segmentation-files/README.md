# Cloth Segmentation Project 👕

## Overview 🌟

This project focuses on cloth segmentation using the U2NET model. The aim is to accurately segment clothing items from images, making it possible to extract and manipulate individual garments for MixNMatchStudio. This technology is particularly useful for fashion design, e-commerce, and augmented reality applications.

## Key Features 🚀

- **Accurate Cloth Segmentation**: Utilizes the U2NET model to segment clothes with high precision. 🎯
- **Transparency Handling**: Generates segmented images with transparent backgrounds. ✨
- **Scalable and Efficient**: Designed to handle large datasets and produce results efficiently. ⚡

## Requirements 📦

To run this project, ensure you have the following libraries installed:

- `os`
- `requests`
- `PIL`
- `cv2`
- `argparse`
- `numpy`
- `torch`
- `torchvision`
- `matplotlib`

You can download the pretrained model from the following link: https://huggingface.co/oyelmali/Clothes-Semantic-Segmentation/blob/main/cloth_segm.pth

## Project Structure 📁

- **network.py**: Contains the U2NET model architecture.
- **top_process.py**: Main script for downloading tops images, generating segmentation masks, and saving results.
- **bottom_process.py**: Main script for downloading bottoms images, generating segmentation masks, and saving results.
- **coord_process.py**: Main script for downloading coords images, generating segmentation masks, and saving results.
- **skirt_process.py**: Main script for downloading skirts images, generating segmentation masks, and saving results.

## Output 📤

The script produces the following outputs:

- **Alpha Masks**: Saved in the `output/alpha` directory.
- **Final Cloth Segmentation**: Saved in the `output/cloth_seg` directory.
- **Transparent Segmented Cloth Image**: Saved in the `output` directory.

## Screenshots 📸

The script displays a figure with three subplots:

- **Original Image**
- **Alpha Mask**
- **Cropped Cloth Image**

![image](https://github.com/user-attachments/assets/cc177652-cbb9-4467-a14e-e906ff94d819)
![image](https://github.com/user-attachments/assets/17ee91f9-bf7a-4afb-ac6c-fa2a15f7ecb2)

## Conclusion 🏁

This project demonstrates an advanced application of deep learning for cloth segmentation, showcasing its potential in various industries. The results highlight the accuracy and efficiency of the U2NET model in handling complex segmentation tasks.


