class Vlasnik:
    def __init__(self, ime, prezime, jmbg):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = jmbg

    def __str__(self):
        return f"Ime: {self._ime}, Prezime: {self._prezime}, JMBG: {self._jmbg}"

    def jmbg(self):
        return self._jmbg


    def ime_sadrzi(self,upit):
        ime_ok = self._ime.find(upit) != -1
        prezime_ok = self._prezime.find(upit) != -1
        return ime_ok or prezime_ok


class Stan:
    def __init__(self, m2, sprat):
        self._m2 = m2
        self._sprat = sprat
        self._vlasnik = None

    def __str__(self):
        return f"m^2: {self._m2}, Sprat: {self._sprat}"

    def vlasnik(self):
        return self._vlasnik

    def novi_vlasnik(self, novi):
        self._vlasnik = novi

    def povrsina(self):
        return self._m2


class Zgrada:
    def __init__(self, adresa, stanovi):
        self._adresa = adresa
        self._stanovi = stanovi

    def __str__(self):
        opis = []
        for stan in self._stanovi:
            opis.append(str(stan))
        opis = "\n\n".join(opis)
        return "{}\n ----\n{}\n---- {}\n".format(self._adresa, opis)

    def dodaj_stan(self,stan):
        self._stanovi.append(stan)

    def stanovi_vlasnika(self, upit):
        vlasnik_stanovi = {}
        for stan in self._stanovi:
            v = stan.vlasnik()
            if v != None and v.ime_sadrzi(upit):
                v_stanovi = vlasnik_stanovi.get(v._jmbg(), [])
                v_stanovi.append(stan)
                vlasnik_stanovi[v._jmbg()] = v_stanovi
        return vlasnik_stanovi





