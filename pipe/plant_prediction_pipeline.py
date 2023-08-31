import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

def plant_recognition():
    cnn = tf.keras.models.load_model('models/Plant_Recognition.h5')
    image_path = 'images/Untitled.jpeg'

    image = tf.keras.preprocessing.image.load_img(image_path,target_size=[64,64])
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #Converting single image to batch
    predictions = cnn.predict(input_arr)

    return predictions

