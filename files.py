import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog

root=tk.Tk()
root.title('learn to code at codemy.com')
#root.iconbitmap('c:/gui/092.ico')

root.filename = filedialog.askopenfile(initialdir = 'C:\gui\images',title = "Select A file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")) )                                                                   
my_label=tk.Label(root,text=root.filename).pack()
my_image = ImageTK.PhotoImage(Image.open(root.filename))
my_image_table = tk.Label(image = my_image).pack()
root.mainloop()
