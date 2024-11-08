import tkinter as tk

import time
def run_spurt():
    #25 minutes
    minutes = 2
    seconds = minutes * 60
    mins, secs = divmod(seconds, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    if seconds > 0:
        root.after(1000, run_spurt, seconds - 1)
    else:
        timer_label.config(text="Time's up!")
        tk.Button(root, text="Study Time!", command=lambda: run_break()).pack()
    
def run_break():
    #5 minutes
    minutes = 1
    seconds = minutes * 60
    mins, secs = divmod(seconds, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    if seconds > 0:
        root.after(1000, run_spurt, seconds - 1)
    else:
        timer_label.config(text="Time's up!")
        tk.Button(root, text="Study Time!", command=lambda: run_spurt()).pack()


def run():
    pass

root = tk.Tk()
root.title("Timer")

timer_label = tk.Label(root, font=("Helvetica", 48))
timer_label.pack()

tk.Button(root, text="Study", command=lambda: run_spurt()).pack()



root.mainloop()