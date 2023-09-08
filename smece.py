from random import randrange
n = int(input("Unesi n:"))
while n < 3:
    n = int(input("Unesi n:"))

matrica = []
for i in range(n):
    red = []
    for j in range(n):
        element = randrange(-20, 21)
        red.append(element)
    matrica.append(red)

print(matrica)

file = open("tekst.txt", "w")
for red in matrica:
    file.write(",".join(map(str, red)) + "\n")

kolona = 2
maksimum = 0
for i in range(n):
    if matrica[i][kolona] > maksimum:
        maksimum = matrica[i][kolona]
print(maksimum)


suma = 0
i = 0
j = n -1

while i < n and j >= 0:
    suma += matrica[i][j]
    i += 1
    j -= 1
av = float(suma/n)
#print(av)

brojac = 0
for i in range(n):
    for j in range(n):
        if matrica[i][j] > av:
            brojac += 1
#print(brojac)

proizvod = 1
i = 0
j = 0
while i < n and j < n:
    if matrica[i][j] % 3 == 0:
        proizvod *= matrica[i][j]
    i += 1
    j += 1
#print(proizvod)

brojac1 = 0
for i in range(n):
    for j in range(n):
        if matrica[i][j] < 0:
            brojac1 += 1
#print(brojac1)

zbir = 0
red = 2
for j in range(n):
    if matrica[red][j] == -3:
        zbir += matrica[red][j]
#print(zbir)


novi_fajl = open("izmjenjeno.txt", "w")
novi_fajl.write("Najveci broj u trecoj koloni je:")
novi_fajl.write(str(maksimum))
novi_fajl.write("\n")
novi_fajl.write("Broj elemenata vecih od prosjeka elemenata na sporednoj dijagonali je:")
novi_fajl.write(str(brojac))
novi_fajl.write("\n")
novi_fajl.write("Proizvod elemenata djeljivih sa 3 na glavnoj dijagonali:")
novi_fajl.write(str(proizvod))
novi_fajl.write("\n")
novi_fajl.write("Broj negativnih elemenata: ")
novi_fajl.write(str(brojac1))
novi_fajl.write("\n")
novi_fajl.write("Zbir brojeva jednakih -3 :")
novi_fajl.write(str(zbir))

file.close()
novi_fajl.close()