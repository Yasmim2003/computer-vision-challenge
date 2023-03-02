import cv2 
import matplotlib
from matplotlib import pyplot as plt

dado = cv2.imread('dado.jpeg')
blur_img = cv2.blur(dado,(5,5))

status = cv2.imwrite("blurimage.jpg", blur_img)