'''
https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Create-your-first-GUI-application
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5_%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82%D1%8B
http://gitolite.com/detached-head.html
'''



import tkinter as tk

class root(tk.Tk):
    def __INIT__(self):
        self.geometry('800x600')


win = root()
win.mainloop()
