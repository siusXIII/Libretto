

class Person:
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome # PREFERIREI CHE NON SI ACCEDESSE A QUESTA VARIABILE
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None # QUESTA VARIABILE NON VOGLIO CHE VENGA USATA, É POSSIBILE ACCEDERCI, MA É PIÙ DIFFICILE
        self.incantesimo = incantesimo

    def __str__(self):
        return f"Person: {self.nome} {self._cognome} \n"

    @property # DECORATORE
    def cognome(self): # EQUIVALE AL GETTER
        return self._cognome

    @cognome.setter
    def cognome(self, cognome): # EQUIVALE AL SETTER
        self._cognome = cognome

class Student(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self): # EQUIVALE AL toString()
        return f"Student: {self.nome} - {self._cognome} - {self.casa} \n "

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

    def prettyPrint(self):
        print("Voglio stampare meglio")

    def copy(self):
        return Student(self.nome, self.cognome, self.eta, self.capelli, self.occhi, self.casa, self.animale, self.incantesimo)

class Teacher(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia
    def __str__(self):
        return f"Teacher: {self.nome} - {self._cognome} - {self.materia} \n "

class Casa:
    def __init__(self, nome, studenti = [] ):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente) # --> [ x,x,x [s1, s2]]
        #self.studenti.extend(studente) # --> [ x,x,x, s1, s2 ]

    def __str__(self):
        if len(self.studenti) == 0:
            return f"La casa {self.nome} è vuota."

        mystr = f"\nLista degli studenti iscritti alla casa {self.nome}\n "
        for s in self.studenti:
            mystr += str(s)

        return mystr

class Scuola:
    def __init__(self, case):
        self.case = case

    def __str__(self): # DELEGA LA DESCRIZIONE DELLA CASA ALLA CLASSE Casa
        mystr = ""
        for c in self.case:
            mystr += str(c)
        return mystr