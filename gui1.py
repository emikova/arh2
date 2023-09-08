from tkinter import *
import random

def Pobjednik(izbor):

    lista = ["Kamen", "Papir", "Makaze"]
    racunar = random.choice(lista)
    print(racunar)

    if (racunar == "Kamen" and izbor == "Makaze") or (racunar == "Papir" and izbor == "Kamen") or (racunar == "Makaze" and izbor == "Papir"):
        unos.delete(0, END)
        unos.insert(0, "Racunar pobjedjuje")
    elif (izbor == "Makaze" and racunar == "Papir") or (izbor == "Kamen" and racunar == "Makaze") or (izbor == "Papir" and racunar == "Kamen"):
        unos.delete(0, END)
        unos.insert(0, "Igrac pobjedjuje")
    else:
        unos.delete(0, END)
        unos.insert(0, "Nerjeseno")


def Ponovi():
    unos.delete(0, END)

window = Tk()
window.geometry("500x500")

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()
frame4 = Frame(window)
frame4.pack()

text = Label(frame1, text="Kamen Papir Makaze", font=("System", 20), fg="blue")
text.grid(row=0, column=0)

igrac = Label(frame2, text="Igrac", font=("System", 15))
igrac.grid(row=0, column=0)
vs = Label(frame2, text="vs", font=("System", 15))
vs.grid(row=0, column=1)
Racunar = Label(frame2, text="Racunar", font=("System", 15))
Racunar.grid(row=0, column=2)

unos = Entry(frame3, width=20, font=("System", 20))
unos.grid(pady=15)

kamen = Button(frame4, text="Kamen", font=("System", 15),command=lambda :Pobjednik("Kamen"))
kamen.grid(row=0, column=0, padx=10)
papir = Button(frame4, text="Papir", font=("System", 15), command=lambda :Pobjednik("Papir"))
papir.grid(row=0, column=1, padx=10)
makaze = Button(frame4, text="Makaze", font=("System", 15), command=lambda :Pobjednik("Makaze"))
makaze.grid(row=0, column=2, padx=10)

ponovi = Button(window, text="Ponovi", font=("System", 15), bg="black", fg="red", command= lambda: Ponovi())
ponovi.pack(pady=15)


izbor_kompjutera = ""


window.mainloop()