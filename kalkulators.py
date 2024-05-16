from tkinter import *


mansLogs = Tk()
mansLogs.title("Kalkulators")


pirmais_skaitlis = None
operacija = None


def btn_klikskis(skaitlis):
    pašreizējais = e.get()
    e.delete(0, END)
    jauns_skaitlis = str(pašreizējais) + str(skaitlis)
    e.insert(0, jauns_skaitlis)


def btn_operacija(op):
    global pirmais_skaitlis, operacija
    pirmais_skaitlis = float(e.get())
    operacija = op
    e.delete(0, END)


def btn_vienads():
    global pirmais_skaitlis, operacija
    otrais_skaitlis = float(e.get())
    e.delete(0, END)

    if operacija == "+":
        e.insert(0, pirmais_skaitlis + otrais_skaitlis)
    elif operacija == "-":
        e.insert(0, pirmais_skaitlis - otrais_skaitlis)
    elif operacija == "*":
        e.insert(0, pirmais_skaitlis * otrais_skaitlis)
    elif operacija == "/":
        if otrais_skaitlis == 0:
            e.insert(0, "Kļūda")
        else:
            e.insert(0, pirmais_skaitlis / otrais_skaitlis)
    pirmais_skaitlis = None
    operacija = None


def btn_notirit():
    e.delete(0, END)


e = Entry(mansLogs, width=15, bd=20, font=("Arial Black", 20), justify="right")
e.grid(row=0, column=0, columnspan=4)


btn0 = Button(mansLogs, text='0', padx=40, pady=20, command=lambda: btn_klikskis(0), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn1 = Button(mansLogs, text='1', padx=40, pady=20, command=lambda: btn_klikskis(1), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn2 = Button(mansLogs, text='2', padx=40, pady=20, command=lambda: btn_klikskis(2), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn3 = Button(mansLogs, text='3', padx=40, pady=20, command=lambda: btn_klikskis(3), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn4 = Button(mansLogs, text='4', padx=40, pady=20, command=lambda: btn_klikskis(4), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn5 = Button(mansLogs, text='5', padx=40, pady=20, command=lambda: btn_klikskis(5), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn6 = Button(mansLogs, text='6', padx=40, pady=20, command=lambda: btn_klikskis(6), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn7 = Button(mansLogs, text='7', padx=40, pady=20, command=lambda: btn_klikskis(7), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn8 = Button(mansLogs, text='8', padx=40, pady=20, command=lambda: btn_klikskis(8), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)
btn9 = Button(mansLogs, text='9', padx=40, pady=20, command=lambda: btn_klikskis(9), bg="light blue", font=("Arial Black", 12), bd=5, relief=RAISED)

btn_plus = Button(mansLogs, text='+', padx=39, pady=20, command=lambda: btn_operacija("+"), bg="light gray", font=("Arial Black", 12), bd=5, relief=RAISED)
btn_minus = Button(mansLogs, text='-', padx=41, pady=20, command=lambda: btn_operacija("-"), bg="light gray", font=("Arial Black", 12), bd=5, relief=RAISED)
btn_reizinat = Button(mansLogs, text='*', padx=40, pady=20, command=lambda: btn_operacija("*"), bg="light gray", font=("Arial Black", 12), bd=5, relief=RAISED)
btn_dalit = Button(mansLogs, text='/', padx=41, pady=20, command=lambda: btn_operacija("/"), bg="light gray", font=("Arial Black", 12), bd=5, relief=RAISED)
btn_vienads = Button(mansLogs, text='=', padx=40, pady=20, command=btn_vienads, bg="light gray", font=("Arial Black", 12), bd=5, relief=RAISED)
btn_notirit = Button(mansLogs, text='C', padx=40, pady=20, command=btn_notirit, bg="red", font=("Arial Black", 12), bd=5, relief=RAISED)


btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_reizinat.grid(row=3, column=3)

btn0.grid(row=4, column=0)
btn_notirit.grid(row=4, column=1)
btn_vienads.grid(row=4, column=2)
btn_dalit.grid(row=4, column=3)


mansLogs.mainloop()
