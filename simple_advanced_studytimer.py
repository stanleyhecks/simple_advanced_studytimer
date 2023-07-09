import tensorflow.keras
import numpy as np
import cv2
import time

model_filename = 'YOUR_KERAS_MODEL_PATH'

model = tensorflow.keras.models.load_model(model_filename)

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

start_time = None
total_studying_time = 0

def preprocessing(frame):
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))
    return frame_reshaped

def predict(frame):
    prediction = model.predict(frame)
    return prediction

while True:
    ret, frame = capture.read()

    if cv2.waitKey(100) > 0:
        break

    preprocessed = preprocessing(frame)
    prediction = predict(preprocessed)

    if prediction[0, 0] < prediction[0, 1]:  # Not studying
        if start_time is not None:
            end_time = time.time()
            studying_time = end_time - start_time
            total_studying_time += studying_time
            start_time = None
        cv2.putText(frame, 'Not studying', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
    else:  # Studying
        if start_time is None:
            start_time = time.time()
        cv2.putText(frame, 'Studying', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    hours = int(total_studying_time // 3600)
    minutes = int((total_studying_time % 3600) // 60)
    seconds = int(total_studying_time % 60)
    time_text = "Total Studying Time: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    cv2.putText(frame, time_text, (0, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    cv2.imshow("VideoFrame", frame)
