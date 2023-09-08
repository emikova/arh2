from tkinter import *
import random

class Vjesala:

    def __init__(self, window):
        self.window = window
        self.window.title("Igra Vjesala")

        self.rijeci = self.ucitaj_rijeci()
        self.rijec = ""
        self.broj_pogadjanja = 6

        self.label_rijec = Label(window, text="", font=("System", 20))
        self.label_rijec.pack(pady=10)

        self.label_broj_pogadjanja = Label(window, text="Broj pogadjanja: 6", font=("System", 20))
        self.label_broj_pogadjanja.pack()

        self.entry_karakter = Entry(window, font=("System", 18))
        self.entry_karakter.pack(pady=10)

        self.button_ispitaj = Button(window, text="Ispitaj", font=("System",20), command=self.ispitaj_karakter)
        self.button_ispitaj.pack()

        self.button_nova_igra = Button(window, text="Nova Igra", font=("System", 20), command=self.nova_igra)
        self.button_nova_igra.pack(pady=20)

        self.nova_igra()


    def ucitaj_rijeci(self):
        with open("rijeci.txt", "r") as file:
            rijeci = [line.strip() for line in file.readlines()]
        return rijeci


    def nova_igra(self):
        self.rijec = random.choice(self.rijeci)
        self.broj_pogadjanja = 6

        self.label_rijec.config(text="_ " * len(self.rijec))
        self.label_broj_pogadjanja.config(text=f"Broj pogadjanja:{self.broj_pogadjanja}")

    def ispitaj_karakter(self):
        karakter = self.entry_karakter.get()
        if karakter in self.rijec:
            nova_rijec = ""
            for i in range(len(self.rijec)):
                if self.rijec[i] == karakter:
                    nova_rijec += karakter + " "
                else:
                    nova_rijec += self.label_rijec.cget("text")[i * 2] + " "
            self.label_rijec.config(text=nova_rijec)

            if "_" not in nova_rijec:
                self.label_broj_pogadjanja.config(text="Pogodili ste rijec!")
        else:
            self.broj_pogadjanja -= 1
            self.label_broj_pogadjanja.config(text=f"Broj pogadjanja:{self.broj_pogadjanja}")

            if self.broj_pogadjanja == 0:
                self.label_broj_pogadjanja.config(text="Igra je zavrsena.Niste pogodili rijec!")








window = Tk()
igra = Vjesala(window)

window.mainloop()