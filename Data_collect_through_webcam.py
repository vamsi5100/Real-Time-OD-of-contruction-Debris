import cv2
import os
import time
import sys
import uuid
Images_path = sys.argv[1]
labels = ['hi','NO','Yo','yes']
num_imgs = sys.argv[2]
for label in labels:
  !mkdir {os.path.join(Images_pathma,label)}
  cap = cv2.VideoCapture(0)
  print('collecting images for {}'.format(label)) 
  time.sleep(5)
  for imgnum in range(num_imgs):
    ret,frame = cap.read()
    imagename = os.path.join(Images_path,label,label+'.'+'{}.jpg'.format(uuid.uuid1()))
    cv2.imwrite(imagename,frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()                   
    time.sleep(2)
    if cv2.waitKey(0) & 0xFF == ord('q'):
       break
  cap.release()