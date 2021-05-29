import cv2 as cv
from glob import glob
import os
files_list = glob(os.path.join(r'C:\Users\mohan\Desktop\FinalProject\hw\_*.jpg'))
sorted(files_list)
word = 1
path, l, x, w, h, f = files_list[0].split('_')
linex = int(x)
linew = int(w)
line = 1
for a_file in sorted(files_list):
    img = cv.imread(a_file,0)
    st = a_file
    path, l, x, w, h, f = st.split('_')
    print(l+" "+x+" "+w+" "+h)
    print(x+" "+str(linex+linew*(6/4)))
    if(int(l) == line):
        if(int(x) <= linex +linew*(6/4)):
            cv.imwrite(r'C:\Users\mohan\Desktop\FinalProject\finalsort\_'+l+'_'+str(word)+'_'+x+'_.jpg',img)
            linex = int(x)
        else:
            word += 1
            linex = int(x)
            linew = int(w)
            cv.imwrite(r'C:\Users\mohan\Desktop\FinalProject\hw\finalsort\_'+l+'_'+str(word)+'_'+x+'_.jpg',img)
    else:
        line += 1
        word += 1
        linex = int(x)
        linew = int(w)
        cv.imwrite(r'C:\Users\mohan\Desktop\FinalProject\hw\finalsort\_'+l+'_'+str(word)+'_'+x+'_.jpg',img)
      
        
        
        
        