import numpy as np
from keras.models import model_from_json
import tensorflow as tf
import sys 
import os
from glob import glob
import cv2 as cv

sys.path.append(os.path.abspath("./model"))


def init(): 
	json_file = open('model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("model.h5")
	print("Loaded Model from disk")
	loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	graph = tf.get_default_graph()
	return loaded_model,graph

global model, graph
model, graph = init()

dict = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
        '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F', '16':'G', '17':'H', '18':'I', '19':'J',
        '20':'K', '21':'L', '22':'M', '23':'N', '24':'O', '25':'P', '26':'Q', '27':'R', '28':'S', '29':'T',
        '30':'U', '31':'V', '32':'W', '33':'X', '34':'Y', '35':'Z', '36':'a', '37':'b', '38':'d', '39':'e',
        '40':'f', '41':'g', '42':'h', '43':'n', '44':'q', '45':'r', '46':'t'}

line = 1
word = 1
finalstr = ''
files_list = glob(os.path.join('/users/swathi/desktop/finalsort/*.jpg'))
for a_file in sorted(files_list):        
    img = cv.imread(a_file,0)
    st = a_file
    path, l, w, x, f = st.split('_')
    x = img
    x = x.reshape(1,28,28,1)
    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out,axis=1))
        print("debug3")
        response = str(np.argmax(out,axis=1))[1:-1]
        response = dict[response]
    if(line == int(l)):
        if(word == int(w)):
            finalstr += response
        else:
            finalstr += ' '+response
            word += 1
    else:
        finalstr += '\n'+response
        word += 1
        line += 1

output = open("Output.txt", "w")
output.write(finalstr)
output.close()
	