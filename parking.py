class ParkingTicket:
    def __init__(self, naziv_parkinga, cijena_po_satu, broj_sati):
        self.naziv_parkinga = naziv_parkinga
        self.cijena_po_satu = cijena_po_satu
        self.broj_sati = broj_sati

    def __str__(self):
        return f"{self.naziv_parkinga} - {self.cijena_po_satu * self.broj_sati}"

    def __le__(self, other):
        return (self.cijena_po_satu * self.broj_sati) <= (other.cijena_po_satu * other.broj_sati)

    def __lt__(self, other):
        return (self.cijena_po_satu * self.broj_sati) < (other.cijena_po_satu * other.broj_sati)

    def __repr__(self):
        return f"ParkingTicket({self.naziv_parkinga},{self.cijena_po_satu * self.broj_sati})"

    @classmethod
    def from_string(cls,string):
        naziv_parkinga, cijena_po_satu, broj_sati = string.split(",")
        return cls(naziv_parkinga, float(cijena_po_satu), int(broj_sati))

Borik = []

with open("parking.txt", "r") as file:
    for line in file:
        if line.startswith("Borik,"):
            b = ParkingTicket.from_string(line.strip())
            Borik.append(b)


print(Borik)

sortiran_parking = sorted(Borik, reverse=True)

for ticket in Borik:
    print(ticket)


