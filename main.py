import cv2
import time
import os
import cognitive_face as CF
import serial
ard = serial.Serial('/dev/ttyACM0', 9600)
print 'Program Initializing... Please wait patiently'
KEY = 'PUT API KEY HERE'
CF.Key.set(KEY)
#Init Retrieving sample photo IDs
faceList = []
nameList = []
for samplePic in os.listdir('/home/linaro/Desktop/PhotoLibrary'):
    faceList.append(CF.face.detect('/home/linaro/Desktop/PhotoLibrary/' + samplePic)[0]['faceId'])
    nameList.append(samplePic[:len(samplePic)-4])
print 'Init Done.'

def saveImg(name):
    cam = cv2.VideoCapture(0)
    s, im = cam.read()
    cv2.imwrite(name, im)
    cam = 0        #Reset camera
def readSens():
    ard.flushInput()
    time.sleep(0.1)
    return int(filter(str.isdigit, ard.readline())) + 0

while True:
    print 'Looping'
    ard.write('1')
    time.sleep(0.2)
   # print readSens()
   # print type(readSens())
   # print readSens() < 50
    while(readSens() < 50):
        print 'Start taking pic'
        saveImg('photo.bmp')
        newFace = CF.face.detect('photo.bmp')
        if len(newFace) == 0:
            print 'Face not detected!'
        else:
            newId = newFace[0]['faceId']
            result = CF.face.find_similars(newId, None, faceList)
            print 'Result Available'
            if len(result) == 0:
                print 'New face!'
                ard.write('1' + 'Denied Entry') 
            else:
                faceSimilarId = result[0]['faceId']
                index = 0
                for ids in faceList:
                    if faceSimilarId == ids:
                        break
                    index += 1
                print 'FaceBy  ' + nameList[index]
                ard.write('1' + nameList[index])
                print 'Confidence level ' + str(result[0]['confidence'])
                time.sleep(2)
