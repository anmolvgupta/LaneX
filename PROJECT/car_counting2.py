import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import Tracker

# Load YOLO model
model = YOLO('yolov9c.pt')

# Class list from the COCO dataset
class_list = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# Initialize Tracker and video capture
tracker = Tracker()
cap = cv2.VideoCapture('road2.mp4')  # Replace with your video path

# Car count variable
car_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection using YOLO
    results = model.predict(frame)
    a = results[0].boxes.data
    a = a.detach().cpu().numpy()
    px = pd.DataFrame(a).astype("float")

    # List to store detected cars
    car_list = []
    
    # Filter for detected cars
    for index, row in px.iterrows():
        x1, y1, x2, y2, conf, d = map(int, row[:6])  # Extract bounding box coordinates and class
        c = class_list[d]
        if 'car' in c:
            car_list.append([x1, y1, x2, y2])

    # Update tracker and get unique car IDs
    bbox_id = tracker.update(car_list)
    # Draw bounding boxes and IDs on frame
    for bbox in bbox_id:
        x, y, w, h, id = bbox
        cv2.rectangle(frame, (x, y), (w, h), (255, 0, 255), 2)
        cv2.putText(frame, f'ID: {id}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    car_count = len(bbox_id)  # Count unique cars

    # Save car count to file
    # Read existing counts or initialize
    try:
        with open("car_counts.txt", "r") as f:
            counts = list(map(int, f.read().strip().split(',')))
    except FileNotFoundError:
        counts = [0, 0, 0]

    # Update only index 0 for this video
    counts[1] = car_count

    # Write updated counts back to file
    with open("car_counts.txt", "w") as f:
        f.write(','.join(map(str, counts)))


    # Display the processed frame
    cv2.imshow("Video 2", frame)

    if cv2.waitKey(0) & 0xFF == 27:  # Press "Esc" to exit
        break

cap.release()
cv2.destroyAllWindows()
