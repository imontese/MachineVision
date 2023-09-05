import cv2
import pandas as pd
import numpy as np

scr_color = cv2.imread('img\\bottle.jpg')
scr = cv2.imread('img\\bottle.jpg', cv2.IMREAD_GRAYSCALE)

image = cv2.adaptiveThreshold(scr, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
contours, hier = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


cnt_mean = np.mean(list(map(lambda x : cv2.contourArea(x), contours)))

cnt_list = []
for cnt in contours:
    area = cv2.contourArea(cnt)

    if area > cnt_mean: 
        cv2.drawContours(scr_color, cnt, -1, color=(0,255,0), thickness=2)

cv2.imwrite('img//bottle-contours.jpg', scr_color)

