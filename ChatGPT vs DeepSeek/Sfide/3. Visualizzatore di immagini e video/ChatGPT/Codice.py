import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import cv2
from ttkthemes import ThemedTk
import os
import threading

# Install required libraries using the command:
# pip install pillow opencv-python ttkthemes

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"),
            ("Video Files", "*.mp4;*.avi;*.mov;*.mkv"),
        ]
    )
    if file_path:
        extension = os.path.splitext(file_path)[1].lower()
        if extension in [".png", ".jpg", ".jpeg", ".bmp"]:
            show_image(file_path)
        elif extension in [".mp4", ".avi", ".mov", ".mkv"]:
            show_video(file_path)

def show_image(file_path):
    def zoom_image(scale):
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        resized_image = img.resize((new_width, new_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_image)
        image_label.config(image=photo)
        image_label.photo = photo

    image_window = tk.Toplevel(root)
    image_window.title("Image Viewer")

    img = Image.open(file_path)
    original_width, original_height = img.size
    photo = ImageTk.PhotoImage(img)

    image_label = ttk.Label(image_window, image=photo)
    image_label.photo = photo
    image_label.pack()

    zoom_slider = ttk.Scale(image_window, from_=0.5, to=2.0, resolution=0.1, command=lambda value: zoom_image(float(value)))
    zoom_slider.set(1.0)
    zoom_slider.pack()

    ttk.Button(image_window, text="Close", command=image_window.destroy).pack(pady=5)

def show_video(file_path):
    def update_frame():
        nonlocal playing
        while playing:
            ret, frame = video.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (video_label.winfo_width(), video_label.winfo_height()))
            frame_img = ImageTk.PhotoImage(image=Image.fromarray(frame))

            video_label.config(image=frame_img)
            video_label.image = frame_img

            cv2.waitKey(int(1000 / playback_speed))

    def play_pause():
        nonlocal playing
        playing = not playing
        if playing:
            play_button.config(text="Pause")
            threading.Thread(target=update_frame, daemon=True).start()
        else:
            play_button.config(text="Play")

    def adjust_volume(value):
        video.set(cv2.CAP_PROP_VOLUME, float(value))

    def adjust_speed(value):
        nonlocal playback_speed
        playback_speed = float(value)

    def close_video():
        nonlocal playing
        playing = False
        video.release()
        video_window.destroy()

    video_window = tk.Toplevel(root)
    video_window.title("Video Viewer")

    video_label = ttk.Label(video_window)
    video_label.pack(fill=tk.BOTH, expand=True)

    video = cv2.VideoCapture(file_path)
    playing = True
    playback_speed = 1.0

    controls_frame = ttk.Frame(video_window)
    controls_frame.pack(fill=tk.X, pady=5)

    play_button = ttk.Button(controls_frame, text="Pause", command=play_pause)
    play_button.pack(side=tk.LEFT, padx=5)

    volume_label = ttk.Label(controls_frame, text="Volume:")
    volume_label.pack(side=tk.LEFT)
    volume_slider = ttk.Scale(controls_frame, from_=0.0, to=1.0, command=adjust_volume)
    volume_slider.set(0.5)
    volume_slider.pack(side=tk.LEFT, padx=5)

    speed_label = ttk.Label(controls_frame, text="Speed:")
    speed_label.pack(side=tk.LEFT)
    speed_slider = ttk.Scale(controls_frame, from_=0.5, to=2.0, resolution=0.1, command=adjust_speed)
    speed_slider.set(1.0)
    speed_slider.pack(side=tk.LEFT, padx=5)

    ttk.Button(controls_frame, text="Close", command=close_video).pack(side=tk.RIGHT, padx=5)

    threading.Thread(target=update_frame, daemon=True).start()

root = ThemedTk(theme="arc")
root.title("Media Viewer")
root.geometry("500x300")

welcome_label = ttk.Label(root, text="Welcome to Media Viewer", font=("Arial", 16))
welcome_label.pack(pady=20)

open_button = ttk.Button(root, text="Open File", command=select_file)
open_button.pack(pady=10)

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
