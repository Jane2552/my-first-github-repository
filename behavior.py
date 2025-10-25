import csv
import os
import tkinter as tk

def yes_button():
    print("是")
def no_button():
    print("否")

window = tk.Tk()
button1 = tk.Button(window, text="是", command=yes_button)
button2 = tk.Button(window, text="否", command=no_button)
button1.pack()
button2.pack()
window.mainloop()