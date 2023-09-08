from tkinter import *
from tkinter import messagebox

def validate_dollar_input(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
def validate_mark_input(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def konvertuj_u_marke(*args):
    try:
        vrijednost_dolara = float(unos_dolara.get())
        vrijednost_marke = round(vrijednost_dolara * 1.8, 2)
        unos_marke.delete(0, END)
        unos_marke.insert(0, vrijednost_marke)
    except ValueError:
        pass


def konvertuj_u_dolar(*args):
    try:
        vrijednost_marke = float(unos_marke.get())
        vrijednost_dolara = round(vrijednost_marke / 1.82, 2)
        unos_dolara.delete(0, END)
        unos_dolara.insert(0, vrijednost_dolara)
    except ValueError:
        pass


def restart():
    unos_dolara.delete(0, END)
    unos_marke.delete(0, END)



window = Tk()
window.geometry("1000x500")

frame = Frame(window)
frame.pack(pady=30)

dolar = Label(frame, text="USD", font=("Arial", 15))
dolar.grid(row=0, column=0)
validate_dollar = window.register(validate_dollar_input)
unos_dolara = Entry(frame, validate="key", validatecommand=(validate_dollar, "%P"))
unos_dolara.grid(row=0, column=1)
unos_dolara.bind("<KeyRelease>", konvertuj_u_marke)


marka = Label(frame, text="KM", font=("Arial", 15))
marka.grid(row=0, column=2)
validate_mark = window.register(validate_mark_input)
unos_marke = Entry(frame, validate="key", validatecommand=(validate_mark, "%P"))
unos_marke.grid(row=0, column=3)
unos_marke.bind("<KeyRelease>", konvertuj_u_dolar)


button1 = Button(window, text="Restartuj", width=30, height=3, font=("Arial", 15), command=restart)
button1.pack()


window.mainloop()