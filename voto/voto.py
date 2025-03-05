from dataclasses import dataclass
import flet

cfuTot = 180

@dataclass
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool
    def __init__(self, materia, punteggio, data, lode):
        if punteggio == 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = lode
        elif punteggio < 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = False
        else:
            raise ValueError(f"Attenzione non posso creare un voto con punteggio {punteggio}")

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"


class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto):
        self.voti.append(voto)

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario}\n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente disponibile nel libretto
        :return: valore numerico della media, oppure ValueError in caso la lista fosse vuota
        """
        if len(self.voti) == 0:
            raise ValueError("Attenzione lista esami vuota!!")
        v = [v1.punteggio for v1 in self.voti] # TUTTI I VOTI DI OGNI ESAME
        return sum(v)/len(v)

    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con punteggio uguale a punti (e lode se punti == 30)
        :param punti: una variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se è presente la lode
        :return: lista di voti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)
        return votiFiltrati

    def getVotoByName(self, nome):
        """
        restituisce un oggetto Voto il cui campo materia è uguale a nome
        :param nome: una variabile di tipo stringa che corrisponde al nome della materia
        :return: oggetto di tipo Voto, oppure Non in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v

# VECCHIO CODICE
#class Voto:
    # def __init__(self, materia, punteggio, data, lode):
    #     if punteggio == 30:
    #         self.materia = materia
    #         self.punteggio = punteggio
    #         self.data = data
    #         self.lode = lode
    #     elif punteggio < 30:
    #         self.materia = materia
    #         self.punteggio = punteggio
    #         self.data = data
    #         self.lode = False
    #     else:
    #         raise ValueError(f"Attenzione non posso creare un voto con punteggio {punteggio}")
    #
    # def __str__(self):
    #     if self.lode:
    #         return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
    #     else:
    #         return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

def testVoto():
    print("Ho usato voto in maniera StandAlone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", True)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)

    myLib = Libretto(None, [v1, v2])
    myLib.append(v3)
    print(myLib)
    print(flet.Text(myLib.proprietario))

if __name__ == "__main__":
    testVoto()