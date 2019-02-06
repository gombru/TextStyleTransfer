import cv2

im_gray = cv2.imread("COCO_train2014_000000244074.png", cv2.IMREAD_GRAYSCALE)

print(im_gray.max())
print(im_gray.min())

# im_gray = im_gray - 20
im_gray[im_gray<230] = 0
# im_gray[im_gray>254] = 254


print(im_gray.max())
print(im_gray.min())

im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)

print(im_gray.max())
print(im_gray.min())

cv2.imwrite('result.png',im_color)