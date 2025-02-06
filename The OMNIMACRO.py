import tkinter as tk
import time
from pynput.keyboard import Key,Controller as KeyController
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController()
keyboard = KeyController()


def mmd(dx, dy):
    time.sleep(5)
    mouse.move(dx, dy)


def hold_release(dur, key):
    keyboard.press(key)
    time.sleep(dur)
    keyboard.release(key)


def efffarm(rows, times=1):  # Wart, Wheat, Carrot, Potato
    for i in range(times):
        time.sleep(5)
        mouse.press(Button.left)
        for i in range(rows):
            hold_release(13.5, "w")
            hold_release(13.5, "a")
        mouse.release(Button.left)
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(0.2)
        for i in "/warp garden":
            hold_release(0.05, i)
        keyboard.press(Key.enter)
        time.sleep(0.4)
        keyboard.release(Key.enter)


def melonfarm(rows, plots):  # Melon, Pumpkin
    keyboard.press("w")
    mouse.press(Button.left)
    for i in range(rows):
        hold_release(17*plots, "d")
        time.sleep(3)
        hold_release(17*plots, "a")
        time.sleep(2)
    mouse.release(Button.left)
    keyboard.release("t")
    keyboard.type("/warp garden")
    keyboard.press(Key.enter)
    time.sleep(0.4)
    keyboard.release(Key.enter)


def suntzucane(rows, plots):  # Cane
    mouse.press(Button.left)
    for i in range(rows):
        hold_release(10*plots, "w")
        hold_release(10*plots, "a")
    mouse.release(Button.left)
    keyboard.release("t")
    keyboard.type("/warp garden")
    keyboard.press(Key.enter)
    time.sleep(0.4)
    keyboard.release(Key.enter)


def AustinShroom(times, plots): # I haven't tested this
    time.sleep(5)
    keyboard.press(",")
    for i in range(times):
        for i in range(3):
            hold_release(98*plots/5, "a")
            hold_release(102*plots/5, "d")
    keyboard.release(",")
    keyboard.press("t")
    time.sleep(0.4)
    keyboard.release("t")
    keyboard.type("/warp garden")
    keyboard.press(Key.enter)
    time.sleep(0.4)
    keyboard.release(Key.enter)
    wawwawe


def open_new_window(window_to_hide, window_to_show):
    window_to_hide.withdraw()  # Hide the window to hide
    window_to_show.deiconify()  # Show the window to show


def getinput(inputbox, checkbox):
    global inputboxres
    global checkboxres
    user_input = inputbox.get()
    checkbox_state = checkbox.get()
    inputboxres = user_input
    checkboxres = checkbox_state

# Homepage

hypixelfarm = tk.Tk()
image = tk.PhotoImage(file="MHS.png")
image_label = tk.Label(hypixelfarm, image=image)
image_label.pack()
hypixelfarm.geometry('400x300')
hypixelfarm.title("Macros")
button = tk.Button(hypixelfarm, text="Melons", command=lambda: open_new_window(hypixelfarm, mm), width=10, height=2)
button1 = tk.Button(hypixelfarm, text="Wheat", command=lambda: open_new_window(hypixelfarm, wm), width=10, height=2)
button2 = tk.Button(hypixelfarm, text="Nether Wart", command=lambda: open_new_window(hypixelfarm, nwm), width=10, height=2)
button3 = tk.Button(hypixelfarm, text="Pumpkin", command=lambda: open_new_window(hypixelfarm, pm), width=10, height=2)
button4 = tk.Button(hypixelfarm, text="Cane", command=lambda: open_new_window(hypixelfarm, scm), width=10, height=2)
button5 = tk.Button(hypixelfarm, text="Potatoes", command=lambda: open_new_window(hypixelfarm, pom), width=10, height=2)
label = tk.Label(hypixelfarm, text="Select the crop you wish to Macro")
label.pack(side="top")
button5.place(x=275,y=120)
button4.place(x=0, y=120)
button3.place(x=0, y=20)
button2.place(x=0, y=70)
button1.place(x=275, y=20)
button.place(x=275, y=70)

