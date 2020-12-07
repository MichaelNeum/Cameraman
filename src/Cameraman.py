import cv2
import sys
import serial

arduinoPort = serial.Serial()
arduinoPort.baudrate = 9600
arduinoPort.port = "COM3"

arduinoPort.open()

cascPath = "C:\Michael\GitHub\Cameraman\src\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        flags= None,
        minSize=(30, 30),
        maxSize= None
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        print(str(x))
        output = str(x) + "f"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    arduinoPort.write(output.encode())

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
arduinoPort.close()