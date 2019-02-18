## Author: Behrad Toghi
## HeyMercedes Project
## http://behrad.toghi.net
## Feb 17, 2019
import houndify
import sys
import json
import requests
from flask import Flask, jsonify, request

#Connect to NYTimes API to acquire the latest popular news in the last week.
#This time period can be changed or even set as a configurable parameter.
def getPopularNews():
  url = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/7.json?api-key=CpOKjWKKSKAtaXrmusZKXsO6GQKWMZaa'
  r = requests.get(url)
  newsJSON = r.json()

  with open('NYTnews.json', 'w') as outfile:
      json.dump(newsJSON, outfile)
  
  return newsJSON