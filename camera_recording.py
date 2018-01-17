import cv2
import os
import time


def record(number):
    print("Start recording..")
    count = number
    vidName = "recording" + '.mp4'
    # MP4 codec
    #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # Change current directory to output directory to save the video in the same folder as the snapshots.
    os.chdir(outputDir)
    # Create the video file
    #out = cv2.VideoWriter(vidName, fourcc, 10.0, (320, 176))

    while(count > 0):
        # Access camera feed
        cap = cv2.VideoCapture("http://admin:123456@192.168.0.158/tmpfs/auto.jpg")
        # Receive frames
        ret, frame = cap.read()
        if not ret:
            break
        else:
            # Rename each frame
            name = "snapshot"+str(count)+".jpg"
            # Save each frame
            cv2.imwrite(os.path.join(outputDir,name), frame)
            # Add each frame to the video
            #out.write(frame)
            count -= 1
            print("Saving snapshot "+str(80-count)+"/"+str(number)+"..")
    # Release video
    #out.release()
    # Release camera feed
    print("Writing video..")
    os.system('sudo avconv -r 10 -i snapshot%d.jpg -b:v 1000k recording.mp4')
    print("Writing successful..")
    cap.release()
    cv2.destroyAllWindows()
    
    print("End recording..")

def test(): 
    print("Start intruder recognition..")
    intruder = 0
    face_cascade = cv2.CascadeClassifier('/home/pi/Chub/CHUB/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/home/pi/Chub/CHUB/haarcascade_eye.xml')
    for i in range(1,number):
        img = cv2.imread('snapshot'+str(i)+".jpg");
        #cv2.imshow('img',img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imwrite("face"+str(i)+".jpg", img)
            intruder += 1
    print("Intruder recognition completed..")
    if(intruder>0):
        print("/!\WARNING/!\ INTRUDER DETECTED /!\WARNING/!\ ")
    else: print("No intruder detected")

def recordnow():
    #Below code will capture X snapshots, store them in a specific folder with timestamps and create a short .MP4 movie with it
	dirname = time.strftime("/%Y-%m-%d_%Hh%Mm%Ss")
    #Directory that will receive all the shots + the recording video
    outputDir = '/var/www/ChubFront/Files'+ dirname
    print("Creating folder..")
    os.makedirs(outputDir)
    number = 80

    record(number)
    test()
    return '/Files'+dirname
