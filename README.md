# Setup instructions
This project uses [OpenCV](http://opencv.org/) to take photos, and [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services) to compute.

The main code runs on Python 2.7 in Debian Operating System

##Installation
Make sure to cd into your working folder before execute these commands!
```bash
sudo apt-get update   #Update the operating system
sudo apt-get install python python-pip git libopencv-dev python-opencv
#If it shows "After this operation, ?? MB of additional disk space will be used.
#Do you want to continue? [Y/n]" Please type "Y" to agree installation.
sudo pip install cognitive_face
git clone https://github.com/Microsoft/Cognitive-Face-Python.git
cd Cognitive-Face-Python
sudo python setup.py install
cd ..  #Go back to working directory
git clone https://github.com/zhaomh1998/FacialRecognitionSmartHome.git
cd FacialRecognitionSmartHome
```
