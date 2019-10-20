import vidinput as vid
from statistics import mode
from pathlib import Path
# from matplotlib import pyplot as plt
import numpy as np
import face_recognition
from keras.models import load_model
import cv2

# Globally loading the model for optimization purposes
model = load_model("../data/_mini_XCEPTION.106-0.65.hdf5")

"""
Input: List of image file names
Output: List of image files names, but with images trimmed to only faces
"""
def trim(image_names):
    for i in image_names[::-1]:
        temp = face_recognition.load_image_file(i)
        try:
            top, right, bottom, left = face_recognition.face_locations(temp)[0]
            cv2.imwrite(i, temp[top:bottom, left:right])
        except:
            image_names.remove(i)
    return image_names

"""
Input: List of image file names
Output: True/False - all images contain the same face
"""
def sameFace(image_names):
    # Encoding of images
    encoding = []

    for i in image_names:
        encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(i))[0])

    # Raise tolerance to make recognition more strict
    return face_recognition.compare_faces([encoding[0]], encoding[1],tolerance=0.50)

"""
Removes residual image files
"""
def cleanUp():
    for p in Path(".").glob("*.jpg"):
        p.unlink()
    for p in Path(".").glob("*.png"):
        p.unlink()
    for p in Path(".").glob("*.jpeg"):
        p.unlink()
    for p in Path(".").glob("*.gif"):
        p.unlink()

def analysis(image_name):
    emotion_dict = {
        'Angry': 0,
        'Disgust': 1,
        'Fear': 2,
        'Happy': 3,
        'Neutral': 4,
        'Sad': 5,
        'Surprise': 6
    }

    # Loading in jpg
    face_image = cv2.imread(image_name)
    # plt.imshow(face_image)
    # plt.show()

    # Lowering resolution for computer vision
    face_image = cv2.resize(face_image, (64,64))

    # "Grayscale" they said...
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('test.jpg', face_image)
    # plt.imshow(face_image)
    # plt.show()

    # Reformatting
    face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
    predicted_class = np.argmax(model.predict(face_image))
    label_map = dict((v,k) for k,v in emotion_dict.items())
    print(predicted_class)
    predicted_label = label_map[predicted_class]

    return predicted_label

"""
Input: FPS
Output: Emotion analysis over fps number of photos take in one second
Note: This is meant to be run in a for-loop, with each iteration representing
      how often you run analysis
"""
def sentAnalysis(fps):
    # Holds the sentiment analysis results per image
    analysis_list = []
    image_names = trim(vid.capFrame(fps))
    if len(image_names) == 0:
        return "No faces recognized"

    #else
    for i in image_names:
        analysis_list.append(analysis(i))

    # cleanUp()
    return mode(analysis_list)

print(sentAnalysis(1))
