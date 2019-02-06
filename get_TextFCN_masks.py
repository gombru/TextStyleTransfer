import numpy as np
from PIL import Image
import caffe
import time
import os

images_path = '../../datasets/COCO-Text/img/train_legible/'
masks_path = '/home/raulgomez/datasets/StyleTransfer/TextFCN_masks/train_legible/'

# Run in GPU
caffe.set_device(0)
caffe.set_mode_gpu()

# load net
net = caffe.Net('../../projects/TextFCN/voc-fcn8s-atonce/deploy.prototxt', '../../datasets/COCO-Text/fcn8s-atonce.caffemodel', caffe.TEST)

print 'Computing heatmaps ...'

count = 0
start = time.time()

resize = False

for file in os.listdir(images_path):

    # try:
    count = count + 1
    if count % 100 == 0:
        print count

    # load image
    im = Image.open(images_path + file)
    if resize:
        im = im.resize((512,512), Image.ANTIALIAS)

    # Turn grayscale images to 3 channels
    if (im.size.__len__() == 2):
        im_gray = im
        im = Image.new("RGB", im_gray.size)
        im.paste(im_gray)

    #switch to BGR and substract mean
    in_ = np.array(im, dtype=np.float32)
    in_ = in_[:,:,::-1]
    in_ -= np.array((104.00698793,116.66876762,122.67891434))
    in_ = in_.transpose((2,0,1))

    # shape for input (data blob is N x C x H x W)
    net.blobs['data'].reshape(1, *in_.shape)
    net.blobs['data'].data[...] = in_

    # run net and take scores
    net.forward()

    # Compute SoftMax HeatMap
    hmap_0 = net.blobs['score_conv'].data[0][0, :, :]   #Text score
    hmap_1 = net.blobs['score_conv'].data[0][1, :, :]   #Backgroung score
    hmap_0 = np.exp(hmap_0)
    hmap_1 = np.exp(hmap_1)
    hmap_softmax = hmap_1 / (hmap_0 + hmap_1)

    #Save PNG softmax heatmap
    hmap_softmax_2save = (255.0 * hmap_softmax).astype(np.uint8)
    hmap_softmax_2save = Image.fromarray(hmap_softmax_2save)
    hmap_softmax_2save.save(masks_path + file.split('/')[-1].replace('jpg','png'))

    # except:
    #     print("Error with image")
    #     continue

    print 'Heatmap saved for image: ' + file.split('/')[-1]

end = time.time()
print 'Total time elapsed in heatmap computations'
print(end - start)
