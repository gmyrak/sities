import random
from tkinter import *

X, Y = 400, 300

root = Tk()

img = Canvas(bg='white', width=X, height=Y)
img.pack(fill='both', expand=1)

def pix(x,y):
    img.create_oval(x,y,x,y)


for x in range(X):
    for y in range(Y):
        pix(x,y)

print()

root.mainloop()