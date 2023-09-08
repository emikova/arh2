from tkinter import *

def Izracunaj():
    unos_prvi = prvi_unos.get()
    unos_drugi = drugi_unos.get()
    unos_treci = treci_unos.get()
    unos_cetvrti = cetvrti_unos.get()
    unos_peti = peti_unos.get()
    unos_sesti = sesti_unos.get()

    dan = int(unos_cetvrti) - int(unos_prvi)
    mjesec = int(unos_peti) - int(unos_drugi)
    godina = int(unos_sesti) - int(unos_treci)

    sedmi_unos.delete(0, END)
    osmi_unos.delete(0, END)
    deveti_unos.delete(0, END)

    sedmi_unos.insert(0, abs(dan))
    osmi_unos.insert(0, abs(mjesec))
    deveti_unos.insert(0, abs(godina))
def Ponovi():
    prvi_unos.delete(0, END)
    drugi_unos.delete(0, END)
    treci_unos.delete(0, END)
    cetvrti_unos.delete(0, END)
    peti_unos.delete(0, END)
    sesti_unos.delete(0, END)
    sedmi_unos.delete(0, END)
    osmi_unos.delete(0, END)
    deveti_unos.delete(0, END)







window = Tk()
frame = Frame(window, width=1000, height=300)
frame.pack(pady=50)
tekst = Label(frame, text="Datum Rodjenja:",font=("System", 20))
tekst.grid(row=0, column=0)
prvi_unos = Entry(frame, width=5)
prvi_unos.grid(row=0, column=1)
drugi_unos = Entry(frame, width=5)
drugi_unos.grid(row=0, column=2)
treci_unos = Entry(frame, width=5)
treci_unos.grid(row=0, column=3)


novi_tekst = Label(frame, text="Trenutni datum:", font=("System", 20))
novi_tekst.grid(row=1, column=0)
cetvrti_unos = Entry(frame, width=5)
cetvrti_unos.grid(row=1, column=1)
peti_unos = Entry(frame, width=5)
peti_unos.grid(row=1, column=2)
sesti_unos = Entry(frame, width=5)
sesti_unos.grid(row=1, column=3)


izracunaj = Button(window, text="Izracunaj", command=lambda: Izracunaj())
izracunaj.pack()

novi_tekst = Label(window, text="Rezultat:", font=("System", 20))
novi_tekst.pack()
sedmi_unos = Entry(window, width=5)
sedmi_unos.pack()
osmi_unos = Entry(window, width=5)
osmi_unos.pack()
deveti_unos = Entry(window, width=5)
deveti_unos.pack()

ponovi = Button(window, text="Ponovi",command=lambda: Ponovi())
ponovi.pack()


window.mainloop()
