# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:38:57 2021

@author: alexa
"""

from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array,load_img

dog="Dog"
cat="Cat"

sample_CAT_image = "training/cat/cat_1.jpg"

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1.0/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

img = load_img(sample_CAT_image, color_mode='grayscale', target_size=(300, 300))

x = img_to_array(img)
x =x.reshape((1,)+x.shape)

i=0
for batch in datagen.flow(x,batch_size=1,save_to_dir='preview', save_prefix=cat,save_format='jpeg'):
    i+=1
    if i>20:
        break