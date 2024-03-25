import tkinter as tk
from tkinter import messagebox
import threading
import time

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("200x150")
        self.master.attributes("-topmost", 1)

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:20:00")
        
        self.label = tk.Label(master, textvariable=self.time_left_var, font=("Arial", 24))
        self.label.pack(pady=10)

        self.ten_min_button = tk.Button(master, text="10 Minutes", command=lambda: self.start_countdown(10))
        self.ten_min_button.pack(fill=tk.X, expand=True)

        self.twenty_min_button = tk.Button(master, text="20 Minutes", command=lambda: self.start_countdown(20))
        self.twenty_min_button.pack(fill=tk.X, expand=True)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(fill=tk.X, expand=True)

        self.running = False
        self.thread = None

    def reset(self):
        if self.thread and self.running:
            self.running = False
            self.thread.join()
        self.time_left_var.set("00:00:00")
        self.label.config(bg="SystemButtonFace")

    def start_countdown(self, minutes):
        self.reset()
        self.running = True
        self.thread = threading.Thread(target=self.countdown, args=(minutes * 60,))
        self.thread.start()

    def countdown(self, time_left):
        while time_left >= 0 and self.running:
            mins, secs = divmod(time_left, 60)
            hours, mins = divmod(mins, 60)
            time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            self.update_time_left(time_format)
            time.sleep(1)
            time_left -= 1
        if self.running:
            self.running = False
            self.flash_colors()

    def update_time_left(self, time_str):
        if self.running:
            self.time_left_var.set(time_str)

    def flash_colors(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        for color in colors:
            if self.running:
                self.label.config(bg=color)
                self.master.update()
                time.sleep(0.5)

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
