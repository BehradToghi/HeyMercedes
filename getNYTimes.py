## Author: Behrad Toghi
## HeyMercedes Project
## http://behrad.toghi.net
## Feb 17, 2019
import houndify
import sys
import json
import requests
from flask import Flask, jsonify, request
from utils import getConfigs

#Connect to NYTimes API to acquire the latest popular news in the rime period.
def getPopularNews():
	
	# Reading configs from CONFIGS.txt file
	houndifyID, houndifyKey, nytKey, nytPeriod = getConfigs()
	
	# Creating the appropriate url to be sent to NYTimes API
	url = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/' + nytPeriod + '.json?api-key=' + nytKey
	
	# Receiving popular news from NYTimes
	r = requests.get(url)
	newsJSON = r.json()

	# Write the received JSON to a file
	with open('NYTnews.json', 'w') as outfile:
	  json.dump(newsJSON, outfile)
	return newsJSON