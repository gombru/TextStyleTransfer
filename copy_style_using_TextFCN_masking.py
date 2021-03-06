# Copies the style of an image generated with StyleTransfer to the original image guided by a mask given by TextFCN

import os
from PIL import Image
import numpy as np
import cv2

images_path = '/home/raulgomez/datasets/COCO-Text/img/train_legible/'
masks_path = '/home/raulgomez/datasets/StyleTransfer/TextFCN_masks/train_legible/'
styled_images_path = '../../other_datasets/COCO-Text/train_legible_words/'
out_path = '../../other_datasets/COCO-Text/train_styled_masked/'
max_num_styles = 34

if not os.path.isdir(out_path):
    os.mkdir(out_path)

for file in os.listdir(images_path):

    src_img = np.array(Image.open(images_path + file))
    mask = np.array(Image.open(masks_path + file.split('/')[-1].replace('jpg','png')))
    # mask[mask < 200] = 0
    mask = mask/255.0
    inv_mask = 1.0 - mask
    for s in range(max_num_styles):
        try:
            style_img = np.array(Image.open(styled_images_path + file.split('/')[-1].split('.')[0] + '_' + str(s) + '.png'))
            h,w,c = src_img.shape
            style_img = cv2.resize(style_img, (w, h))
        except:
            print("Error")
            break

        src_img_edited = src_img.copy()
        for c in range(3):
            src_img_edited[:,:,c] = src_img_edited[:,:,c] * inv_mask
            style_img[:,:,c] = style_img[:,:,c] * mask

        out_img = Image.fromarray(style_img + src_img_edited)

        out_img.save(out_path + file.split('/')[-1].split('.')[0] + '_' + str(s) + '.jpg')

print("DONE")

