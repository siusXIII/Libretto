import operator
from dataclasses import dataclass
import flet
from python.Lib.test.test_buffer import randslice_from_shape

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

    # def __eq__(self, other):
    #     return self.materia==other.materia and self.punteggio==other.punteggio and self.lode==other.lode

    def copy(self):
        """
        Crea una copia del voto
        :return: Istanza della classe Voto
        """
        return Voto(self.materia, self.punteggio, self.data, self.lode)

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto):
        if self.hasConflitto(voto) is False and self.hasVoto(voto) is False:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto è già presente")

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

    def hasVoto(self, voto):
        """
        Questo metodo verifica se il libretto contiene gia il voto "voto". Due voti sono considerati uguali per questo
        metodo se hanno lo stesso campo materia e lo stesso campo voto (voto è formato da punteggio e lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se il voto è già presente, False altrimenti
        """
        for v in self.voti:
            # MODO NUMERO 1 --> CONTROLLO DIRECTORY
            #if v==voto:
            #    pass
            # MODO NUMERO 2 --> VERIFICA SOLO I CAMPI   (CORRETTO)
            if v.materia == voto.materia and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def hasConflitto(self, voto):
        """
        Questo metodo controllo che il voto "voto" non rappresenti un conflitto con i voti già presenti nel libretto.
        Consideriamo due voti in conflitto quando hanno los tesso campo materia ma diversa coppia (voto, lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se il voto è in conflitto, False altrimenti
        """
        for v in self.voti:
            if v.materia == voto.materia and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False

    def copy(self):
        """
        Crea una nuova copia del libretto
        :return: istanza della classe Libretto
        """
        nuovo = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

    def creaMigliorato(self):
        """
        Crea un nuovo oggetto Libretto, in cui i voto sono migliorati seguendo la seguente logica:
        se il voto è >= 18 e < 24 aggiungo +1;
        se il voto è >= 24 e < 29 aggiungo +2;
        se il voto è 29 aggiungo +1;
        se il voto è 30 rimane 30.
        :return: Nuovo libretto
        """
        nuovo = self.copy()

        # MODIFICO I VOTI IN NUOVO
        for v in nuovo.voti:
            if 18 <= v.punteggio < 24 or v.punteggio == 29:
                v.punteggio += 1
            elif 24 <= v.punteggio < 29:
                v.punteggio += 2
        return nuovo

    # OPZIONI SORT
    # 1) CREO DUE METODI DI STAMPA CHE PRIMA ORDINANO E POI STAMPANO
    # 2) CREO DUE METODI CHE ORDINANO LA LISTA DI SELF E POI UN UNICO METODO DI STAMPA
    # 3) CREO DUE METODI CHE SI FANNO UNA COPIA AUTONOMA DELLA LISTA, LA ORDINANO E LA RESTITUISCONO. POI UN ALTRO
    #    SI OCCUPERÀ DI STAMPARE LE LISTE  ---> MIGLIORE
    # 4) CREO UNA SHALLOW COPY DI SELF.VOTI E ORDINO LA LISTA

    def sortByMateria(self):
        self.voti.sort(key=operator.attrgetter('materia')) #self.voti.sort(key=lambda x: x.materia)
        #self.voti.sort(key=estraiMateria)

    def creaLibOrdinatoPerMateria(self):
        """
        Crea un nuovo oggetto Libretto e lo ordina per materia
        :return: Nuova istanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        """
        Crea un nuovo oggetto Libretto e lo ordina per punteggio
        :return: Nuova istanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: (v.punteggio, v.lode), reverse=True)
        return nuovo

    def cancellaInferiori(self, punteggio):
        """
        Questo metodo agisce sul libretto corrente, eliminando tutti i voti inferiori al parametro indicato
        :param punteggio: intero indicante in valore minimo
        :return:
        """
        # nuovo = []
        # for v in self.voti:
        #     if v.punteggio >= punteggio:
        #         nuovo.append(v)
        nuovo = [v for v in self.voti if v.punteggio >= punteggio]
        self.voti = nuovo


# def estraiMateria(voto):
#     """
#     Questo metodo restituisce il campo materia dell'oggetto voto
#     :param voto: Istanza dell'oggetto di tipo Voto
#     :return: Stringa della materia
#     """
#     return voto.materia

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