from tkinter import *

X, Y = 800, 100

MAX = X

root = Tk()
CNV = Canvas(root, width=X, height=Y, bg='white')
CNV.pack()

but = Button(text='OK')
but.pack()

img = PhotoImage(width=X,height=Y)
im = CNV.create_image(0, 0, anchor=NW, image=img)


def rgb(r, g, b):
    return '#{:03x}{:03x}{:03x}'.format(int(0xfff*r), int(0xfff*g), int(0xfff*b))
    #return '#{:02x}{:02x}{:02x}'.format(int(0xff * r), int(0xff * g), int(0xff * b))
    #return '#{:01x}{:01x}{:01x}'.format(int(0xf * r), int(0xf * g), int(0xf * b))

def color(level):
    L = 5*level
    if L < 1:
        return rgb(L, 0, 0)
    elif L < 2:
        return rgb(2-L, L-1, 0)
    elif L < 3:
        return rgb(0, 3-L, L-2)
    elif L < 5:
        return rgb((L-3)/2, (L-3)/2, 1)
    else:
        return rgb(1, 1, 1)



for x in range(MAX):
    p = x/(MAX-1)
    img.put(color(p), to=(x, 0, x + 1, Y))


img2= PhotoImage(width=X,height=Y)
img2.put(rgb(0.5, 0.5, 0), to=(50, 0, 60, Y))

but.config(command= lambda : CNV.itemconfig(im, image=img2))


root.mainloop()