# 高斯噪声
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# img = cv.imread('die.png')
# dst=cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()


"""第一个参数是嘈杂帧的列表。第二个参数 imgToDenoiseIndex 指定我们需要去噪的帧，因为我们在输入列表中传递了 frame 的索引。第三个是 temporalWindowSize，它指定了用于去噪的附近帧的数量。应该很奇怪。在这种情况下，使用总共 temporalWindowSize 帧，其中中心帧是要去噪的帧。例如，您传递了 5 个帧的列表作为输入。设 imgToDenoiseIndex = 2 和 temporalWindowSize = 3.然后使用 frame-1，frame-2 和 frame-3 对帧-2 进行去噪"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
cap = cv.VideoCapture('output.avi')
# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]
# convert all to grayscale
gray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in img]
# convert all to float64
gray = [np.float64(i) for i in gray]
# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10
# Add this noise to images
noisy = [i+noise for i in gray]
# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]
# Denoise 3rd frame considering all the 5 frames
dst = cv.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7,35)
plt.subplot(131),plt.imshow(gray[2],'gray')
plt.subplot(132),plt.imshow(noisy[2],'gray')
plt.subplot(133),plt.imshow(dst,'gray')
plt.show()