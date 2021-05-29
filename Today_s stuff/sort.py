import cv2 as cv
from glob import glob
import os
files_list = glob(os.path.join('/users/swathi/desktop/hw1/r*.jpg'))
sorted(files_list)
line = 1
path, y, x, w, h, f = files_list[0].split('_')
liney = int(y)
lineh = int(h)
#print(liney+" "+lineh)
for a_file in sorted(files_list):
    img = cv.imread(a_file,0)
    st = a_file
    path, y, x, w, h, f = st.split('_')
    print(y+" "+x+" "+w+" "+h)
    print(y+" "+str(liney+lineh*(4/3)))
    if(int(y) <= liney + lineh*(4/3)):
        cv.imwrite('/users/swathi/desktop/hw/_'+str(line)+'_'+x+'_'+w+'_'+h+'_.jpg',img)
    else:
        line += 1
        liney = int(y)
        lineh = int(h)
        cv.imwrite('/users/swathi/desktop/hw/_'+str(line)+'_'+x+'_'+w+'_'+h+'_.jpg',img)
        