#importing the libraries
import cv2
import time
import winsound
#loading the data

eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")

#detecting 

#1 converting into gray and detecting
def detect(gray,frame):
    eye=eye_cascade.detectMultiScale(gray,1.3,5) #here the eyes are detected by algorithm and also converted into gray

    
    
    if eye == ():
        time.sleep(5)
        winsound.Beep(5000,200)
    #2 drawing the rectangle in eye
    for(x,y,w,h)in eye:
        rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
        

        if rectangle.any()==True:
            cv2.putText(rectangle,"Eyes opened",(400,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

        
    return frame

#take input from camera

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()