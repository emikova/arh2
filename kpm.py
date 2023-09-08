from tkinter import *
import random

def pobjednik(izbor):
    global rezultat
    kompjuter = random.choice(["KAMEN", "PAPIR", "MAKAZE"])
    rezultat = ""

    if izbor == kompjuter:
        rezultat = "Nerijeseno"
    elif ((izbor == "KAMEN" and kompjuter == "MAKAZE") or (izbor == "MAKAZE" and kompjuter == "PAPIR") or (izbor == "PAPIR" or kompjuter == "KAMEN")):
        rezultat = "Igrac pobjedjuje!"
    else:
        rezultat = "Kompjuter pobjedjuje"

    entry.insert(0, rezultat)


def ponovi():
    global rezultat
    rezultat = ""
    entry.delete(0, END)


window = Tk()
window.geometry("1000x1000")


frame = Frame(window)
frame.pack(pady=40)
label1 = Label(frame, text="Igrac", font=("System", 15))
label1.grid(row=0 , column=0)
label2 = Label(frame, text="VS",font=("System", 15))
label2.grid(row=0, column=1)
label2 = Label(frame, text="Racunar",font=("System", 15))
label2.grid(row=0, column=2)
entry = Entry(window, width=40, font=("System", 20))
entry.pack()

frame1 = Frame(window)
frame1.pack(pady=20)
kamen = Button(frame1, width=10, height=3, text="KAMEN", font="System",command=lambda: pobjednik("KAMEN"))
kamen.grid(row=0, column=0)
papir = Button(frame1, width=10, height=3, text="PAPIR", font="System",command=lambda: pobjednik("PAPIR"))
papir.grid(row=0, column=1)
makaze = Button(frame1, width=10, height=3, text="MAKAZE", font="System", command=lambda: pobjednik("MAKAZE"))
makaze.grid(row=0 ,column=2)

restart = Button(window, width=40, height=3, text="PONOVI IGRU", bg="black", fg="white", font="System",command=lambda: ponovi())
restart.pack()

rezultat = ""


window.mainloop()