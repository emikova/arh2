class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        return f"Ime: {self.ime} Prezime: {self.prezime}"


class Student1:
    def __init__(self, ime, prezime, broj_indeksa):
        Osoba.__init__(self,ime, prezime)
        self.broj_indeksa = broj_indeksa

    def __str__(self):
        return Osoba.__str__(self) + "\t" + f"Broj indeksa: {self.broj_indeksa}"


class Student2:
    def __init__(self, ime, prezime, broj_indkeksa):
        self.osoba = Osoba(ime, prezime)
        self.broj_indeksa= broj_indkeksa

    def __str__(self):
        return str(self.osoba) +"\t" + f"Broj indeksa: {self.broj_indeksa}"


class Student3:
    def __init__(self, osoba, broj_indeksa):
        self.osoba = osoba
        self.broj_indeksa = broj_indeksa


    def __str__(self):
        return str(self.osoba) + "\t" +f"Broj indeksa: {self.broj_indeksa}"



s1 = Student1("Jane", "Doe", "123/12")
print(s1)
s2 = Student2("Josh", "Braun", "1234/66")
print(s2)
s3 = Osoba("Mike","Delfino")
s2 = Student3(s3, "345/77")
print(s2)