# Wheat Macr0
wm = tk.Toplevel(hypixelfarm)
wm.geometry('400x300')
wm.title("Wheat macros")
image_wm = tk.PhotoImage(file="WheatScreen.png")
image_wm_label = tk.Label(wm, image=image_wm)
label = tk.Label(wm, text="What Farm Schematic do you use?")
label.pack()
wm.withdraw()
rb = tk.Button(wm, text="Back to main", command=lambda: open_new_window(wm, hypixelfarm))
rb.pack()
image_wm_label.place(x=-2,y=-2)

# Potato Macros
pom = tk.Toplevel(hypixelfarm)
pom.geometry('400x300')
pom.title("Cane Macros")
image_pom = tk.PhotoImage(file="PotatoScreen.png")
image_pom_label = tk.Label(pom, image=image_pom)
label_pom = tk.Label(pom, text="What farm schematic do you use?")
label_pom.pack()
pom.withdraw()
pom_rb = tk.Button(pom, text="Back to main", command=lambda: open_new_window(pom, hypixelfarm))
pom_rb.pack()
cane_fs1_button = tk.Button(pom, text="Drai's Potato Farm", command=lambda: open_new_window(pom, draiPotato))
cane_fs1_button.pack()
image_pom_label.place(x=-2,y=-2)

# Nether Wart Macro
nwm = tk.Toplevel(hypixelfarm)
nwm.geometry('400x300')
nwm.title("Nether Wart Macros")
image3 = tk.PhotoImage(file="WartScreen.png")
image3_label = tk.Label(nwm, image=image3)
label2 = tk.Label(nwm, text="What farm schematic do you use?")
label2.pack()
nwm.withdraw()
rb1 = tk.Button(nwm, text="Back to main", command=lambda: open_new_window(nwm, hypixelfarm))
rb1.pack()
nethwart_fs1_button = tk.Button(nwm, text="Protwins827's Nether Wart Farm", command=lambda: open_new_window(nwm, p827wart))
nethwart_fs1_button.pack()
image3_label.place(x=-2,y=-2)

# Cane Macro
scm = tk.Toplevel(hypixelfarm)
scm.geometry('400x300')
scm.title("Cane Macros")
image_scm = tk.PhotoImage(file="CaneScreen.png")
image_scm_label = tk.Label(scm, image=image_scm)
label_scm = tk.Label(scm, text="What farm schematic do you use?")
label_scm.pack()
scm.withdraw()
scm_rb = tk.Button(scm, text="Back to main", command=lambda: open_new_window(scm, hypixelfarm))
scm_rb.pack()
cane_fs1_button = tk.Button(scm, text="SunTzu Cane Farm", command=lambda: open_new_window(scm, STCane))
cane_fs1_button.pack()
image_scm_label.place(x=-2,y=-2)

# Pumpkin Macro
pm = tk.Toplevel(hypixelfarm)
pm.geometry('400x300')
pm.title("Pumpkin Macros")
image2 = tk.PhotoImage(file="PumpkinScreen.png")
image2_label = tk.Label(pm, image=image2, text="What Farm Schematic do you use?")
label3 = tk.Label(pm, text="What Farm Schematic do you use?")
pumpkin_fs1_button = tk.Button(pm, text="SunTzu's Black Cat Farm", command=lambda: open_new_window(pm, STpumpkin))
label3.pack()
pm.withdraw()
rb2 = tk.Button(pm, text="Back to main", command=lambda: open_new_window(pm, hypixelfarm))
rb2.pack()
pumpkin_fs1_button.pack()
image2_label.place(x=-2, y=-2)

