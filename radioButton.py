import tkinter as tk
from PIL import ImageTk,Image

root=tk.Tk()
root.title('learn to code at codemy.com')
root.iconbitmap('c:/gui/092.ico')
r = tk.IntVar()
r.set('2')
def clicked(value):
    myLabel=tk.Label(root,text = r.get())
    myLabel.pack()
    

tk.Radiobutton(root,text="Option 1",variable = r,value = 1).pack()
tk.Radiobutton(root,text="Option 2",variable = r,value = 2).pack()

myButton = tk.Button(root,text = "click me",command = lambda:clicked(r.get())).pack()


root.mainloop()
