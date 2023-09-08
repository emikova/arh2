class Predstava:
    def __init__(self, naziv_predstave, broj_posjetioca, cijena_karte):
        self.naziv_predstave = naziv_predstave
        self.broj_posjetioca = broj_posjetioca
        self.cijena_karte = cijena_karte

    def __str__(self):
        return f"{self.naziv_predstave} - {self.broj_posjetioca} - {self.cijena_karte}"

    def __le__(self, other):
        return self.broj_posjetioca * self.cijena_karte <= other.broj_posjetioca * other.cijena_karte

    def __lt__(self, other):
        return self.broj_posjetioca * self.cijena_karte < other.broj_posjetioca * other.cijena_karte

    def __repr__(self):
        return f"Predstava({self.naziv_predstave}-{self.broj_posjetioca}-{self.cijena_karte})"


    @classmethod
    def from_string(cls, string):
        naziv_predstave, broj_posjetioca, cijena_karte = string.split(",")
        return cls(naziv_predstave, int(broj_posjetioca), float(cijena_karte))






predstave = []
with open("predstava.txt", "r") as file:
    for line in file:
        predstava = Predstava.from_string(line.strip())
        predstave.append(predstava)

print(predstave)

sortirane_predstave = sorted(predstave, reverse=True)

for predstava in sortirane_predstave:
    print(predstava)
najposjecenija = max(predstave, key=lambda x: x.broj_posjetioca)
print("Najposjecenija predstava je:", {najposjecenija})