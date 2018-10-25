from tkinter import *
from time import time

X, Y = 800, 600

X0, Y0 = 3*X/5, Y/2
s1 = 400

MAX_ITER = 60

point_r = 3
pointer = 0


def mandelbrot(c):
    z = c
    i = 0
    while i < MAX_ITER and abs(z) < 2:
        z = z**2 + c
        i += 1
    return i


def color(n):
    tone = int(0xFFF - 0xFFF * n/MAX_ITER)
    return '#{:03x}{:03x}{:03x}'.format(tone, tone, tone)


def dec_x(i):
    return (i-X0)/s1


def dec_y(j):
    return (Y0-j)/s1


root = Tk()
root.resizable(0, 0)
cn = Canvas(root, width=X, height=Y, bg='white')
cn.pack()


img = PhotoImage(width=X,height=Y)



def draw():
    t0 = time()
    cn.delete('all')
    inf = cn.create_text(X / 2, Y / 2, text='', anchor='center')
    cn.update()
    img.blank()
    per = 0
    for i in range(X):
        per2 = 100*i//X
        if per2 != per:
            per = per2
            cn.itemconfig(inf, text='Processing: {:3}%'.format(per), )
            cn.update()
        for j in range(Y):
            c = complex(dec_x(i), dec_y(j))
            img.put( color(mandelbrot(c)) , to=(i, j))
    cn.create_image(0, 0, anchor=NW, image=img)
    cn.create_line(0, Y0, X, Y0, arrow='last')
    cn.create_line(X0, Y, X0, 0, arrow='last')
    cn.delete(inf)
    print('Draw fractal {}x{} ({} iter): {:2f} c'.format(X, Y, MAX_ITER, time() - t0))


draw()


pn = Frame(height=50)
pn.pack(fill='x')


def cn_clisk(event):
    x, y = event.x, event.y
    global pointer
    if (pointer > 0):
        cn.delete(pointer)
    pointer = cn.create_oval(x-point_r, y-point_r, x+point_r, y+point_r, fill='yellow', outline='red', tag='p')
    print(event.x, event.y)


cn.bind('<Button-1>', cn_clisk)


def action():
    draw()


act = Button(pn, text='Redraw', command=action)
act.pack(side='left')

root.mainloop()