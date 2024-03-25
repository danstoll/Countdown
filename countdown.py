import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import time
import tempfile
import os
from timer_app_icon import icon_data  # Import the icon byte array

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.resizable(True, True)

        # Set default window size: Width x Height
        self.master.geometry("200x180")  # Example: 400 pixels wide by 300 pixels tall

        # Convert the icon data list to a bytes object and handle the icon
        icon_bytes = bytes(icon_data)  # Ensure icon_data is correctly formatted
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ico') as tmp:
            tmp.write(icon_bytes)  # Write bytes to the temp file
            self.master.iconbitmap(tmp.name)
            self.icon_temp_file = tmp.name  # Save the temp file name for cleanup

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:20:00")
        
        self.label = tk.Label(master, textvariable=self.time_left_var, font=("Arial", 24))
        self.label.pack(pady=10)

        self.config_button = tk.Button(master, text="Config", command=self.configure_times)
        self.config_button.pack(fill=tk.X, expand=True)

        self.custom_times = {"10": 10, "20": 20}  # Default times

        self.ten_min_button = tk.Button(master, text="10 Minutes", command=lambda: self.start_countdown(self.custom_times.get("10", 10) * 60))
        self.ten_min_button.pack(fill=tk.X, expand=True)

        self.twenty_min_button = tk.Button(master, text="20 Minutes", command=lambda: self.start_countdown(self.custom_times.get("20", 20) * 60))
        self.twenty_min_button.pack(fill=tk.X, expand=True)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(fill=tk.X, expand=True)

        self.running = False
        self.thread = None

    def configure_times(self):
        ten_min = simpledialog.askinteger("Configure", "Set custom time for 10 Min button (in minutes):", initialvalue=self.custom_times["10"])
        if ten_min is not None: self.custom_times["10"] = ten_min
        twenty_min = simpledialog.askinteger("Configure", "Set custom time for 20 Min button (in minutes):", initialvalue=self.custom_times["20"])
        if twenty_min is not None: self.custom_times["20"] = twenty_min

    def reset(self):
        if self.thread and self.running:
            self.running = False
            self.thread.join()
        self.time_left_var.set("00:00:00")
        self.label.config(bg="SystemButtonFace", fg="black")

    def start_countdown(self, seconds):
        self.reset()
        self.running = True
        self.thread = threading.Thread(target=self.countdown, args=(seconds,))
        self.thread.start()

    def countdown(self, time_left):
        while time_left > 0 and self.running:
            mins, secs = divmod(time_left, 60)
            hours, mins = divmod(mins, 60)
            time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            self.update_time_left(time_format)
            time.sleep(1)
            time_left -= 1
        if self.running:
            self.running = False
            self.flash_colors()
            self.blink_timer()

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

    def blink_timer(self):
        for _ in range(10):
            self.label.config(fg="red")
            self.master.update()
            time.sleep(0.5)
            self.label.config(fg="black")
            self.master.update()
            time.sleep(0.5)

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
    # Cleanup the temporary icon file after the application closes
    if app.icon_temp_file:
        os.unlink(app.icon_temp_file)

if __name__ == "__main__":
    main()