# Melon Macro
mm = tk.Toplevel(hypixelfarm)
mm.geometry('400x300')
mm.title("Green Pumpkin Macros")
image1 = tk.PhotoImage(file="MelonScreen.png")
image1_label = tk.Label(mm, image=image1)
label4 = tk.Label(mm, text="What Farm Schematic do you use?")
label4.pack()
mm.withdraw()
melon_fs1_button = tk.Button(mm, text="MelonKingDe's Melon Farm", command=lambda: open_new_window(mm, melonkingdemelons))
rb3 = tk.Button(mm, text="Back to main", command=lambda: open_new_window(mm, hypixelfarm))
rb3.pack()
melon_fs1_button.pack()
image1_label.place(x=-2, y=-2)

# MelonKingDe's Melon Farm
melonkingdemelons = tk.Toplevel(hypixelfarm)
melonkingdemelons.geometry('400x300')
melonkingdemelons.title("MelonKingDe's Farm")
melonkingdemelons_label = tk.Label(melonkingdemelons, text="How wide is your 1 plot thick farm")
melonkingdemelons_label.pack()
melonkingdemelons_plots_1 = tk.Button(melonkingdemelons, text="1 Plot", command=lambda: melonfarm(10, 1))
melonkingdemelons_plots_2 = tk.Button(melonkingdemelons, text="2 Plots", command=lambda: melonfarm(10, 2))
melonkingdemelons_plots_3 = tk.Button(melonkingdemelons, text="3 Plots", command=lambda: melonfarm(10, 3))
melonkingdemelons_plots_4 = tk.Button(melonkingdemelons, text="4 Plots", command=lambda: melonfarm(10, 4))
melonkingdemelons_plots_5 = tk.Button(melonkingdemelons, text="5 Plots", command=lambda: melonfarm(10, 5))
melonkingdemelons_plots_1.pack()
melonkingdemelons_plots_2.pack()
melonkingdemelons_plots_3.pack()
melonkingdemelons_plots_4.pack()
melonkingdemelons_plots_5.pack()
melonkingdemelons.withdraw()
melonkingdemelons_button_back = tk.Button(melonkingdemelons, text="Back to Melons", command=lambda:
open_new_window(melonkingdemelons, mm))
melonkingdemelons_button_back.pack()
melonkingdemelons_button_home = tk.Button(melonkingdemelons, text="Back to Home", command=lambda:
open_new_window(melonkingdemelons, hypixelfarm))
melonkingdemelons_button_home.pack()

# Protwins827's Wart Farm
p827wart = tk.Toplevel(hypixelfarm)
p827wart.geometry('400x300')
p827wart.title("Protwins827's Farm")
p827wart_label = tk.Label(p827wart, text="How many plots does your farm have?")
p827wart_label.pack()
p827wart_plots_1 = tk.Button(p827wart, text="1 Plot", command=lambda: efffarm(10))
p827wart_plots_2 = tk.Button(p827wart, text="2 Plots", command=lambda: efffarm(21, 3))
p827wart_plots_3 = tk.Button(p827wart, text="3 Plots", command=lambda: efffarm(32))
p827wart_plots_4 = tk.Button(p827wart, text="4 Plots", command=lambda: efffarm(42))
p827wart_plots_5 = tk.Button(p827wart, text="5 Plots", command=lambda: efffarm(52))
p827wart_plots_1.pack()
p827wart_plots_2.pack()
p827wart_plots_3.pack()
p827wart_plots_4.pack()
p827wart_plots_5.pack()
p827wart.withdraw()
p827wart_button_back = tk.Button(p827wart, text="Back to Wart", command=lambda:
open_new_window(p827wart, nwm))
p827wart_button_back.pack()
p827wart_button_home = tk.Button(p827wart, text="Back to Home", command=lambda:
open_new_window(p827wart, hypixelfarm))
p827wart_button_home.pack()

