from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf

inputs = keras.Input(shape=(585, 800, 3), name="img")

x = layers.Conv2D(64, 3, activation="relu", padding="same")(inputs)
x = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(32, 3, activation="relu", padding="same")(x)
x = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(16, 3, activation="relu")(x)
x = layers.GlobalAveragePooling2D()(x)

outputs = layers.Dense(16, activation='softmax')(x)

model = keras.Model(inputs, outputs, name="test")
