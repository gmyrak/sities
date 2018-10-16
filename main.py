import tkinter as tk
import game

'dev version'

root = tk.Tk()
root.geometry('800x600')
root.title('Города')
#root.resizable(False, False)
#myFont = Font(family="Times New Roman bold", size=16)


control_panel = tk.Frame(root)
text_panel = tk.Frame(root)

control_panel.place(width=400, relheight=1)
text_panel.place(width=400, relheight=1, relwidth=1, x=400)


en = tk.Entry(control_panel, font='Verdana 20 bold')
en.place(width=380, x=10, y=20)

text = tk.Text(text_panel)
text.place(relx=20, relheight=1, relwidth=1)

Scrol = tk.Scrollbar(text_panel)
Scrol.place(width=20, relheight=1)
Scrol['command'] = text.yview
text['yscrollcommand'] = Scrol.set

control_panel.configure(bg = 'gray')





root.mainloop()
