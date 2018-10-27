from tkinter import *
from time import time
"Commit from Ubuntu"

X, Y = 800, 600
MAX_ITER = 100
BASE_SIZE = X/4
scale = 0

def size1(s):
    return BASE_SIZE*10**(s)

s1 = size1(scale)


px0, py0 = 3 * X / 5, Y / 2

point_r = 3
pointer = 0

cx, cy = X/2, Y/2

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
#    if n==MAX_ITER:
#        return '#000'
#    else:
#        return '#fff'


def dec_x(i):
    return (i - px0) / s1


def dec_y(j):
    return (py0 - j) / s1


root = Tk()
root.title('Set of Malderbrot')
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
    cn.create_line(0, py0, X, py0, arrow='last')
    cn.create_line(px0, Y, px0, 0, arrow='last')
    cn.delete(inf)
    print('Draw fractal {}x{} ({} iter): {:2f} c'.format(X, Y, MAX_ITER, time() - t0))


draw()


pn = Frame(height=50)
pn.pack(fill='x')


def cn_clisk(event):
    i, j = event.x, event.y
    global pointer
    if (pointer > 0):
        cn.delete(pointer)
    pointer = cn.create_oval(i-point_r, j-point_r, i+point_r, j+point_r, fill='yellow', outline='red', tag='p')
    print(i, j)
    global cx, cy
    cx, cy = i, j


cn.bind('<Button-1>', cn_clisk)

ent_scale = Entry(pn, width=8)
ent_iter = Entry(pn, width=8)

def action():
    global s1, px0, py0, MAX_ITER, scale, cx, cy
    s2 = size1(float(ent_scale.get()))
    px0 = X/2 - s2*(cx - px0)/s1
    py0 = Y/2 + s2*(py0 - cy)/s1
    s1 = s2
    MAX_ITER = int(ent_iter.get())
    cx, cy = X/2, Y/2
    draw()


act = Button(pn, text='Redraw', command=action)
act.pack(side='left')

Label(pn, text='  Scale:').pack(side='left')


ent_scale.pack(side='left')
ent_scale.insert(0, str(scale))

Label(pn, text='  Iter: ').pack(side='left')
ent_iter.pack(side='left')
ent_iter.insert(0, str(MAX_ITER))


root.mainloop()