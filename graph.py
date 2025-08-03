import tkinter as tk

def on_click():
    label.config(text="Button Clicked!")

root = tk.Tk()               # Create the main window
root.title("My First GUI")
root.geometry("300x200")     # Set window size

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()              # Start the GUI event loop
   