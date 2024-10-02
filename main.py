import tkinter as tk

root = tk.Tk()
root.title("StudySpurt")

# Create a label
label = tk.Label(root, text="hello world")

# Place the label at specific coordinates
label.place(x=5, y=5)

root.mainloop()