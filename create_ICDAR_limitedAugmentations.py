import os
import random
from shutil import copyfile

img_list = '/home/Imatge/ssd2/ICDAR_2015_IndicentalSceneText/train/img/'
origin_dir = '/home/Imatge/ssd2/ICDAR_2015_IndicentalSceneText/train/img_styled_masked/'
out_dir = '/home/Imatge/ssd2/ICDAR_2015_IndicentalSceneText/train/img_4styles_masked/'


for file in os.listdir(img_list):
    wanted_styles = random.sample(range(34), 4)
    wanted_styles.remove(0)
    wanted_styles.remove(6)
    wanted_styles.remove(25)
    for s in wanted_styles:
        copyfile(origin_dir + file.strip('.jpg') + '_' + str(s) + '.jpg', out_dir + file.strip('.jpg') + '_' + str(s) + '.jpg')
