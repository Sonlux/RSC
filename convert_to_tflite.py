import tensorflow as tf

# Path to your saved model
h5_model_path = 'pothole_detector.h5'
tflite_model_path = 'pothole_detector.tflite'

# Load the model
model = tf.keras.models.load_model(h5_model_path)

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optional: Optimizations (important for ESP32 memory!)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert the model
tflite_model = converter.convert()

# Save to .tflite file
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)

print(f"✅ TFLite model saved as {tflite_model_path}")
