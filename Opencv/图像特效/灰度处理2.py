import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros(img.shape, np.uint8)
# #Gray = r*0.299 + g*0.587 + b*0.114 = (r+b+g)/3
# for i in range(0, height):
#     for j in range(0, width):
#         (b, g, r) = img[i, j]
#         gray = (int(b) + int(g) + int(r))/3
#         dst[i, j] = np.uint8(gray)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b, g, r = int(b), int(g), int(r)
        Gray = r*0.299 + g*0.587 + b*0.114
        dst[i, j] = np.uint8(Gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)

