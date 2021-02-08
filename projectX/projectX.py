from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter .filedialog import *
import fileinput
from tkinter.messagebox import *

def image123_ (name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(3)
    can.create_image(20,20,image=img,anchor=NW)
    
root=Tk()
root.geometry("800x800")
root.title("Elemendid Tkinteris")
#222
tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="CAMRY 3.5")
tabs.add(tab2,text="BMW M3 E46")
tabs.add(tab3,text="AMG GT")
tabs.add(tab4,text="RS7")

texts=""
def camry():
    global texts
    for text in fileinput.input("Camry.txt"):
        texts=texts+text
        lbl1.configure(text=texts)

texts1=""
def bmw():
    global texts1
    for text in fileinput.input("bmw.txt"):
        texts1=texts1+text
        lbl2.configure(text=texts1)

texts2=""
def amg():
    global texts2
    for text in fileinput.input("amg.txt"):
        texts2=texts2+text
        lbl3.configure(text=texts2)

texts3=""
def rs7():
    global texts3
    for text in fileinput.input("rs7.txt"):
        texts3=texts3+text
        lbl4.configure(text=texts3)

M=Menu(root)
root.config(menu=M)

m3=Menu(M,tearoff=0)
M.add_cascade(label="Машины",menu=m3)
m3.add_command(label="AMG GT",command=lambda:image123_("amg.png"))
m3.add_command(label="CAMRY 3.5",command=lambda:image123_("camry.png"))
m3.add_command(label="BMW E46",command=lambda:image123_("e46.png"))
m3.add_command(label="AUDI RS7",command=lambda:image123_("rs7.png"))
m3.add_separator()

can2=Canvas(tab1,width=500,height=400,)
img2=PhotoImage(file="camry.png").subsample(3)
can2.create_image(20,20,image=img2,anchor=NW)
btn3=Button(tab1,text="Информация об Авто", command=camry)

can1=Canvas(tab2,width=500,height=400,)
img1=PhotoImage(file="e46.png").subsample(3)
can1.create_image(20,20,image=img1,anchor=NW)
btn2=Button(tab2,text="Информация об Авто", command=bmw)

can=Canvas(tab3,width=500,height=400,)
img=PhotoImage(file="amg.png").subsample(3)
can.create_image(20,20,image=img,anchor=NW)
btn1=Button(tab3,text="Информация об Авто", command=amg)

can3=Canvas(tab4,width=500,height=400,)
img3=PhotoImage(file="rs7.png").subsample(3)
can3.create_image(20,20,image=img3,anchor=NW)
btn4=Button(tab4,text="Информация об Авто", command=rs7)

lbl1=Label(tab1,width=100,height=30,bg="lightblue")
lbl2=Label(tab2,width=100,height=30,bg="lightblue")
lbl3=Label(tab3,width=100,height=30,bg="lightblue")
lbl4=Label(tab4,width=100,height=30,bg="lightblue")

can.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
can1.pack()
can2.pack()
can3.pack()
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
tabs.pack(fill="both")
root.mainloop()
