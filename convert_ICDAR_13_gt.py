import os

gt_folder = '/home/raulgomez/other_datasets/ICDAR_2013_FocusedSceneText/test/gt_original/'

for file in os.listdir(gt_folder):
    lines_2_write = []

    for line in open(gt_folder + file):
        data = line.split(',')
        left = int(data[0])
        top = int(data[1])
        right = int(data[2])
        bot = int(data[3])
        word = data[4]

        x1 = int(left)
        y1 = int(top)
        x2 = int(right)
        y2 = int(top)
        x3 = int(right)
        y3 = int(bot)
        x4 = int(left)
        y4 = int(bot)

        lines_2_write.append(str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(x3)+','+str(y3)+','+str(x4)+','+str(y4)+','+word)

    with open(gt_folder.replace('_original','') + file,'w') as outfile:
        for l in lines_2_write:
            outfile.write(l)

print("DONE")



