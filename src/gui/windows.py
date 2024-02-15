import tkinter as tk
from tkinter import ttk

class HelloWindow(tk.Tk):
    """
    Dedicated GUI Window for Hello Application

    Parameters:
    -----------
    - app: Application - An instantiation of the Application object
    """
    def __init__(self, app):
        self._app = app
        tk.Tk.__init__(self)
        self.winfo_toplevel().title("Hello Window")

        self._frame = HelloFrame(self)

        self.winfo_toplevel().geometry("460x250+50+10")
        self.resizable(0,0)

        self._frame.grid(row=0, column=0, sticky="NEWS")

        self.mainloop()
    
    def app(self):
        return self._app

class HelloFrame(tk.Frame):
    """
    Dedicated Frame for Hello Application
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='white', width="750")
        self.winfo_toplevel().geometry("550x500")

        _label = ttk.Label(self, text="Hello!")
        _label.pack()

        self.place(relx=0.5, rely=0.5, anchor='center')
