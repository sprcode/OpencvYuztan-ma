from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

yuz_cascade=cv2.CascadeClassifier('/home/pi/Desktop/opencv/face.xml')
 
def main():
    #kamerayı başlat 
    camera=PiCamera()
    camera.resolution=(640,480)
    camera.framerate=32
    rawCapture=PiRGBArray(camera,size=(640,480))
 
    #kamera için bekleme
    time.sleep(0.1)
 
    for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
        #resimi temsil eden numPy dizisini alıp imgOriginal içine atıyoruz
 
        imgOriginal=frame.array
     
        griton=cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
        yuzler = yuz_cascade.detectMultiScale(griton, 1.3, 4)
        
 
        for (x, y, w, h) in yuzler:
            cv2.rectangle(imgOriginal, (x, y), (x + w, y + h), (0, 255, 255), 3)

        cv2.imshow("imgOriginal",imgOriginal)
        cv2.imshow("GRAY",griton)

        
 
        key=cv2.waitKey(1)&0xFF
 
        rawCapture.truncate(0) # birsonraki frame için rawCapture temizliyoruz.
 
        if key == ord("q"): # klavyeden q tuşuna basılırsa döngüyü sonlandır.
            return
 
if __name__ == "__main__":
        main()