import cognitive_face as CF
KEY = 'PUT API KEY HERE'
CF.Key.set(KEY)
import time
import cv2
cv2.namedWindow("preview")
def checkValid(img):
    cv2.imwrite('local.jpg', img)
    if len(CF.face.detect('local.jpg')) == 0:
        return False
    else:
        return True

while True:
    print 'Start photo'
    vc = 0
    vc = cv2.VideoCapture(0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
        while not checkValid(frame):
            print 'Face not detectable! Retaking...'
            vc = 0
            time.sleep(0.5)
            vc = cv2.VideoCapture(0)
            print 1
            rval, frame = vc.read()
            print 2
    else:
         rval = False
    while rval:
        cv2.imshow("preview", frame)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")
    print 'To accept, type your name'
    print 'To re-take the photo, type 1'
    print 'To exit, type 0'
    choice = raw_input()
    if choice == '1':
        continue
    elif choice == '0':
        break
    else:
        filename = choice + '.bmp'
        print filename
        cv2.imwrite('/home/linaro/Desktop/PhotoLibrary/' + filename, frame)
        print('Photo Saved as ' + filename)
        print 'To take another photo, type 1'
        print 'To exit, type anything'
        if raw_input() == '1':
            continue
        else:
            break
        
