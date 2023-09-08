from tkinter import *

def Konverzija():
    if unos_farenhajta.get():
        f = float(unos_farenhajta.get())
        vrijednost_celzijusa = (f - 32) / 1.8
        unos_celzijusa.delete(0, END)
        unos_celzijusa.insert(0, vrijednost_celzijusa)
    elif unos_celzijusa.get():
        c = float(unos_celzijusa.get())
        vrijednost_farenhajta = (c * 1.8) +32
        unos_farenhajta.delete(0, END)
        unos_farenhajta.insert(0, vrijednost_farenhajta)


def Restartuj():
    unos_farenhajta.delete(0,END)
    unos_celzijusa.delete(0, END)

window = Tk()
window.geometry("800x500")
frame = Frame(window)
frame.pack()

farenhajt = Label(frame, text="°F", font=("System", 20))
farenhajt.grid(row=0, column=0)
unos_farenhajta = Entry(frame,font=("System",20))
unos_farenhajta.grid(row=0, column=1)

celzijus = Label(frame, text="°C", font=("System",20))
celzijus.grid(row=0, column=2)
unos_celzijusa = Entry(frame, font=("System",20))
unos_celzijusa.grid(row=0, column=3)

konvertuj = Button(window, text="Konvertuj", font=("System",20), command=lambda :Konverzija())
konvertuj.pack()

restart = Button(window, text="Restartuj", font=("System",20), command=lambda :Restartuj())
restart.pack()




window.mainloop()