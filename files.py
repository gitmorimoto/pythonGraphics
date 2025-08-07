import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog

root=tk.Tk()
root.title('learn to code at codemy.com')
root.myImage=None
#root.iconbitmap('c:/gui/092.ico')
def open():
    root.filename =  filedialog.askopenfilename(initialdir = 'C:/gui/images',title = "Select A file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")) )                                                                   
    my_label=tk.Label(root,text=root.filename).pack()
    root.myImage = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_table = tk.Label(image = root.myImage).pack()
my_btn=tk.Button(root,text="open file",command=open).pack()
root.mainloop()