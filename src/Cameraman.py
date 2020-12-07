import cv2 as cv
import sys

cascPath = sys.argv[1]
faceCascade = cv.CascadeClassifier(cascPath)

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('Video', frame)