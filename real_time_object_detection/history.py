
import csv
import os
from datetime import datetime

def save_history(object_counts):
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "outputs", "detection_history.csv")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date and Time", "Object", "Count"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for object_name, count in object_counts.items():
            writer.writerow([timestamp, object_name, count])

    print("Detection history saved:", file_path)
