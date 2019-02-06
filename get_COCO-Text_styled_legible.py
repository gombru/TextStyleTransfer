import os
from shutil import copyfile

ref_path = '/home/raulgomez/datasets/COCO-Text/gt/gt_COCO_format_legible/'
img_path = '/home/raulgomez/other_datasets/COCO-Text/all_legible_words/'
out_path = '/home/raulgomez/other_datasets/COCO-Text/train_legible_words/'

train_legible_ids = []
for file in os.listdir(ref_path):
    img_id= file.strip('.json')
    train_legible_ids.append(img_id)

print(len(train_legible_ids))

for file in os.listdir(img_path):
    img_id = file.strip('.png')
    rem = '_' + img_id.split('_')[-1]
    img_id = img_id.replace(rem,'')
    if img_id in train_legible_ids:
        copyfile(img_path + file, out_path + file)
