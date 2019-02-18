#!/bin/bash


testInput=$2



if [ "$1" = "text" ]; then
	echo "Evaluating the TEXT input..."
	echo "Sending text input to Houndify: $testInput" 
	
	serverAddress="http://127.0.0.1:5000/MBUXtext/$testInput"
	echo Fetching News from: $serverAddress
	curl $serverAddress

elif [ "$1" = "audio" ]; then
	echo "Evaluating the AUDIO input..."
	echo "Sending audio input to Houndify: $testInput" 
	serverAddress="http://127.0.0.1:5000/MBUXaudio/$testInput"
	echo Fetching News from: $serverAddress
	curl $serverAddress
else 
	echo "ERROR: input is not defined! Only audio and text modes are supported."
fi



