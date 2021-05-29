import cv2 as cv

import numpy as np
img = cv.imread(r'C:\Users\mohan\Desktop\Final_Project\character_segmentation/hw1.jpg',0)
img = cv.GaussianBlur(img,(3,3),0)
img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,75,10)
cv.imwrite(r'C:\Users\mohan\Desktop\Final_Project\character_segmentation/clone3.jpg',img)
img = cv.bitwise_not(img)
ret,thresh = cv.threshold(img,127,255,0)
img, contours, hierarchy = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_TC89_KCOS) 
mask = np.zeros(img.shape, np.uint8)
cv.drawContours(mask, contours, -1, (255),1)
img = cv.cvtColor(img,cv.COLOR_GRAY2RGB)
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    crop_img = img [y:y+h, x:x+w]
    r = 100.0 / crop_img.shape[1]
    dim = (100, int(crop_img.shape[0] * r))
    resized = cv.resize(crop_img, dim, interpolation = cv.INTER_AREA)
    resize_img = cv.resize(resized  , (28 , 28))
    row, col= resize_img.shape[:2]
    bottom= resize_img[row-2:row, 0:col]
    mean= cv.mean(bottom)[0]
    bordersize=5
    border=cv.copyMakeBorder(resize_img, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv.BORDER_CONSTANT, value=[0,0,0] )
    r_img = cv.resize(border  , (28 , 28))
    cv.imwrite(r'C:\Users\mohan\Desktop\Final_Project\character_segmentation/hw1/r_'+str(y).zfill(5)+'_'+str(x).zfill(5)+'_'+str(w).zfill(5)+'_'+str(h).zfill(5)+'_.jpg',r_img)
cv.imwrite(r'C:\Users\mohan\Desktop\Final_Project\character_segmentation/clone.jpg',img)
cv.imwrite(r'C:\Users\mohan\Desktop\Final_Project\character_segmentation/clone1.jpg',mask)

