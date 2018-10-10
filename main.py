import tkinter as ui
import game

root = ui.Tk()
root.geometry('800x600')
root.title('Города')
#root.resizable(False, False)

control_panel = ui.Frame(root)
control_panel.place(width=200, relheight=True)

control_panel.configure(bg = 'red')

root.mainloop()
