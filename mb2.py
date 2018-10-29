from tkinter import *
from tkinter import filedialog as fd
from time import time
import re


X, Y = 1024, 768
MAX_ITER = 80
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


def rgb(r, g, b):
    return '#{:03x}{:03x}{:03x}'.format(int(0xfff*r), int(0xfff*g), int(0xfff*b))


def color_pal(level):
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


def color_gray(level):
    return rgb(level, level, level)


def color_black(level):
    if level > 0:
        return rgb(1, 1, 1)
    else:
        return rgb(0, 0, 0)


#color = color_gray


def dec_x(i):
    return (i - px0) / s1


def dec_y(j):
    return (py0 - j) / s1


root = Tk()
root.title('Set of Malderbrot')
root.resizable(0, 0)
cn = Canvas(root, width=X, height=Y, bg='white')
cn.pack()



pinfo = Frame(root, bg='white', height=20, relief='raise')
info= Label(pinfo, bg='white')


img = PhotoImage(width=X,height=Y)



def draw():
    if rb_state.get() == 1:
        color = color_black
    elif rb_state.get() == 2:
        color = color_gray
    else:
        color = color_pal

    info['text'] = 'Calculate...'
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
            img.put( color(1 - mandelbrot(c)/MAX_ITER) , to=(i, j))
    cn.create_image(0, 0, anchor=NW, image=img)
    cn.create_line(0, py0, X, py0, arrow='last')
    cn.create_line(px0, Y, px0, 0, arrow='last')
    cn.delete(inf)

    info['text'] = 'Size: {}x{}; Iter: {}; Time: {:2f} c; (x={}, y={}); Width: {}'.format(X, Y, MAX_ITER, time() - t0, dec_x(X/2), dec_y(Y/2), Y/s1)


#draw()

root.after(0, draw)

pn = Frame(height=60)
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
act.pack(side='left', padx=10)

Label(pn, text='  Scale:').pack(side='left')


ent_scale.pack(side='left')
ent_scale.insert(0, str(scale))

Label(pn, text='  Iter: ').pack(side='left')
ent_iter.pack(side='left')
ent_iter.insert(0, str(MAX_ITER))


def save():
    fn = fd.asksaveasfilename(initialdir='.', title='Save picture', filetypes=(('gif file', '*.gif'),))
    if fn:
        if not re.search(r'\.gif', fn, re.I):
            fn += '.gif'
        img.write(fn)
        print('Save to file: {}'.format(fn))
    else:
        print('Cancel')


sv = Button(pn, text='Save', command=save)

chouse_color = LabelFrame(pn, text='Color Type')
chouse_color.pack(side='left', padx=20)

rb_state = IntVar()
rb_state.set(2)

rb1 = Radiobutton(chouse_color, text='Black', indicatoron=0, variable=rb_state, value=1)
rb2 = Radiobutton(chouse_color, text='Gray', indicatoron=0, variable=rb_state, value=2)
rb3 = Radiobutton(chouse_color, text='Color', indicatoron=0, variable=rb_state, value=3)
rb1.pack(side='left')
rb2.pack(side='left')
rb3.pack(side='left')


#b1 = Button(chouse_color, text='OK').pack(side='left')
sv.pack(side='left')

pinfo.pack(fill ='x')
info.pack(side='left')
info['text'] = 'Hello!'



root.mainloop()