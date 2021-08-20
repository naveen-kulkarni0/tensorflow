# print("hello")
import tensorflow as tf;
import keras
import os
import sys
from keras.preprocessing.image import ImageDataGenerator

class_names = ['roses', 'daisy', 'dandelion', 'sunflowers', 'tulips']
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

test_path = os.path.join(base_dir, 'flower-classification-tensorflow/test')
test_dir = ImageDataGenerator(rescale=1./255)
# test_data = test_dir.flow_from_directory(test_path,class_mode='sparse')
test_data = tf.keras.preprocessing.image_dataset_from_directory(test_path)
print(test_data.class_names)