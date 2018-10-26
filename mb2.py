from tkinter import *
from time import time


I_MAX, J_MAX = 300, 200
ITER_LIMIT = 50
BASE_SIZE = I_MAX/4

POINT_R = 3


root = Tk()
root.title('Set of Malderbrot')
root.resizable(0, 0)
CNVS = Canvas(root, width=I_MAX, height=J_MAX, bg='white')
CNVS.pack()
PNL = Frame(height=50)
PNL.pack(fill='x')



class Fractal():
    def __init__(self):
        self.i0, self.j0 = 3 * I_MAX / 5, J_MAX / 2
        self.iter_limit = ITER_LIMIT
        self.scale = 0
        self.s1 = self.size_one(self.scale)
        self.i_point, self.j_point = I_MAX / 2, J_MAX / 2
        self.pointer = 0
        self.img = PhotoImage(width=I_MAX, height=J_MAX)
        self.draw()

    def size_one(self, scale):
        return BASE_SIZE * 10**scale

    def dec_x(self, i):
        return (i - self.i0) / self.s1

    def dec_y(self, j):
        return (self.j0 - j) / self.s1

    def mandelbrot(self, c):
        z = c
        i = 0
        while i < self.iter_limit and abs(z) < 2:
            z = z ** 2 + c
            i += 1
        return i

    def color(self, n):
        tone = int(0xFFF - 0xFFF * n / self.iter_limit)
        return '#{:03x}{:03x}{:03x}'.format(tone, tone, tone)

    def draw(self):
        t0 = time()
        CNVS.delete('all')
        inf = CNVS.create_text(I_MAX / 2, J_MAX / 2, text='', anchor='center')
        CNVS.update()
        self.img.blank()
        per = 0
        for i in range(I_MAX):
            per2 = 100 * i // I_MAX
            if per2 != per:
                per = per2
                CNVS.itemconfig(inf, text='Processing: {:3}%'.format(per), )
                CNVS.update()
            for j in range(J_MAX):
                c = complex(self.dec_x(i), self.dec_y(j))
                self.img.put( self.color(self.mandelbrot(c)) , to=(i, j))
        CNVS.create_image(0, 0, anchor=NW, image=self.img)
        CNVS.create_line(0, self.j0, I_MAX, self.j0, arrow='last')
        CNVS.create_line(self.i0, J_MAX, self.i0, 0, arrow='last')
        CNVS.delete(inf)
        if self.pointer > 0:
            CNVS.delete(self.pointer)
            self.pointer = 0
        print('Draw fractal {}x{} ({} iter): {:2f} c'.format(I_MAX, J_MAX, self.iter_limit, time() - t0))

    def set_pointer(self, i, j):
        if self.pointer > 0:
            CNVS.delete(self.pointer)
        self.pointer = CNVS.create_oval(i - POINT_R, j - POINT_R, i + POINT_R, j + POINT_R, fill='yellow', outline='red', tag='p')
        self.i_point, self.j_point = i, j

    def recalculate(self, new_scale, iter_limit):
        s2 = self.size_one(new_scale)
        self.i0 = I_MAX/2 - s2 * (self.i_point - self.i0)/self.s1
        self.j0 = J_MAX/2 + s2 * (self.j0 - self.j_point)/self.s1
        self.s1 = s2
        self.iter_limit = iter_limit
        self.draw()




F = Fractal()


CNVS.bind('<Button-1>', lambda e : F.set_pointer(e.x, e.y))

ent_scale = Entry(PNL, width=8)
ent_iter = Entry(PNL, width=8)


act = Button(PNL, text='Redraw', command= lambda : F.recalculate(float(ent_scale.get()), int(ent_iter.get())))
act.pack(side='left')

Label(PNL, text='  Scale:').pack(side='left')


ent_scale.pack(side='left')
ent_scale.insert(0, str(F.scale))

Label(PNL, text='  Iter: ').pack(side='left')
ent_iter.pack(side='left')
ent_iter.insert(0, str(F.iter_limit))


root.mainloop()