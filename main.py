
import cv2
from ultralytics import YOLO
from collections import Counter
import os
from history import save_history

model = YOLO("yolo26n.pt")
camera = cv2.VideoCapture(0)

os.makedirs("outputs", exist_ok=True)

if not camera.isOpened():
    print("Error: Cannot open webcam.")
    raise SystemExit

print("Real-Time Object Detection Started!")
print("Press S to save an image.")
print("Press Q to exit.")

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Cannot read webcam frame.")
            break

        results = model.predict(
            source=frame,
            conf=0.30,
            verbose=False
        )

        output = results[0].plot()

        class_ids = results[0].boxes.cls.tolist()
        names = results[0].names
        counts = Counter(
            names[int(class_id)] for class_id in class_ids
        )

        cv2.putText(
            output, "OBJECT COUNTS", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

        y = 60
        for name, count in counts.items():
            cv2.putText(
                output, f"{name}: {count}", (10, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
            )
            y += 30

        cv2.imshow("Real-Time Object Detection", output)

        key = cv2.waitKey(1) & 0xFF


        if key == ord("s"):
            cv2.imwrite("outputs/detection_result.jpg", output)
            save_history(counts)
            print("Detection result and history saved!")

        elif key == ord("q"):
            break


  
finally:
    camera.release()
    cv2.destroyAllWindows()
