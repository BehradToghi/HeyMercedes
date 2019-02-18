# Mercedes Benz Project - News Catcher 
# Author: Behrad Toghi, http://behrad.toghi.net

This is a project for my internship application to #HeyMercedes team at MBRDNA, CA, USA. This simple web service takes a text or audio file as input and uses the Houndify SDK alongside with New York Times API to acquire popular news items as a JSON file.


## Instal the Dependencies 
This implementation runs on Flask web platform for Python 3.x

```bash
sudo pip3 install Flask
```

## Running the module

Please download the repository. Activate the web service by running:

```bash
python3 MBUX_News.py 
```

You can run the application (runMBUX.sh) in two "audio" and "text" modes as follows:

```bash
chmod +x ./runMBUX.sh 
./runMBUX.sh  <mode=audio/text> <name of audio file/input text in HTML format>
```

Test audio files are saved in "test_audio" directory.


### Some test cases
You can try running following scenarios as some examples:

```bash
./runMBUX.sh text give%20me%20apple
./runMBUX.sh text give%20me%20news
./runMBUX.sh text give%20me%20popular%20news
./runMBUX.sh audio turnthelightson.wav
./runMBUX.sh audio givemenews.wav
./runMBUX.sh audio givemepopularnews.wav
```


### Output JSON
output JSON file containing the news is saved to "./NYTnews.json"