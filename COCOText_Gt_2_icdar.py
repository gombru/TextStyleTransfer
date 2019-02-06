import os
import json

in_path = '../../datasets/COCO-Text/gt/gt_COCO_format_legible/'
out_path = '../../datasets/COCO-Text/gt/gt_ICDAR_format_legible/'

for file in os.listdir(in_path):
    lines_2_write = []
    data = json.load(open(in_path + file))
    for el in data:
        bbox = el['bbox']

        x = int(bbox[0])
        y = int(bbox[1])
        w = int(bbox[2])
        h = int(bbox[3])

        x1 = x
        y1 = y
        x2 = x + w
        y2 = y
        x3 = x + w
        y3 = y + h
        x4 = x
        y4 = y + h

        lines_2_write.append(
            str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + str(x3) + ',' + str(y3) + ',' + str(
                x4) + ',' + str(y4) + ',' + '###' + '\n')

    if len(lines_2_write) > 0:
        with open(out_path + file.strip('.json') + '.txt', 'w') as outfile:
            for l in lines_2_write:
                outfile.write(l)