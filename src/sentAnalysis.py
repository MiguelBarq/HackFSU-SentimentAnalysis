import vidinput as vid
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2

vid.capFrame(1)

image1 = Image.open("frame0.jpg")
image_array1 = np.array(image1)
plt.imshow(image_array1)
plt.show()
