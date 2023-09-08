from tkinter import *

def Konvertovanje():

    if unos_dolara.get():
        usd = float(unos_dolara.get())
        km = usd * 1.8 + 32
        unos_marke.delete(0, END)
        unos_marke.insert(0, km)
    elif unos_marke.get():
        km = float(unos_marke.get())
        usd = (km - 32) / 1.8
        unos_dolara.delete(0, END)
        unos_dolara.insert(0, usd)



window = Tk()
window.geometry("1000x500")
window.title("USD - KM")
window.configure(bg="lightgray")

frame = Frame(window)
frame.pack(pady=40)
frame.configure(bg="lightgray")

dolar = Label(frame, text="C:", font=("System", 20), bg="lightgray")
dolar.grid(row=0, column=0)
unos_dolara = Entry(frame, font=("System", 20))
unos_dolara.grid(row=0, column=1)

marke = Label(frame, text="F:", font=("System", 20), bg="lightgray")
marke.grid(row=0, column=2, padx=15)
unos_marke = Entry(frame, font=("System", 20))
unos_marke.grid(row=0, column=3)

konvertuj = Button(window, text="Konvertuj", font=("System", 20), command= lambda: Konvertovanje())
konvertuj.pack()


window.mainloop()