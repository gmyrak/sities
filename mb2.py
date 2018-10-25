from tkinter import *

X, Y = 300, 200

X0, Y0 = 3*X/5, Y/2
s1 = 100

MAX_ITER = 100


def mandelbrot(c):
    z = c
    i = 0
    while i < MAX_ITER and abs(z) < 2:
        z = z**2 + c
        i += 1
    return i


def color(n):
    tone = int(0xFFF - 0xFFF * n / MAX_ITER)
    return '#{:03x}{:03x}{:03x}'.format(tone, tone, tone)


def dec_x(i):
    return (i-X0)/s1


def dec_y(j):
    return (Y0-j)/s1


root = Tk()
root.resizable(0, 0)
cn = Canvas(root, width=X, height=Y, bg='white')
img = PhotoImage(width=X,height=Y)

cn.create_image(0, 0, anchor=NW, image=img)

def draw():
    img.blank()
    for i in range(X):
        for j in range(Y):
            c = complex(dec_x(i), dec_y(j))
            img.put( color(mandelbrot(c)) , to=(i, j))

    img.write('pic{}x{}({}).gif'.format(X, Y, MAX_ITER))

    cn.create_image(0, 0, anchor=NW, image=img)
    cn.create_line(0, Y0, X, Y0, arrow='last')
    cn.create_line(X0, Y, X0, 0, arrow='last')


draw()
cn.pack()

pn = Frame(height=50)
pn.pack(fill='x')


def cn_clisk(event):
    print(event.x, event.y)


cn.bind('<Button-1>', cn_clisk)


def act_press():
    cn.delete('all')
    inf = cn.create_text(20, 30, text='Wait...')
    cn.update()
    draw()
    cn.delete(inf)



act = Button(pn, text='OK', command=act_press)
act.pack(side='left')

root.mainloop()