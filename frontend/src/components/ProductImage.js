import React, { useEffect, useRef, useState } from 'react';
import { Image, Transformer } from 'react-konva';
import useImage from 'use-image';

const ProductImage = ({ image, isSelected, onSelect, onDragEnd, onTransformEnd }) => {
  const [img] = useImage(image.src);
  const imageRef = useRef(null);
  const trRef = useRef(null);

  useEffect(() => {
    if (isSelected) {
      trRef.current.nodes([imageRef.current]);
      trRef.current.getLayer().batchDraw();
    }
  }, [isSelected]);

  return (
    <>
      <Image
        image={img}
        x={image.x}
        y={image.y}
        width={image.width}
        height={image.height}
        draggable
        onClick={(e) => {
          onSelect(image.id);
          e.cancelBubble = true;
        }}
        onTap={(e) => {
          onSelect(image.id);
          e.cancelBubble = true;
        }}
        onDragEnd={(e) => onDragEnd(e, image.id)}
        onTransformEnd={(e) => {
          const node = imageRef.current;
          const scaleX = node.scaleX();
          const scaleY = node.scaleY();
          node.scaleX(1);
          node.scaleY(1);
          onTransformEnd(image.id, {
            x: node.x(),
            y: node.y(),
            width: Math.max(5, node.width() * scaleX),
            height: Math.max(5, node.height() * scaleY),
          });
        }}
        ref={imageRef}
        shadowBlur={50}
        shadowColor="black"
        shadowOpacity={0.2}
      />
      {isSelected && (
        <Transformer
          ref={trRef}
          boundBoxFunc={(oldBox, newBox) => {
            if (newBox.width < 5 || newBox.height < 5) {
              return oldBox;
            }
            return newBox;
          }}
        />
      )}
    </>
  );
};

export default ProductImage;
