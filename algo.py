import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Dataset path
dataset_path = "My Dataset/train"

# Parameters
img_size = (64, 64)
batch_size = 16

# Data generator
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(dataset_path,
                                        target_size=img_size,
                                        batch_size=batch_size,
                                        class_mode='binary',
                                        subset='training')

val_gen = datagen.flow_from_directory(dataset_path,
                                      target_size=img_size,
                                      batch_size=batch_size,
                                      class_mode='binary',
                                      subset='validation')

# Model
model = Sequential([
    Conv2D(16, (3,3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(train_gen, validation_data=val_gen, epochs=10)

# Save
model.save("pothole_detector.h5")
