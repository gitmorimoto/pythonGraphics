import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.title("Learn to code at Codemy.com")
root.iconbitmap('C:\gui\092.ico')
button_quit=tk.Button(root,text="Exit Program",command=root.quit)
button_quit.pack()
my_image = ImageTk.PhotoImage(Image.open('092.jpg'))
my_label =tk.Label(image = my_image)
my_label.pack()
root.mainloop()