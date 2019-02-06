import os
from shutil import copyfile

ref_path = '../../datasets/COCO-Text/gt/gt_COCO_format_legible/'
img_path = '../../datasets/COCO-Text/img/train/'
out_path = '../../datasets/COCO-Text/img/train_legible/'

for file in os.listdir(ref_path):
    img_name = file.replace('.json','.jpg')
    try:
        copyfile(img_path + img_name, out_path + img_name)
    except: # Because in gt we have images from all splits!
        continue