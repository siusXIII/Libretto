from scuola.scuola import Student
from voto.voto import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
mylib =Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 24, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-17", False)

#1)
print("1) Aggiungi Voti")
mylib.append(v1)
mylib.append(v2)
mylib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))
mylib.append(Voto("Pozioni", 21, "2022-06-14", False))
print(mylib)


print("Calcola media")
print(mylib.calcolaMedia())

#2)
print("\n2) Voti con un certo punteggio")
votiFiltrati = mylib.getVotiByPunti(21, False)
print("Esami con 21")
for v in votiFiltrati:
    print(v)

#3)
print("\n3) Voto di un certo esame")
votoPozioni = mylib.getVotoByName("Pozioni")
if votoPozioni is None:
    print("Voto non trovato!")
else:
    print(votoPozioni)

#4)
print("\n4) Voto nel libretto")
print(mylib.hasVoto(v1)) # ANCHE print(Voto("Difesa contro le arti oscure", 24, "2022-01-30", False))
print(mylib.hasVoto(Voto("Aritmazia", 30, "2023-07-10", False)))

#5)
print("\n5) Voto in conflitto")
print(mylib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)))

#6)
print("\n6) append modificata")
mylib.append(Voto("Aritmazia", 30, "2023-07-10", False)) # OK
# mylib.append(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)) # ERRORE
mylib.append(Voto("Divinazione", 25, "2021-02-08", False))
mylib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))

#7)
print("Libretto migliorato")
print(f"Libretto normale:\n {mylib}")
print(f"Libretto migliorato:\n {mylib.creaMigliorato()}")

#8)
print("Libretto ordinati")

print("Libretto ordinato per materia:\n", mylib.creaLibOrdinatoPerMateria())
print("Libretto ordinato per voto:\n", mylib.creaLibOrdinatoPerVoto())

#9)
print("Libretto >= 24")
ordinato = mylib.creaLibOrdinatoPerVoto()
ordinato.cancellaInferiori(24)
print("Libretto con voti >= 24", ordinato)