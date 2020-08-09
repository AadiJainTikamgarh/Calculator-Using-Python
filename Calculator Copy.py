from tkinter import *
from tkinter import messagebox

def About():
    messagebox.showinfo("About Us", """This is a calculator Created by Aadi Jain 
        Using Pyhton 3 and Tkinter""")

root = Tk()
def top():
    l1 = Toplevel(root)
    l1.geometry("600x200")
    l1.title("About Us")
    l1.configure()
    Label(l1, text="This is an Calculator Created BY:- ", font="lucida 16 bold").pack()
    Label(l1, text="Aadi Jain", font="lucida 16 bold").pack()
    Label(l1, text="With the Help of:-", font="lucida 16 bold").pack()
    Label(l1, text="Python 3 and Tkinter", font="lucida 16 bold").pack()

# menubar = (root)
# def func():
#     messagebox.showinfo("info","Invalid Operation")


#MainMenu
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff= 0)
m1.add_command(label="About us", command = top)

root.configure(menu=mainmenu)
mainmenu.add_cascade(label="About",menu = m1)
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = ""

        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

    # if value == "":
    #     func()
    #     value == ""
    # else :
    #   pass    


# root = Tk()
root.geometry("269x390")
root.maxsize(269, 400)
root.minsize(269, 390)
root.title("Calculator")
# root.iconbitmap("1.ico")
root.configure(background="#696969")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=11.85, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=15.49, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=13.98, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=15, pady=15, font="lucida 20 bold", bg="#A9A9A9", fg="white")
b.pack(side=LEFT, fill="both")
b.bind("<Button-1>", click)

f.pack()
"""
f = Frame(root, bg="grey")
b = Button(f, text="/", padx=33, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=21, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=27, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=26, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()
"""
root.mainloop()
