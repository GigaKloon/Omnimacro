import tkinter as tk
import time
from pynput.keyboard import Key,Controller as KeyController
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController()
keyboard = KeyController()


def open_new_window(window_to_hide, window_to_show):
    window_to_hide.withdraw()  # Hide the window to hide
    window_to_show.deiconify()  # Show the window to show


homepage = tk.Tk()
hp_dm = tk.Button(homepage, text="Dive Mine", command=lambda: open_new_window(homepage, divemine))
hp_dm.pack()


divemine = tk.Toplevel(homepage)
divemine_hp = tk.Button(divemine, text="Back", command=lambda: open_new_window(divemine, homepage))
divemine_hp.pack()


homepage.mainloop()


