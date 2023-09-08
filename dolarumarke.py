from tkinter import *

def Konvertovanje():
    if unos_dolara.get():
        vrijednost_dolara = float(unos_dolara.get())
        vrijednost_u_KM = float(vrijednost_dolara * 1.83)
        unos_marke.delete(0, END)
        unos_marke.insert(0, vrijednost_u_KM)
    elif unos_marke.get():
        vrijednost_marke = float(unos_marke.get())
        vrijednost_u_USD = float(vrijednost_marke / 1.83)
        unos_dolara.delete(0, END)
        unos_dolara.insert(0, vrijednost_u_USD)


window = Tk()
frame = Frame(window)
frame.pack()


dolar = Label(frame,text="USD", font=20)
dolar.grid(row=0,column=0)
unos_dolara = Entry(frame, font=20)
unos_dolara.grid(row=0, column=1)

marka = Label(frame, text="KM", font=20)
marka.grid(row=0, column=2)
unos_marke = Entry(frame, font=20)
unos_marke.grid(row=0,column=3)

konvertuj  =Button(window, width=20, command=lambda :Konvertovanje())
konvertuj.pack()


window.mainloop()