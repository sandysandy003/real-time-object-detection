\# Real-Time Object Detection Using YOLO



\## Project Overview

This project detects objects in real time using a webcam. It uses the YOLO object detection model, Python, and OpenCV to identify objects, display bounding boxes, and count detected objects.



\## Features

\- Real-time object detection using a webcam

\- Object names and bounding boxes

\- Live object counting

\- Save detection images

\- Save detection history in CSV format

\- GUI with Start Detection, Stop Detection, Open Output Folder, and View Detection History buttons



\## Technologies Used

\- Python

\- YOLO (Ultralytics)

\- OpenCV

\- Tkinter

\- CSV



\## Project Structure

\- `main.py` — runs real-time object detection

\- `gui.py` — graphical user interface

\- `history.py` — saves detection history

\- `yolo26n.pt` — YOLO model weights

\- `outputs/` — stores detection images and history



\## Installation

1\. Install Python.

2\. Install the required packages:

&nbsp;  `pip install -r requirements.txt`

3\. Make sure `yolo26n.pt` is in the project folder.



\## How to Run

1\. Open a terminal in the project folder.

2\. Run `python gui.py`.

3\. Click \*\*START DETECTION\*\*.

4\. Press `S` in the webcam window to save a detection image and history.

5\. Press `Q` in the webcam window to exit detection.



\## Author

Add your name here.



\## Future Improvements

\- Object detection reports and charts

\- Detection from uploaded images and videos

\- Improved detection performance



