from tkinter import *
from time import time


I_MAX, J_MAX = 800, 600
POINT_R = 3


def mandelbrot(c):
    z = c
    i = 0
    while i < iter_limit and abs(z) < 2:
        z = z**2 + c
        i += 1
    return i


def size_one(s):
    return 200 * 10**s


class Fractal():
    i0, j0 = 3 * I_MAX / 5, J_MAX / 2
    iter_limit = 100
    scale = 0
    s1 = size_one(scale)
    i_point, j_point = X / 2, Y / 2
    pointer = 0















iter_limit = 100
scale = 0



s1 = size_one(scale)
i0, j0 = 3 * I_MAX / 5, J_MAX / 2


pointer = 0

cx, cy = I_MAX / 2, J_MAX / 2

def color(n):
    tone = int(0xFFF - 0xFFF * n / iter_limit)
    return '#{:03x}{:03x}{:03x}'.format(tone, tone, tone)
#    if n==MAX_ITER:
#        return '#000'
#    else:
#        return '#fff'


def dec_x(i):
    return (i - i0) / s1


def dec_y(j):
    return (j0 - j) / s1


root = Tk()
root.title('Set of Malderbrot')
root.resizable(0, 0)
cn = Canvas(root, width=I_MAX, height=J_MAX, bg='white')
cn.pack()


img = PhotoImage(width=I_MAX, height=J_MAX)






def draw():
    t0 = time()
    cn.delete('all')
    inf = cn.create_text(I_MAX / 2, J_MAX / 2, text='', anchor='center')
    cn.update()
    img.blank()
    per = 0
    for i in range(I_MAX):
        per2 = 100 * i // I_MAX
        if per2 != per:
            per = per2
            cn.itemconfig(inf, text='Processing: {:3}%'.format(per), )
            cn.update()
        for j in range(J_MAX):
            c = complex(dec_x(i), dec_y(j))
            img.put( color(mandelbrot(c)) , to=(i, j))
    cn.create_image(0, 0, anchor=NW, image=img)
    cn.create_line(0, j0, I_MAX, j0, arrow='last')
    cn.create_line(i0, J_MAX, i0, 0, arrow='last')
    cn.delete(inf)
    print('Draw fractal {}x{} ({} iter): {:2f} c'.format(I_MAX, J_MAX, iter_limit, time() - t0))


draw()


pn = Frame(height=50)
pn.pack(fill='x')


def cn_click(event):
    i, j = event.x, event.y
    global pointer
    if pointer > 0:
        cn.delete(pointer)
    pointer = cn.create_oval(i - POINT_R, j - POINT_R, i + POINT_R, j + POINT_R, fill='yellow', outline='red', tag='p')
    print(i, j)
    global cx, cy
    cx, cy = i, j


cn.bind('<Button-1>', cn_click)

ent_scale = Entry(pn, width=8)
ent_iter = Entry(pn, width=8)

def action():
    global s1, i0, j0, iter_limit, scale
    s2 = size_one(float(ent_scale.get()))
    i0 = I_MAX / 2 - s2 * (cx - i0) / s1
    j0 = J_MAX / 2 + s2 * (j0 - cy) / s1
    s1 = s2
    iter_limit = int(ent_iter.get())
    draw()


act = Button(pn, text='Redraw', command=action)
act.pack(side='left')

Label(pn, text='  Scale:').pack(side='left')


ent_scale.pack(side='left')
ent_scale.insert(0, str(scale))

Label(pn, text='  Iter: ').pack(side='left')
ent_iter.pack(side='left')
ent_iter.insert(0, str(iter_limit))


root.mainloop()