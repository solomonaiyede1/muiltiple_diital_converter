from tkinter import *
import requests

root=Tk()
root.title("Digital Conversion Calculator")
root.geometry("1200x600")
root.resizable(False, False)
logo=PhotoImage(file='logo.png')
root.iconphoto(True, logo)

#Image background
f1=Frame(root, width=300, height=450, bg="white", highlightbackground="green", highlightthickness=5)
f1.place(x=20, y=20)

image1=PhotoImage(file='background.png')
label1= Label(f1, image=image1)
label1.place(x=0, y=0)
label2=Label(f1,text="Digital Conversion Calculator", font=("Arial 14"))
label2.place(x=0, y=300)

#Digital Calculator
f2=Frame(root, width=320, height=420, bg="white", highlightbackground="green", highlightthickness=5)
f2.place(x=350, y=50)

def show1(x):
    e1.insert(END, x)

e1=Entry(f2, width=50, font=("Arial 18"))


def wipe1():
    e1.delete(0, END)

def result():
    answer=eval(e1.get())
    e1.delete(0, END)
    e1.insert(END, answer)
lc=Label(root, text="Electronic Calculator", font=("Arial 20"), fg="blue")
b9=Button(f2, width=10, height=2, text="9", bg="white", command=lambda:show1(9))
b8=Button(f2, width=10, height=2, text="8", bg="white", command=lambda:show1(8))
b7=Button(f2, width=10, height=2, text="7", bg="white", command=lambda:show1(7))

b6=Button(f2, width=10, height=2, text="6", bg="white", command=lambda:show1(6))
b5=Button(f2, width=10, height=2, text="5", bg="white", command=lambda:show1(5))
b4=Button(f2, width=10, height=2, text="4", bg="white", command=lambda:show1(4))

b3=Button(f2, width=10, height=2, text="3", bg="white", command=lambda:show1(3))
b2=Button(f2, width=10, height=2, text="2", bg="white", command=lambda:show1(2))
b1=Button(f2, width=10, height=2, text="1", bg="white", command=lambda:show1(1))

b0=Button(f2, width=10, height=2, text="0", bg="white", command=lambda:show1(0))
bplus=Button(f2, width=10, height=2, text="+", bg="white",command=lambda:show1("+"))
bminus=Button(f2, width=10, height=2, text="-", bg="white",command=lambda:show1("-"))

btimes=Button(f2, width=10, height=2, text="X", bg="white",command=lambda:show1("*"))
bdivide=Button(f2, width=10, height=2, text="/", bg="white",command=lambda:show1("/"))
bequals=Button(f2, width=10, height=2, text="=", bg="white", command=result)

bclear=Button(f2, width=31, height=2, text="clear", bg="white", command=wipe1)

lc.place(x=350, y=5)
b7.place(x=5, y=40)
b8.place(x=80, y=40)
b9.place(x=150, y=40)

b4.place(x=5, y=80)
b5.place(x=80, y=80)
b6.place(x=150, y=80)
#
b1.place(x=5, y=120)
b2.place(x=80, y=120)
b3.place(x=150, y=120)
#
b0.place(x=5, y=160)
bplus.place(x=80, y=160)
bminus.place(x=150, y=160)
#
btimes.place(x=5, y=200)
bdivide.place(x=80, y=200)
bequals.place(x=150, y=200)
#
bclear.place(x=5, y=240)

e1.place(x=2, y=2)


#Digital converter
f3=Frame(root, width=500, height=420, bg="white", highlightbackground="green", highlightthickness=5)
f3.place(x=700, y=50)
ld=Label(root, text="Digital Converter", font=("Arial 20"), fg="green")

def hour():
    h=e3.get()
    h=int(h)*60
    e4.insert(END, h)

l3=Label(f3, text="Hour to minutes")
e3=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e4=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l3.place(x=0,y=10)
e3.place(x=10, y=30)
e4.place(x=300, y=30)
bh=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command=hour)
bh.place(x=150, y=30)

def df():
    from fractions import Fraction
    a=float(e5.get())
    x = Fraction(a).limit_denominator()
    e6.delete(0, END)
    e6.insert(END, x)

l5=Label(f3, text="Decimal to Fraction")
e5=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e6=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l5.place(x=0,y=70)
e5.place(x=10, y=90)
e6.place(x=300, y=90)
bh1=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command=df)
bh1.place(x=150, y=90)
# #

def degree1():
    import math
    x=int(e7.get())
    x=math.radians(x)
    e8.insert(END, x)

l7=Label(f3, text="Degree to Radian")
e7=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e8=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l7.place(x=0,y=140)
e7.place(x=10, y=160)
e8.place(x=300, y=160)
bh2=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command=degree1)
bh2.place(x=150, y=160)
#
def km():
    x=int(e9.get())
    x=1000*x
    e10.insert(END, x)

l9=Label(f3, text="Kilometer to meter")
e9=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e10=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l9.place(x=0,y=210)
e9.place(x=10, y=230)
e10.place(x=300, y=230)
bh3=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command=km)
bh3.place(x=150, y=230)
# #

def cf():
    x=int(e11.get())
    x=(x*9/5)+32
    e12.delete(0, END)
    e12.insert(END, x)


l11=Label(f3, text="Celcius to faraheit")
e11=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e12=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l11.place(x=0,y=270)
e11.place(x=10, y=290)
e12.place(x=300, y=290)
bh4=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command=cf)
bh4.place(x=150, y=290)
# #

def dollar1():
    url="https://v6.exchangerate-api.com/v6/d8e91155d4e7d129086fc1d8/pair/USD/NGN"
    response= requests.get(url)
    res=response.json()
    x=int(res['conversion_rate'])
    y= int(e13.get())
    z=x*y
    e14.delete(0, END)
    e14.insert(END, z)

l13=Label(f3, text="Dollar to Naira")
e13=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
e14=Entry(f3, font=("Arial 14"), highlightbackground="black", highlightthickness=1, width=10)
l13.place(x=0,y=340)
e13.place(x=10, y=360)
e14.place(x=300, y=360)
bh5=Button(f3, width=15, height=1, text="convert", bg="green", fg="white", command= dollar1)
bh5.place(x=150, y=360)

ld.place(x=700, y=5)

lt=Label(root, text="Built by Solomon", font=("Arial, 40"))
lt.place(x=400, y=520)
root.mainloop()