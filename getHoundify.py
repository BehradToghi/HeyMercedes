## Author: Behrad Toghi
## HeyMercedes Project
## http://behrad.toghi.net
## Feb 17, 2019
import houndify
import sys
import json
import time
import wave
from utils import getConfigs


# This function determines what is the operation mode (text/audio) and sets a flag
# If the received JSON from Houndify contains the checkCase string, the flag is set to True
def getHoundifyFlag(inputArg, type):
	checkCase = "NEWS.popular"
	flag = False

	# Reading configs from CONFIGS.txt file
	houndifyID, houndifyKey, nytKey, nytPeriod = getConfigs()
	
	# Decide if the input is text or audio
	if type == 'text':
		responseJSON = getHoundifyTextFlag(inputArg, houndifyID, houndifyKey)
	elif type == 'audio':
		responseJSON = getHoundifyAudioFlag(inputArg, houndifyID, houndifyKey)
	else:		
	# 	print ("data type is invalid, it should be either text or audio")
		responseJSON = list({"AllResults": "ERROR"})

	JSONresults = responseJSON["AllResults"][0]

	if ('Result' in list(JSONresults.keys()) and JSONresults["Result"]['action'] == checkCase):
		flag = True		

	return flag

# Sending a text request to our custom application in Houndify
def getHoundifyTextFlag(textIn, ID, Key):

	QUERY = textIn

	requestInfo = {
	  ## We are at MBRDNA headquarters!
	  'Latitude': 37.386431, 
	  'Longitude': -122.034832
	}

	# Set the Houndify Client
	client = houndify.TextHoundClient(ID, Key, "test_user", requestInfo)

	# Send the text query and receive response from Houndify custom application
	response = client.query(QUERY)
	responseDecoded = response.decode("utf-8")
	responseJSON = json.loads(responseDecoded)

	return responseJSON


# Sending an audio file to be evaluated by our custom application in Houndify
def getHoundifyAudioFlag(audioFile, ID, Key):

	BUFFER_SIZE = 256

	audio = wave.open(audioFile)
	#some sanity checks for the audio file
	if audio.getsampwidth() != 2:
	  print("%s: wrong sample width (must be 16-bit)" % fname)
	  sys.exit()
	if audio.getframerate() != 8000 and audio.getframerate() != 16000:
	  print("%s: unsupported sampling frequency (must be either 8 or 16 khz)" % fname)
	  sys.exit()
	if audio.getnchannels() != 1:
	  print("%s: must be single channel (mono)" % fname)
	  sys.exit()

	# extract audio file attributes
	audio_size = audio.getnframes() * audio.getsampwidth()
	audio_duration = audio.getnframes() / audio.getframerate()
	chunk_duration = BUFFER_SIZE * audio_duration / audio_size

	# StreamingHoundClient method from Houndify API is being used.
	# set a Houndify client
	client = houndify.StreamingHoundClient(ID, Key, "test_user", enableVAD=False)
	client.setLocation(37.386431, -122.034832) # We are at MBRDNA headquarters!
	client.setSampleRate(audio.getframerate())

	# Run the client
	client.start()

	while True:
	  chunk_start = time.time()

	  samples = audio.readframes(BUFFER_SIZE)
	  if len(samples) == 0: break
	  if client.fill(samples): break
	# Finish the client and receieve respons/error
	responseJSON = client.finish() # returns either final response or error

	return responseJSON