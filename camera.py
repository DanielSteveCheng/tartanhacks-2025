import cv2
from ultralytics import YOLO
import numpy as np
# face_cascade = cv2.CascadeClassifier("")

model = YOLO("yolov8n.pt")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.releast()

    def get_frame(self):
        ret, frame = self.video.read()

        # # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BGGR2GRAY)
        # ret, jpeg = cv2.imencode('.jpg', frame)

        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0]) 
                confidence = box.conf[0]
                label = box.cls[0]
                
                if confidence > 0.4:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    cv2.putText(frame, f'{model.names[int(label)]}: {confidence:.2f}', (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Trash Detection (Real-time)', frame)

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
