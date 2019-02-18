## Author: Behrad Toghi
## HeyMercedes Project
## http://behrad.toghi.net
## Feb 17, 2019
import houndify
import sys
import json
import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for
# from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import getNYTimes as NYT
import getHoundify as HND
import os
from werkzeug.utils import secure_filename


# allowed file types initialization
UPLOAD_FOLDER = './test_audio'
ALLOWED_EXTENSIONS = set(['wav', 'ogg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

############### ROUTING

# Just a test route
@app.route('/')
def index():
	return 'Hey Mercedes!'

# This is the text route
@app.route('/MBUXtext/<textIn>', methods=['GET'])
def textCommand(textIn):

	flag = HND.getHoundifyFlag(textIn, 'text')
	
	if flag == True:
		outJSON = NYT.getPopularNews()
	else:
		outJSON = {'ERROR': 'Input command is not defined, try GIVE ME NEWS instead!'} 

	return jsonify(outJSON)

# another route for audio file upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	file= request.files['inputFile']

	return file.filename

@app.route('/MBUXaudio/<fileName>', methods=['GET', 'POST'])
def audioCommand(fileName):
	fileAddress = "./test_audio/" + fileName
	flag = HND.getHoundifyFlag(fileAddress, 'audio')		

	if flag == True:
		outJSON = NYT.getPopularNews()
	else:
		outJSON = {'ERROR': 'Input command is not defined, try GIVE ME NEWS instead!'} 

	return jsonify(outJSON)



# run the application in debug mode
if __name__ == "__main__":
	app.run(debug=True)



