# Speech Recognition
Speech recognition project using [SpeechRecognition](https://github.com/Uberi/speech_recognition) library. The goal of this project is to build a fully functional speech recognition given by the user with microphone, also apply this to build a small game about name gussing. The most important thing is to understand how speech recognition worksk in depth. The following commands are linux based.

## Prerequisites
- python, pip, 
- gTTS `sudo pip install gTTS`
- SpeechRecognition `sudo pip insall SpeechRecognition` 
- portaudio19-dev `sudo apt-get install portaudio19-dev` (required for PyAudio)
- PyAudio `sudo pip install PyAudio`

## Usage
run the main.py file: `python main.py`. Once started, each word you say will be displayed on the command line while also saving them as a string and later saving the text as .mp3 format 

run the game.py game file: `python game.py`. Once started you will be requested to chooose (speech to the microphone) one among the options, if you fail 3 times you lost the game.

## Resources
- [SpeechRecognition github](https://github.com/Uberi/speech_recognition)
- [Guide to speech rocognition](https://realpython.com/python-speech-recognition/)
- [Hidden Markov Model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- [Cepstrum](https://en.wikipedia.org/wiki/Cepstrum) 
- [gTTS](https://gtts.readthedocs.io/en/latest/)


