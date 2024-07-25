# This digital coverter is meant to convert the following parameters
# 1. currency converter: dollar to naira
# 2. Temperature converter
# 3. Degree to radian
# 4. decimal to fraction
# 5. hour to minutes
# 6. Kilometer to Meter

from tkinter import *
root=Tk()
root.title("Digital Converter")
root.resizable(False, False)
root.geometry("1200x500")

#0. Include Calculator initially build on a frame at the right side
f=Frame(root, width=300, height=400, background='white', highlightbackground='black', highlightthickness=1)
f.place(x=800, y=20)
l0=Label(f, text="Electronic Calculator")
l0.place(x=10, y=10)
img=PhotoImage(file="check.png")
ico=root.iconphoto(False, img)
l1=Label(f, image=img)
l1.place(x=10, y=20)


#1. Hour to minutes
label1=Label(root, text="Hour to Minute conversion")
label1.place(x=50, y=30)
entry1= Entry(root, font=('Arial', 14))
entry1.insert(0, "")
entry1.place(x=50, y=50)
btn1=Button(root, text="Convert", width=10, height=2, bg='blue',fg="white")
btn1.place(x=380, y=50)
entry2= Entry(root, font=('Arial', 14))
entry2.insert(0, "")
entry2.place(x=500, y=50)

#2.  Decimal to Fraction
label1=Label(root, text="Decimal to fraction")
label1.place(x=50, y=80)
entry3= Entry(root, font=('Arial', 14))
entry3.insert(0, "")
entry3.place(x=50, y=100)
btn2=Button(root, text="Convert", width=10, height=2, bg='red',fg="white")
btn2.place(x=380, y=100)
entry4= Entry(root, font=('Arial', 14))
entry4.insert(0, "")
entry4.place(x=500, y=100)

#3. Degree to radian
label1=Label(root, text="Degree to Radian")
label1.place(x=50, y=130)
entry5= Entry(root, font=('Arial', 14))
entry5.insert(0, "")
entry5.place(x=50, y=150)
btn3=Button(root, text="Convert", width=10, height=2, bg='green',fg="white")
btn3.place(x=380, y=150)
entry6= Entry(root, font=('Arial', 14))
entry6.insert(0, "")
entry6.place(x=500, y=150)

#4. Degree to Faraheit
label1=Label(root, text="Degree to Faraheit")
label1.place(x=50, y=180)
entry7= Entry(root, font=('Arial', 14))
entry7.insert(0, "")
entry7.place(x=50, y=200)
btn4=Button(root, text="Convert", width=10, height=2, bg='purple',fg="white")
btn4.place(x=380, y=200)
entry8= Entry(root, font=('Arial', 14))
entry8.insert(0, "")
entry8.place(x=500, y=200)

#5. Kilometer to Meter
label1=Label(root, text="Kilometer to meter")
label1.place(x=50, y=230)
entry9= Entry(root, font=('Arial', 14))
entry9.insert(0, "")
entry9.place(x=50, y=250)
btn5=Button(root, text="Convert", width=10, height=2, bg='black',fg="white")
btn5.place(x=380, y=250)
entry10= Entry(root, font=('Arial', 14))
entry10.insert(0, "")
entry10.place(x=500, y=250)

#6. Dollar to Naira
label1=Label(root, text="Dollar to Naira")
label1.place(x=50, y=280)
entry11= Entry(root, font=('Arial', 14))
entry11.insert(0, "")
entry11.place(x=50, y=300)
btn6=Button(root, text="Convert", width=10, height=2, bg='magenta',fg="white")
btn6.place(x=380, y=300)
entry12= Entry(root, font=('Arial', 14))
entry12.insert(0, "")
entry12.place(x=500, y=300)

root.mainloop()

