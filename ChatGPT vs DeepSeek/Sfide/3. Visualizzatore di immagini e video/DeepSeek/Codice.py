import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os

class MediaViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E3440")

        self.media_label = tk.Label(root, bg="#2E3440")
        self.media_label.pack(expand=True, fill=tk.BOTH)

        self.controls_frame = tk.Frame(root, bg="#2E3440")
        self.controls_frame.pack(fill=tk.X)

        self.open_button = tk.Button(self.controls_frame, text="Apri File", command=self.open_file, bg="#4C566A", fg="#D8DEE9")
        self.open_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.close_button = tk.Button(self.controls_frame, text="Chiudi", command=self.close_media, bg="#4C566A", fg="#D8DEE9")
        self.close_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.zoom_in_button = tk.Button(self.controls_frame, text="Zoom +", command=self.zoom_in, bg="#4C566A", fg="#D8DEE9")
        self.zoom_out_button = tk.Button(self.controls_frame, text="Zoom -", command=self.zoom_out, bg="#4C566A", fg="#D8DEE9")

        self.play_pause_button = tk.Button(self.controls_frame, text="Play/Pausa", command=self.play_pause, bg="#4C566A", fg="#D8DEE9")
        self.volume_scale = tk.Scale(self.controls_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, bg="#4C566A", fg="#D8DEE9")
        self.speed_scale = tk.Scale(self.controls_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_speed, bg="#4C566A", fg="#D8DEE9")

        self.current_media = None
        self.zoom_level = 1.0
        self.video_paused = False
        self.video_capture = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Immagini", "*.jpg *.jpeg *.png"), ("Video", "*.mp4 *.avi")])
        if file_path:
            self.close_media()
            if file_path.lower().endswith((".jpg", ".jpeg", ".png")):
                self.show_image(file_path)
            elif file_path.lower().endswith((".mp4", ".avi")):
                self.show_video(file_path)

    def show_image(self, file_path):
        self.current_media = "image"
        self.image = Image.open(file_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.media_label.config(image=self.tk_image)

        self.zoom_in_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.zoom_out_button.pack(side=tk.LEFT, padx=10, pady=10)

    def show_video(self, file_path):
        self.current_media = "video"
        self.video_capture = cv2.VideoCapture(file_path)
        self.video_paused = False

        self.play_pause_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.volume_scale.pack(side=tk.LEFT, padx=10, pady=10)
        self.speed_scale.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_video()

    def update_video(self):
        if not self.video_paused:
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (800, 600))
                self.tk_frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.media_label.config(image=self.tk_frame)
            self.root.after(25, self.update_video)

    def play_pause(self):
        self.video_paused = not self.video_paused
        if not self.video_paused:
            self.update_video()

    def set_volume(self, volume):
        # Implementa la regolazione del volume qui
        pass

    def set_speed(self, speed):
        self.video_capture.set(cv2.CAP_PROP_FPS, float(speed) * self.video_capture.get(cv2.CAP_PROP_FPS))

    def zoom_in(self):
        self.zoom_level *= 1.1
        self.resize_image()

    def zoom_out(self):
        self.zoom_level /= 1.1
        self.resize_image()

    def resize_image(self):
        if self.current_media == "image":
            width, height = self.image.size
            new_size = (int(width * self.zoom_level), (int(height * self.zoom_level))
            resized_image = self.image.resize(new_size, Image.ANTIALIAS)
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.media_label.config(image=self.tk_image)

    def close_media(self):
        if self.current_media == "video" and self.video_capture:
            self.video_capture.release()
        self.media_label.config(image="")
        self.zoom_in_button.pack_forget()
        self.zoom_out_button.pack_forget()
        self.play_pause_button.pack_forget()
        self.volume_scale.pack_forget()
        self.speed_scale.pack_forget()
        self.current_media = None
        self.zoom_level = 1.0

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaViewer(root)
    root.mainloop()