#MelonKingDePumpkin
STpumpkin = tk.Toplevel(hypixelfarm)
STpumpkin.geometry('400x300')
STpumpkin.title("SunTzu's Farm")
STpumpkin_label = tk.Label(STpumpkin, text="How wide is your 1 plot thick farm? ")
STpumpkin_label.pack()
STpumpkin_plots_1 = tk.Button(STpumpkin, text="1 Plot", command=lambda: melonfarm(10, 1))
STpumpkin_plots_2 = tk.Button(STpumpkin, text="2 Plots", command=lambda: melonfarm(10, 2))
STpumpkin_plots_3 = tk.Button(STpumpkin, text="3 Plots", command=lambda: melonfarm(10, 3))
STpumpkin_plots_4 = tk.Button(STpumpkin, text="4 Plots", command=lambda: melonfarm(10, 4))
STpumpkin_plots_5 = tk.Button(STpumpkin, text="5 Plots", command=lambda: melonfarm(10, 5))
STpumpkin_plots_1.pack()
STpumpkin_plots_2.pack()
STpumpkin_plots_3.pack()
STpumpkin_plots_4.pack()
STpumpkin_plots_5.pack()
STpumpkin.withdraw()
STpumpkin_button_back = tk.Button(STpumpkin, text="Back to Pumpkin", command=lambda:
open_new_window(STpumpkin, pm))
STpumpkin_button_back.pack()
STpumpkin_button_home = tk.Button(STpumpkin, text="Back to Home", command=lambda:
open_new_window(STpumpkin, hypixelfarm))
STpumpkin_button_home.pack()

#Clo's Cane Farm

STCane = tk.Toplevel(hypixelfarm)
STCane.geometry('400x300')
STCane.title("Clo's Farm")
STCane_label = tk.Label(STCane, text="How wide is your 1 plot thick farm")
STCane_label.pack()
STCane_plots_1 = tk.Button(STCane, text="1 Plot", command=lambda: suntzucane(14, 1))
STCane_plots_2 = tk.Button(STCane, text="2 Plots", command=lambda: suntzucane(14, 2))
STCane_plots_3 = tk.Button(STCane, text="3 Plots", command=lambda: suntzucane(14, 3))
STCane_plots_4 = tk.Button(STCane, text="4 Plots", command=lambda: suntzucane(14, 4))
STCane_plots_5 = tk.Button(STCane, text="5 Plots", command=lambda: suntzucane(14, 5))
STCane_plots_1.pack()
STCane_plots_2.pack()
STCane_plots_3.pack()
STCane_plots_4.pack()
STCane_plots_5.pack()
STCane.withdraw()
STCane_button_back = tk.Button(STCane, text="Back to Cane", command=lambda:
open_new_window(STCane, scm))
STCane_button_back.pack()
STCane_button_home = tk.Button(STCane, text="Back to Home", command=lambda:
open_new_window(STCane, hypixelfarm))
STCane_button_home.pack()

# Drai's Potato Farm

draiPotato = tk.Toplevel(hypixelfarm)
draiPotato.geometry('400x300')
draiPotato.title("MelonKingDe's Farm")
draiPotato_label = tk.Label(draiPotato, text="How many plots thick is your 1 plot wide farm?")
draiPotato_label.pack()
draiPotato_plots_1 = tk.Button(draiPotato, text="1 Plot", command=lambda: efffarm(10))
draiPotato_plots_2 = tk.Button(draiPotato, text="2 Plots", command=lambda: efffarm(21))
draiPotato_plots_3 = tk.Button(draiPotato, text="3 Plots", command=lambda: efffarm(32))
draiPotato_plots_4 = tk.Button(draiPotato, text="4 Plots", command=lambda: efffarm(43))
draiPotato_plots_5 = tk.Button(draiPotato, text="5 Plots", command=lambda: efffarm(54))
draiPotato_plots_1.pack()
draiPotato_plots_2.pack()
draiPotato_plots_3.pack()
draiPotato_plots_4.pack()
draiPotato_plots_5.pack()
draiPotato.withdraw()
draiPotato_button_back = tk.Button(draiPotato, text="Back to Potato", command=lambda:
open_new_window(draiPotato, pom))
draiPotato_button_back.pack()
draiPotato_button_home = tk.Button(draiPotato, text="Back to Home", command=lambda:
open_new_window(draiPotato, hypixelfarm))
draiPotato_button_home.pack()

# Start the Tkinter event loop
hypixelfarm.mainloop()
