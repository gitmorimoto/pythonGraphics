import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

root=tk.Tk()
root.title('learn to code at codemy.com')
root.iconbitmap('c:/gui/092.ico')
#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def popup():
    response=messagebox.askquestion("This is my Popup!","Hello World!")
    tk.Label(root,text=response).pack()
    if(response== "yes"):
        tk.Label(root,text="You clicked yes.").pack()
    else:
        tk.Label(root,text="You clicked no").pack()
    
tk.Button(root,text="popup",command=popup).pack()




root.mainloop()
