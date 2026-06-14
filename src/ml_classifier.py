from picamera2 import Picamera2
import cv2
import numpy as np
import time
import tflite_runtime.interpreter as tflite
MODEL_PATH = "model_unquant.tflite"
LABELS_PATH = "labels.txt"
with open(LABELS_PATH, "r") as f:
    labels = [line.strip().split(" ", 1)[1] for line in f]
interpreter = tflite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_height = input_details[0]['shape'][1]
input_width = input_details[0]['shape'][2]
picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)
picam2.configure(config)
picam2.start()
time.sleep(2)
ROI_SIZE = 300
ROI_Y_OFFSET = 20
def classify_object():
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    h, w, _ = frame.shape
    cx = w // 2
    cy = h // 2 + ROI_Y_OFFSET
    x1 = cx - ROI_SIZE // 2
    y1 = cy - ROI_SIZE // 2
    x2 = cx + ROI_SIZE // 2
    y2 = cy + ROI_SIZE // 2

    roi = frame[y1:y2, x1:x2]

    img = cv2.resize(roi, (input_width, input_height))
    img = img.astype(np.float32)
    img = (img / 127.5) - 1

    img = np.expand_dims(img, axis=0)

    interpreter.set_tensor(
        input_details[0]['index'],
        img
    )
    interpreter.invoke()
    output = interpreter.get_tensor(
        output_details[0]['index']
    )[0]
    class_id = np.argmax(output)
    confidence = float(output[class_id])
    prediction = labels[class_id]
    return prediction, confidence
def cleanup():
    picam2.stop()
    cv2.destroyAllWindows()
