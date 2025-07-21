import tkinter as tk
root = tk.Tk()
myLabel1 = tk.Label(root,text="grid practice").grid(row=0,column=0)
myLabel2 = tk.Label(root,text="My name is morimoto.").grid(row=1,column=2)
myLabel3 = tk.Label(root,text="                   ").grid(row=1,column=1)

root.mainloop()