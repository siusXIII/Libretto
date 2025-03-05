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
mylib.append(Voto("Pozioni", 21, "2022-06-14", False))
print(mylib)

#2)
print("2) Calcola media")
print(mylib.calcolaMedia())
#3)
print("3) Voti con un certo punteggio")
votiFiltrati = mylib.getVotiByPunti(21, False)
print("Esami con 21")
for v in votiFiltrati:
    print(v)

#4)
print("4) Voto di un certo esame")
votoPozioni = mylib.getVotoByName("Pozioni")
if votoPozioni is None:
    print("Voto non trovato!")
else:
    print(votoPozioni)