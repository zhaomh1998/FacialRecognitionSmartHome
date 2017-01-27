import cv2
import time
import os
import cognitive_face as CF
print 'Program Initializing... Please wait patiently'
KEY = 'API KEY HERE'
CF.Key.set(KEY)
#Init Retrieving sample photo IDs
faceList = []
nameList = []
for samplePic in os.listdir('/home/linaro/Desktop/PhotoLibrary'):
    faceList.append(CF.face.detect('/home/linaro/Desktop/PhotoLibrary/' + samplePic)[0]['faceId'])
    nameList.append(samplePic[:len(samplePic)-4])

def saveImg(name):
    cam = cv2.VideoCapture(0)
    s, im = cam.read()
    #print 's=' + str(s) S is true when succeeded
    cv2.imwrite(name, im)
    cam = 0        #Reset camera

saveImg('photo.bmp')
print 'Done Taking photo'
newFace = CF.face.detect('photo.bmp')
if len(newFace) == 0:
    print 'Face not detected!'
else:
    newId = newFace[0]['faceId']
    print 'Start uploading'
    result = CF.face.find_similars(newId, None, faceList)
#print result
    print 'Result Available'
    if len(result) == 0:
        print 'New face!'
    else:
        faceSimilarId = result[0]['faceId']
        index = 0
        for ids in faceList:
            if faceSimilarId == ids:
                break
            index += 1
        print 'FaceBy  ' + nameList[index]
        print 'Confidence level ' + str(result[0]['confidence'])
