from tkinter import *
from tkinter.messagebox import showinfo
import os

root = Tk()
root.geometry("310x420")
root.title("Calculater")
if "app_comp" in os.listdir():
    root.wm_iconbitmap("app_comp\\Icons\\Calculator.ico")
root.minsize(310, 420)
root.maxsize(310, 420)

# Variables
def_font = ("Verdana 20 bold")
sc_font = ("Verdana 30 bold")
typed = ""
# funcs
def show_help():
    help_root = Tk()
    help_root.title("HELP")
    help_root.geometry("900x130")
    help_root.minsize(900, 130)
    help_root.maxsize(900, 130)

    l = Label(help_root, text="HELP", font=("Verdana 30 bold"))
    l.pack()

    l = Label(help_root, text="You can use Calculator to perform simple calculations such as addition, subtraction, multiplication, and division\n" + "You can perform calculations by clicking the calculator buttons, or you can type calculations by using your keyboard.\n" + " You can also use the numeric keypad to type numbers and operators by pressing Num Lock" , font=("Verdana 10 bold"))
    l.pack()
    help_root.mainloop()

def show_about():
    showinfo("ABOUT", "This Is A Simple Calculater Made By Abhishek Kumar In Python Programming Languange")

def calc(event):

    global sc_value
    text = event.widget.cget("text").replace("←", "")    

    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        
        else:
            try:
                value = eval(screen.get())
            
            except Exception as e:
                print(e)
                value = "Error"
        
        sc_value.set(value)
        screen.update()

    elif text == "C":
        sc_value.set("")
        screen.update()
    
    elif event.widget.cget("text") == "←":
        sc_value.set(sc_value.get()[:len(sc_value.get())-1])

    elif sc_value.get() == "0":
        sc_value.set("")
        sc_value.set(sc_value.get() + text)

    else:
        sc_value.set(sc_value.get() + text)
        screen.update()

# menus
m_menu = Menu(root)
m1 = Menu(m_menu, tearoff=0)
m1.add_command(label="View Help", command=show_help)
m1.add_command(label="About Calculator", command=show_about)
m_menu.add_cascade(label="Help", menu=m1)
root.config(menu=m_menu)

sc_value = StringVar()
sc_value.set("0")

# entry
screen = Entry(root, textvar=sc_value, font=sc_font, justify="right")
screen.pack(fill=X, padx=10, pady=10)

# Frames
f1 = Frame(root)
f1.place(x=10, y=75)

f2 = Frame(root)
f2.place(x=10, y=160)

f3 = Frame(root)
f3.place(x=10, y=245)

f4 = Frame(root)
f4.place(x=10, y=330)

f5 = Frame(root)
f5.place(x=10, y=415)

# buttons

# 1st COL
b = Button(f1, text="←", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f1, text="/", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f1, text="C", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f1, text="*", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f1, text="-", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

# 2nd COl
b = Button(f2, text="7", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f2, text="8", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f2, text="9", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f2, text="+", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f2, text="%", font=def_font, width=2)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

# 3rd COl
b = Button(f3, text="4", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f3, text="5", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f3, text="6", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(root, text="0", font=def_font)
b.place(x=190, y=245)
b.bind("<Button-1>", calc)

b = Button(root, text=".", font=def_font, width=2)
b.place(x=250, y=245)
b.bind("<Button-1>", calc)

b = Button(root, text="=", font=def_font, width=5)
b.place(x=190, y=330)
b.bind("<Button-1>", calc)

# 4th COl
b = Button(f4, text="1", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f4, text="2", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

b = Button(f4, text="3", font=def_font)
b.pack(side=LEFT, padx=5)
b.bind("<Button-1>", calc)

root.mainloop()
