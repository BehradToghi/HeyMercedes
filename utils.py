## Author: Behrad Toghi
## HeyMercedes Project
## http://behrad.toghi.net
## Feb 17, 2019
import json


# This function reads the configurations from a text file to be used in other modules
def getConfigs():

	filename = 'CONFIGS.txt'

	configs = {}
	with open(filename) as fl:
	    for line in fl:
	        config, value = line.strip().split(' ', 1)
	        configs[config] = value.strip()

	configsJSON = json.dumps(configs, indent=2, sort_keys=True)
	configsDict = json.loads(configsJSON)

	houndifyID = configsDict["HOUNDIFYID"] 
	houndifyKey = configsDict["HOUNDIFYKEY"]  
	nytKey = configsDict["NYTKEY"]  
	nytPeriod = configsDict["NYTPERIOD"] 

	return houndifyID, houndifyKey, nytKey, nytPeriod


