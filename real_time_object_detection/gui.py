
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

root = tk.Tk()
root.title("Real-Time Object Detection")
root.geometry("600x480")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

process = None

title = tk.Label(
    root,
    text="REAL-TIME OBJECT DETECTION",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="YOLO | OpenCV | Python",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="#b8c7e0"
)
subtitle.pack(pady=5)

status = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white"
)
status.pack(pady=15)

def start_detection():
    global process

    if process is not None and process.poll() is None:
        status.config(text="Detection is already running!", fg="orange")
        return

    try:
        folder = os.path.dirname(os.path.abspath(__file__))
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            cwd=folder
        )
        status.config(text="Detection started!", fg="#50fa7b")
    except Exception as error:
        messagebox.showerror("Error", str(error))

def stop_detection():
    global process

    if process is not None and process.poll() is None:
        process.terminate()
        process = None
        status.config(text="Detection stopped!", fg="#ff5555")
    else:
        status.config(text="Detection is not running!", fg="orange")

def open_history():
    folder = os.path.dirname(os.path.abspath(__file__))
    history_file = os.path.join(
        folder, "outputs", "detection_history.csv"
    )

    if os.path.exists(history_file):
        os.startfile(history_file)
    else:
        messagebox.showinfo(
            "History",
            "No detection history found. Run detection and press S first."
        )



def open_output():
    folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "outputs"
    )
    os.makedirs(folder, exist_ok=True)
    os.startfile(folder)

def close_app():
    if process is not None and process.poll() is None:
        process.terminate()
    root.destroy()

start_button = tk.Button(
    root,
    text="START DETECTION",
    command=start_detection,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    width=22,
    pady=10
)
start_button.pack(pady=8)

stop_button = tk.Button(
    root,
    text="STOP DETECTION",
    command=stop_detection,
    font=("Arial", 12, "bold"),
    bg="#ea580c",
    fg="white",
    width=22,
    pady=10
)
stop_button.pack(pady=8)

output_button = tk.Button(
    root,
    text="OPEN OUTPUT FOLDER",
    command=open_output,
    font=("Arial", 11),
    bg="#374151",
    fg="white",
    width=22,
    pady=8
)
output_button.pack(pady=8)

history_button = tk.Button(
    root,
    text="VIEW DETECTION HISTORY",
    command=open_history,
    font=("Arial", 11),
    bg="#7c3aed",
    fg="white",
    width=22,
    pady=8
)
history_button.pack(pady=8)


close_button = tk.Button(
    root,
    text="EXIT",
    command=close_app,
    font=("Arial", 11),
    bg="#dc2626",
    fg="white",
    width=12,
    pady=5
)
close_button.pack(pady=8)

root.mainloop()
