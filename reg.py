from tkinter import *
from tkinter import messagebox
import os
import webbrowser
from tkhtmlview import HTMLLabel
import digital_conversion_calculator

root=Tk()
root.geometry("400x300")
root.title("Login Page")
root.resizable(False, False)

def log():
    user=e3.get()
    pass1=e4.get()
    if(user=="" or pass1==""):
        messagebox.showinfo("Error", "Please field cannot be left empty")
    elif(user != "solo" and pass1 != "springboard"):
        messagebox.showinfo("Eror", "Incorrect username or password")
    elif(user=="solo" and pass1=="springboard"):
        messagebox.showinfo("success", "You have successfully logged in")
        root.destroy()
        os.system("digital_conversion_calculator.py")

def web1():
    webbrowser.open_new("https://facebook.com")



l1=Label(root, text="Login Page", font=("Calibri, 20"))
l2=Label(root, text="Please enter your login details below")

l3=Label(root, text="Username")
e3=Entry(root)
l4=Label(root, text="Password")
e4=Entry(root, show="*")
b4=Button(root, text="Login", bg="green", fg="white", height=1, width=10, command=log)
b5=Button(root, text="web", bg="green", fg="white", height=1, width=10, command=web1)

html01=HTMLLabel(root, html='<a href="https://www.facebook.com">Link to facebook</a>')

l1.place(x=100, y=20)
l2.place(x=100, y=50)
l3.place(x=20, y=90)
e3.place(x=100, y=90)
l4.place(x=20, y=130)
e4.place(x=100, y=130)
b4.place(x=140, y=170)
b5.place(x=200, y=170)
html01.place(x=200, y=250)
root.mainloop()