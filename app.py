from tkinter import *
import math
import os
import sys

root = Tk()
clicks = 0
cost = 1
acost = 10
level = 1
autolevel = 1
timeplayed = 0
root.title("Cursor Clicker")
root.geometry("720x480")
root.config(bg="#FFF5FF")


def counter():
    global clicks
    for i in range(0, level):
        clicks += 1 + autolevel
    score.config(text="Score: " + str(clicks))


def upgrade():
    global level
    global clicks
    global cost
    if clicks >= cost:
        level += 1
        clicks -= cost
    score.config(text="Score: " + str(clicks))
    levelLabel.config(text="Upgrade: " + str(level))
    cost = int(math.exp(level))
    costLabel.config(text="Cost: " + str(cost))


def auto():
    global autolevel
    global clicks
    for i in range(0, autolevel):
        clicks += 1
    score.config(text="Score: " + str(clicks))
    root.after(1000, auto)


def autoupgrade():
    global autolevel
    global clicks
    global acost
    if clicks >= acost:
        autolevel += 1
        clicks -= acost
    score.config(text="Score: " + str(clicks))
    autoCostLabel.config(text="Auto Cost: " + str(acost))
    acost = int(math.exp(autolevel))
    clickerlevelLabel.config(text="Auto Upgrade: " + str(autolevel))


def timer():
    global timeplayed
    timeplayed += 1
    timeLabel.config(text="Time: " + str(timeplayed) + "s")
    root.after(1000, timer)


clickingButton = Button(root, text="Click Me!",
                        bg="#FFDFCA", padx=25, pady=10, command=counter, width=20)
clickingButton.pack()
clickingButton.place(relx=0.5, rely=0.3, anchor=CENTER)

score = Label(root, text="Score: 0", font=(
    "Helvetica", 16), padx=25, bg="#FFF5FF")
score.pack()
score.place(relx=0.5, rely=0.1, anchor=CENTER)

upgradeButton = Button(root, text="Upgrade", bg="#FFDFCA",
                       padx=25, pady=10, command=upgrade, width=20)
upgradeButton.pack()
upgradeButton.place(relx=0.2, rely=0.3, anchor=CENTER)

levelLabel = Label(root, text="Upgrade: 1", font=(
    "Helvetica", 16), padx=25, pady=10, bg="#FFF5FF")
levelLabel.pack()
levelLabel.place(relx=0.2, rely=0.1, anchor=CENTER)

costLabel = Label(root, text="Cost: 2", font=(
    "Helvetica", 16), padx=25, pady=10, bg="#FFF5FF")
costLabel.pack()
costLabel.place(relx=0.2, rely=0.2, anchor=CENTER)

clickerlevelLabel = Label(root, text="Auto Upgrade: 1", font=(
    "Helvetica", 16), padx=25, pady=10, bg="#FFF5FF")
clickerlevelLabel.pack()
clickerlevelLabel.place(relx=0.8, rely=0.1, anchor=CENTER)

autoCostLabel = Label(root, text="Auto Cost: 10", font=(
    "Helvetica", 16), padx=25, pady=10, bg="#FFF5FF")
autoCostLabel.pack()
autoCostLabel.place(relx=0.8, rely=0.2, anchor=CENTER)

autoClicker = Button(root, text="Auto Clicker Upgrade", bg="#FFDFCA",
                     padx=25, pady=10, command=autoupgrade, width=20)
autoClicker.pack()
autoClicker.place(relx=0.8, rely=0.3, anchor=CENTER)

timeLabel = Label(root, text="Time played: 0s", font=(
    "Helvetica", 16), padx=25, pady=10, bg="#FFF5FF")
timeLabel.pack()
timeLabel.place(relx=0.5, rely=0.2, anchor=CENTER)

about = Label(root, bg="#FFF5FF", font=(
    "Helvetica", 10), text="This is a simple clicker game made by me (Igor Lubura) in Python 3.10.4\nThis game is not affiliated with any other company or organization.\nThis game is free to use and modify.\nYou can message me on discord: igor papa |||#4500")
about.pack()
about.place(relx=0.5, rely=0.8, anchor=CENTER)

auto()
timer()
root.update_idletasks()
root.mainloop()
