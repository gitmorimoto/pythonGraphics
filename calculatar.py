import tkinter as tk
root=tk.Tk()
#tk.Tk() creates an instance of the Tkinter main application window.
#This window is where you will place your widgets (like buttons, labels, etc.).
#It’s typically the first thing you create in a Tkinter application.
#Think of root as the starting point or container for all your interface elements.
root.title("simple calculator")
e=tk.Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_add():
    return
button_1=tk.Button(root,text='1',padx=40,pady=20,command=button_add)
button_2=tk.Button(root,text='2',padx=40,pady=20,command=button_add)
button_3=tk.Button(root,text='3',padx=40,pady=20,command=button_add)
button_4=tk.Button(root,text='4',padx=40,pady=20,command=button_add)
button_5=tk.Button(root,text='5',padx=40,pady=20,command=button_add)
button_6=tk.Button(root,text='6',padx=40,pady=20,command=button_add)
button_7=tk.Button(root,text='7',padx=40,pady=20,command=button_add)
button_8=tk.Button(root,text='8',padx=40,pady=20,command=button_add)
button_9=tk.Button(root,text='9',padx=40,pady=20,command=button_add)
button_0=tk.Button(root,text='0',padx=40,pady=20,command=button_add)
button_plus=tk.Button(root,text='+',padx=39,pady=20,command=button_add)
button_equal=tk.Button(root,text='=',padx=86,pady=20,command=button_add)
button_clear=tk.Button(root,text='clear',padx=78,pady=20,command=button_add)
#place buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

#padx and pady are padding options
#padx (padding-x): Adds horizontal space outside the widget (to the left and right).
#pady (padding-y): Adds vertical space outside the widget (above and below).

#myButton=tk.Button(root,text="Enter your Stock Quote.",command=myClick)
root.mainloop()