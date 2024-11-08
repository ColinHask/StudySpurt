import tkinter as tk
import time

# use pyqt5

def start_timer(minutes):
    seconds = minutes * 60
    countdown(seconds)

def countdown(count):
    mins, secs = divmod(count, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        
        timer_label.config(text="Time's up!")

root = tk.Tk()
root.title("Timer")

timer_label = tk.Label(root, font=("Helvetica", 48))
timer_label.pack()

tk.Button(root, text="Study", command=lambda: start_timer(1)).pack()
time.sleep(10)


root.mainloop()