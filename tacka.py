import math
class Tacka:
    broj_tacaka = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
        Tacka.broj_tacaka += 1

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)


    #cemu classmethod, ako se tacke unose kao integer-i, a zbog classmethoda se moraju unositi kao string
    # (samo kako bi klasa fromString pretvorila string "brojeve" u integer-e ??????????????)
    @classmethod
    def fromString(cls, string):
        x,y = string.split(",")
        return cls(int(x), int(y))

    @classmethod
    def broj_tacaka_f(cls, broj):
        cls.broj_tacaka += broj

    @staticmethod
    def rastojanje(a,b):
        x_osa = pow(a.x - b.x, 2)
        y_osa = pow(a.y - b.y, 2)
        rezultat = math.sqrt(x_osa + y_osa)
        return rezultat


#a = Tacka(3,5)
a =Tacka.fromString("5,10")
print(a)

b = Tacka.fromString("10,3")
print(b)
print(Tacka.rastojanje(a,b))

Tacka.broj_tacaka_f(10)
print(Tacka.broj_tacaka)