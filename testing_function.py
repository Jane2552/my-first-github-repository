import tkinter as tk

def on_button_yes_click():
    print("即將轉跳至新畫面!")

def on_button_no_click():
    print("確定要退出嗎?")

root = tk.Tk()
button1 = tk.Button(root, text="yes", command=on_button_yes_click)
button2 = tk.Button(root, text="no", command=on_button_no_click)
button1.pack()
button2.pack()
root.mainloop()