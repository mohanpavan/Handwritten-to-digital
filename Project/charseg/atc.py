import cv2 as cv
import numpy as np
img = cv.imread('equation.jpg',0)
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
    #r = 100.0 / crop_img.shape[1]
    #dim = (100, int(crop_img.shape[0] * r))
    #resized = cv.resize(crop_img, dim, interpolation = cv.INTER_AREA)
    cv.imwrite(str(x)+'_'+str(y)+'.jpg',resized)
cv.imwrite('clone.jpg',img)
cv.imwrite('clone1.jpg',mask)