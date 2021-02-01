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
root.geometry("600x600")
root.title("Elemendid Tkinteris")

#tabs=ttk.Notebook(root)
#texts=["1","2","3","4","5","6","7","8"]


tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="CAMRY 3.5")
tabs.add(tab2,text="BMW M3 E46")
tabs.add(tab3,text="AMG GT")
tabs.add(tab4,text="RS7")

def funktion(a):
    tabs.select(a)

def camry():
    lines = ""
    with open("Camry.txt", "r") as f:
        for element in f.readlines():
            lines+=element.strip()
        lbl1.configure(text=lines)

def bmw():
    lines = ""
    with open("bmw.txt", "r") as f:
        for element in f.readlines():
            lines+=element.strip()
        lbl2.configure(text=lines)

def amg():
    lines = ""
    with open("amg.txt", "r") as f:
        for element in f.readlines():
            lines+=element.strip()
        lbl3.configure(text=lines)

def rs7():
    lines = ""
    with open("rs7.txt", "r") as f:
        for element in f.readlines():
            lines+=element.strip()
        lbl4.configure(text=lines)

##########################################################НУжно сделать текст с информацией#########################################################
M=Menu(root)
root.config(menu=M)


m3=Menu(M,tearoff=0)
M.add_cascade(label="Машины",menu=m3)
m3.add_command(label="AMG GT",command=lambda:image123_("amg.png"))
m3.add_command(label="CAMRY 3.5",command=lambda:image123_("camry.png"))
m3.add_command(label="BMW e46",command=lambda:image123_("e46.png"))
m3.add_command(label="AUDI RS7",command=lambda:image123_("rs7.png"))
m3.add_separator()

m4=Menu(M,tearoff=0)
M.add_cascade(label="Информация",menu=m3)
m4.add_command(label="AMG GT")
m4.add_command(label="CAMRY 3.5")
m4.add_command(label="BMW e46")
m4.add_command(label="AUDI RS7")
m4.add_separator()

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

lbl1=Label(tab1,width=80,height=10,bg="lightblue")
lbl2=Label(tab2,width=80,height=10,bg="lightblue")
lbl3=Label(tab3,width=80,height=10,bg="lightblue")
lbl4=Label(tab4,width=80,height=10,bg="lightblue")

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
