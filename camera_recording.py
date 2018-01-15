import cv2
import os
import time

#Below code will capture X snapshots, store them in a specific folder with timestamps and create a short .MP4 movie with it

#Directory that will receive all the shots + the recording video
outputDir = '/Users/thibaud/Desktop'+time.strftime("/%Y-%m-%d_%Hh%Mm%Ss")
os.makedirs(outputDir)

def record(number):
    count = number
    vidName = "recording" + '.mp4'
    # MP4 codec
    fourcc = cv2.VideoWriter_fourcc(*'a\0\0\0')
    # Change current directory to output directory to save the video in the same folder as the snapshots.
    os.chdir(outputDir)
    # Create the video file
    out = cv2.VideoWriter(vidName, fourcc, 20.0, (320, 176))

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
            out.write(frame)
            count -= 1
    # Release video
    out.release()
    # Release camera feed
    cap.release()
    cv2.destroyAllWindows()

record(80)