from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

imagegen = ImageDataGenerator(rescale=1./255., rotation_range=30, horizontal_flip=True, validation_split=0.1)

path_to_zip = os.getcwd() + "\\---"
PATH = os.path.join((path_to_zip), '')

