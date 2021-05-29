import cv2 as cv
import glob
import os
import numpy as np
img = cv.imread('/users/swathi/desktop/hw1/hw1.jpg',0)
img = cv.GaussianBlur(img,(3,3),0)
img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,75,10)
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
    #k = cv.waitKey(0)
    #if k == 27:
     #   cv.destroyWindow('img')
    resize_img = cv.resize(resized  , (28 , 28))
    #cv.imshow('img' , resize_img)
    #x = cv.waitKey(0)
    #if x == 27:
    #   cv.destroyWindow('img')
    
    cv.imwrite('/users/swathi/desktop/hw1/r_'+str(y).zfill(5)+'_'+str(x).zfill(5)+'_'+str(w).zfill(5)+'_'+str(h).zfill(5)+'_.jpg',resize_img)
cv.imwrite('/users/swathi/desktop/hw1/clone.jpg',img)
cv.imwrite('/users/swathi/desktop/hw1/clone1.jpg',mask)

