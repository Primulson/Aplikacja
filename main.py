import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk

choice = 0

def choice_0():
    global choice
    choice = 0

def choice_1():
    global choice
    choice = 1

def choice_2():
    global choice
    choice = 2

def choice_3():
    global choice
    choice = 3

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root2 = tk.Tk()

root.title("Wideo")
root2.title("Wybór")

root2.geometry('500x500')

btn1 = tk.Button(root2, text='Default',
                 width = 20,
                 height = 10,
             command=choice_0)
btn2 = tk.Button(root2, text='Grayscale',
                width = 20,
                 height = 10,
             command=choice_1)
btn3 = tk.Button(root2, text='Darker',
                 width = 20,
                 height = 10,
             command=choice_2)
btn4 = tk.Button(root2, text='Brighter',
                 width = 20,
                 height = 10,
             command=choice_3)
btn1.pack(side='top')
btn2.pack(side='left')
btn3.pack(side='right')
btn4.pack(side='bottom')


root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()



def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if choice == 0:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    if choice == 1:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if choice == 2:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        M = np.ones(cv2image.shape, dtype="uint8") * 100
        cv2image = cv2.subtract(cv2image, M)
    if choice == 3:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        M = np.ones(cv2image.shape, dtype="uint8") * 100
        cv2image = cv2.add(cv2image, M)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()
root2.mainloop()