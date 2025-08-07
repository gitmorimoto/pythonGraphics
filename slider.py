import tkinter as tk
from PIL import ImageTk,Image
#from tkinter import filedialog

root=tk.Tk()
root.title('learn to code at codemy.com')

vertical=tk.Scale(root,from_= 0, to = 400)
vertical.pack()
horizontal=tk.Scale(root,from_=0,to=400,orient=tk.HORIZONTAL)
horizontal.pack()
def slide():
    my_label=tk.Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
my_btn=tk.Button(root,text='Click me',command=slide).pack()


root.mainloop()