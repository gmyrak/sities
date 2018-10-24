import tkinter as tk
import game



root = tk.Tk()
#root.geometry('800x600')
root.title('Города')
root.resizable(True, True)
#myFont = Font(family="Times New Roman bold", size=16)

panel_ctrl = tk.Frame(root, width=400, bg='gray')
panel_ctrl.pack(side='left', fill='y')

en = tk.Entry(panel_ctrl, font='Verdana 20 bold')
en.pack(padx=10, pady=10)

but = tk.Button(panel_ctrl, text='OK', width=10)
but.pack(padx=10, pady=10)

text = tk.Text(root)
text.pack(side='left', fill='both', expand=1)
scroll = tk.Scrollbar(command=text.yview)
scroll.pack(side='left', fill='y')
text.config(yscrollcommand=scroll.set)


#cn = tk.Canvas(root, bg='yellow')
#cn.pack(side='left', fill='both', expand=1)


'''
panel_ctrl.place(width=400, relheight=1)
panel_text.place(width=400, relheight=1, relwidth=1, x=400)



en.place(relwidth=0.8, relx=0.1, y=20)

but = tk.Button(panel_ctrl, text='OK')
but.place(relx=0.5, y=70)

text = tk.Text(panel_text)
text.place(x=20, relheight=1, relwidth=1)

Scrol = tk.Scrollbar(panel_text)
Scrol.place(width=20, relheight=1)
#Scrol.pack(side='right', fill='y')
Scrol['command'] = text.yview
text['yscrollcommand'] = Scrol.set

panel_ctrl.configure(bg ='gray')
'''




root.mainloop()
