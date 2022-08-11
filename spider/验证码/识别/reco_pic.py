"""import cv2 as cv
import pytesseract
from PIL import Image

def recognize_text(image):
    # 边缘保留滤波  去噪
    dst = cv.pyrMeanShiftFiltering(image, sp=10, sr=60)
    #cv.imshow('dst',dst)
    # 灰度图像
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 形态学操作   腐蚀  膨胀
    erode = cv.erode(binary, None, iterations=2)
    dilate = cv.dilate(erode, None, iterations=1)
    cv.imshow('dilate', dilate)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(dilate, dilate)
    cv.imshow('binary-image', dilate)
    # 识别
    test_message = Image.fromarray(dilate)
    print(test_message,type(test_message))
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


if __name__ == "__main__":
    #img = open('a.jpg', 'rb').read()
    src = cv.imread(r'./a.jpg')
    cv.imshow('input image', src)
    recognize_text(src)
    cv.waitKey(0)
    cv.destroyAllWindows()"""


"""import cv2 as cv
import pytesseract
from PIL import Image
def recognize_text(image):
    # 边缘保留滤波  去噪
    blur =cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv.imshow('binary', binary)
    # 形态学操作  获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow('bin1', bin1)
    kernel = cv.getStructuringElement(cv.MORPH_OPEN, (2, 3))
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow('bin2', bin2)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(bin2, bin2)
    cv.imshow('binary-image', bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')

if __name__ == "__main__":
    src = cv.imread(r'./a.jpg')
    cv.imshow('input image', src)
    recognize_text(src)
    cv.waitKey(0)
    cv.destroyAllWindows()"""

#/////////////////////////////////////////////////////////////////////////

import cv2 as cv
import pytesseract
from PIL import Image

def recognize_text(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=10, sr=60)
    cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化  设置阈值  自适应阈值的话 黄色的4会提取不出来
    ret, binary = cv.threshold(gray, 160, 255, cv.THRESH_BINARY_INV)    #THRESH_BINARY THRESH_BINARY_INV THRESH_TRUNC  THRESH_TOZERO THRESH_TOZERO_INV
    print(f'二值化设置的阈值：{ret}')
    cv.imshow('binary', binary)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(binary, binary)
    cv.imshow('bg_image', binary)
    # 识别
    test_message = Image.fromarray(binary)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')
if __name__ == "__main__":
    src = cv.imread(r'a.jpg')
    cv.imshow('input image', src)
    recognize_text(src)
    cv.waitKey(1)
    cv.destroyAllWindows()
#///////////////////////////////////////////////////////////////////////////////////////////////////
"""import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('E://figures/other/poems.jpg'))"""








