import re

fajl = open("ulaz.txt", "r")
tekst = fajl.read()
datumi = re.findall(r'(\d+.\d+.\d+.)', tekst)

i = 0
lista = []
while i < len(datumi):
    #print(datumi[i][1])
    novi_datumi = int( datumi[i][1]) + 1
    lista.append(novi_datumi)
    i += 1
#print(lista)

nova_lista = list(map(str, lista))
print(nova_lista)

pozicija = 1
for i in range(len(datumi)):
    brojna_lista = list(datumi[i])
    brojna_lista[pozicija] = nova_lista[i]
    novi_broj = "".join(brojna_lista)

    datumi[i] = novi_broj




