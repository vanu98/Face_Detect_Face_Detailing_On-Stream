import numpy as np
import cv2



font                   = cv2.FONT_HERSHEY_DUPLEX
bottomLeftCornerOfText = (0,30)
fontScale              = 1
fontColor              = (0,0,0)
lineType               = 5



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture('aa.mp4')
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),0)
#			roi_gray = gray[y:y+h, x:x+w]
#			roi_color = img[y:y+h, x:x+w]
#			roi_gray = cv2.GaussianBlur(roi_color,(23, 23), 30)
			ret,img[y:y+h, x:x+w] = cv2.threshold(img[y:y+h, x:x+w],127,255,cv2.THRESH_BINARY)
			cv2.putText(img,'No of faces:'+str(len(faces)), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
		cv2.imshow('img',img)
        # & 0xFF is required for a 64-bit system
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
