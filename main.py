import tkinter as tk
#from tkinter.font import Font
import game

root = tk.Tk()
root.geometry('800x600')
root.title('Города')
#root.resizable(False, False)
#myFont = Font(family="Times New Roman bold", size=16)


control_panel = tk.Frame(root)
control_panel.place(width=400, relheight=True)

text_panel = tk.Frame(root)
text_panel.place(width=400, relheight=True, x=400)


en = tk.Entry(control_panel, font='Verdana 20 bold')
en.place(width=380, x=10, y=20)


text = tk.Text(text_panel)
text.place(relheight=True, relwidth=True)


control_panel.configure(bg = 'gray')

root.mainloop()
