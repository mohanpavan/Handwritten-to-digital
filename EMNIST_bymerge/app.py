#imports
from flask import Flask, render_template,request
from scipy.misc import imsave, imread, imresize, imshow
import numpy as np
import keras.models
from keras.models import model_from_json
import tensorflow as tf
import re
import sys 
import os
import base64

#path to the saved model
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

#initalize the flask app
app = Flask(__name__)

#global variables
global model, graph
model, graph = init()

#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search(b'base64,(.*)',imgData1).group(1)
	with open('output.png','wb') as output:
		output.write(base64.b64decode(imgstr))
	

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_data()
	convertImage(imgData)
	print("debug")
	x = imread('output.png',mode='L')
	x = np.invert(x)
	x = imresize(x,(28,28))
	x = x.reshape(1,28,28,1)
	print("debug2")
	with graph.as_default():
		out = model.predict(x)
		print(out)
		print(np.argmax(out,axis=1))
		print("debug3")
		response = np.array_str(np.argmax(out,axis=1))
		return response	
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
