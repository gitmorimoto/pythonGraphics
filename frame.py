import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.title('learn to code at codemy.com')
root.iconbitmap('c:/gui/092.ico')
frame = tk.LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)
b = tk.Button(frame,text="Don't click here")
b2 = tk.Button(frame,text = "This is button2")
b.grid(row = 0,column= 0)
b2.grid(row = 1,column = 1)
#b.pack()
#b2.pack()
root.mainloop()

