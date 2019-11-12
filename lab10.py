from tkinter import *
import tkinter as tk
root= Tk()

idli = tk.IntVar()
dosa = tk.IntVar()
puri = tk.IntVar()
vada = tk.IntVar()
palav = tk.IntVar()
biryani = tk.IntVar()

def var_states():
   a=idli.get()
   b=dosa.get()
   c=puri.get()
   d=vada.get()
   e=palav.get()
   f=biryani.get()
   root1 = Tk()
   root1.geometry("200x200")
   cost = a*15 + b*50 + c*35 + d*15 + e*45 + f*120
   tk.Label(root1, text="the cost was : "+str(cost),justify = tk.CENTER,padx = 20).pack()
   

root.geometry("500x500") 
tk.Label(root, text="""Simple Restaurant menu :""",justify = tk.CENTER,padx = 20).pack()
tk.Label(root, text="""""",justify = tk.CENTER,padx = 20).pack()

tk.Label(root, text="""**ITEM**""",justify = tk.CENTER,padx = 40).place(relx = 0.1, rely = 0.1)
tk.Label(root, text="""**PRICE**""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.1)

tk.Checkbutton(root, text="IDLI",padx = 20, variable=idli).place(relx = 0.1, rely = 0.17)
tk.Label(root, text="""Rs. 15""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.17)

tk.Checkbutton(root,text="MASALA DOSA", padx = 20,  variable=dosa).place(relx = 0.1, rely = 0.23)
tk.Label(root, text="""Rs. 50""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.23)

tk.Checkbutton(root,text="PURI", padx = 20,  variable=puri).place(relx = 0.1, rely = 0.29)
tk.Label(root, text="""Rs. 35""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.29)

tk.Checkbutton(root,text="VADA", padx = 20,  variable=vada).place(relx = 0.1, rely = 0.35)
tk.Label(root, text="""Rs. 15""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.35)

tk.Checkbutton(root,text="PALAV", padx = 20,  variable=palav).place(relx = 0.1, rely = 0.41)
tk.Label(root, text="""Rs. 45""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.41)

tk.Checkbutton(root,text="BIRYANI", padx = 20,  variable=biryani).place(relx = 0.1, rely = 0.47)
tk.Label(root, text="""Rs. 120""",justify = tk.CENTER,padx = 40).place(relx = 0.5, rely = 0.47)

Button(root, text='Quit', command=root.quit).place(relx = 0.20, rely = 0.60)
Button(root, text='Submit', command=var_states).place(relx = 0.40, rely = 0.60)

root.mainloop()
