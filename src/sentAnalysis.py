import vidinput as vid
import os
import time
from pathlib import Path
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2

def trim(image_names):
    for i in image_names:
        temp = face_recognition.load_image_file(i)
        top, right, bottom, left = face_recognition.face_locations(temp)[0]
        cv2.imwrite(i, temp[top:bottom, left:right])
    return image_names

def sameFace(image_names):
    # Encoding of images
    encoding = []

    for i in image_names:
        encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(i))[0])

    # Raise tolerance to make recognition more strict
    return face_recognition.compare_faces([encoding[0]], encoding[1],tolerance=0.50)

def cleanUp():
    for p in Path(".").glob("*.jpg"):
        p.unlink()

def main():
    image_names = trim(vid.capFrame(2))
    print(sameFace(image_names))
    cleanUp()

main()
