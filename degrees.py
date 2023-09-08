from tkinter import *
from tkinter import messagebox

def validacija_c(P):
    if P == "" or P == "-":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def validacija_f(P):
    if P == "" or P == "-":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False


def konverzija_u_celzijus(*args):
    try:
        vrijednost_farenhajta = float(unos_farenhajta.get())
        vrijednost_celzijusa = round((vrijednost_farenhajta - 32) / 1.8, 2)
        unos_celzijusa.delete(0, END)
        unos_celzijusa.insert(0, vrijednost_celzijusa)
    except ValueError:
        pass
def konverzija_u_farenhajt(*args):
    try:
        cv = float(unos_celzijusa.get())
        fv = round((cv * 1.8) +32, 2)
        unos_farenhajta.delete(0, END)
        unos_farenhajta.insert(0, fv)
    except ValueError:
        pass

def restartuj():
    unos_farenhajta.delete(0, END)
    unos_celzijusa.delete(0, END)



window = Tk()
window.geometry("1000x500")
frame = Frame(window)
frame.pack(pady=30)

celzijus = Label(frame, text="°C", font=("Arial", 15))
celzijus.grid(row=0, column=0)
validacija_celzijusa = window.register(validacija_c)
unos_celzijusa = Entry(frame, validate="key", validatecommand=(validacija_celzijusa, "%P"))
unos_celzijusa.grid(row=0, column=1)
unos_celzijusa.bind("<KeyRelease>", konverzija_u_farenhajt)

farenhajt = Label(frame, text="°F", font=("Arial", 15))
farenhajt.grid(row=0, column=2)
validacija_farenhajta = window.register(validacija_f)
unos_farenhajta = Entry(frame, validate="key", validatecommand=(validacija_farenhajta, "%P"))
unos_farenhajta.grid(row=0, column=3)
unos_farenhajta.bind("<KeyRelease>", konverzija_u_celzijus)


button = Button(window, text="Restart", command=restartuj, width=30, height=2, font=("Arial", 15))
button.pack()







window.mainloop()
