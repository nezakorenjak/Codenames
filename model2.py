#Tukaj bodo konstante 
# 
# codenames_bazen.txt


import random
import time

def vsebuje(matrika, n):
    for i in matrika:
            for j in i:
                if j == n:
                    return True
    return False


class Ekipa:

    def __init__(self, ime_ekipe, govorec, ugibalec):
        self.ime_ekipe = ime_ekipe
        self.govorec = govorec
        self.ugibalec = ugibalec

class Igra:

    def __init__(self, matrika, polje, ekipe):
        self.matrika = matrika         #to vidita le govorca
        self.polje = polje             #to je polje besed
        self.ekipe = ekipe
        self.ekipa_na_potezi = 1

    def zamenjaj_ekipo(self):
        if self.ekipa_na_potezi == 1:
            self.ekipa_na_potezi = 2
        elif self.ekipa_na_potezi == 2:
            self.ekipa_na_potezi = 1

    def konec(self):
        if vsebuje(matrika, 1) and vsebuje(matrika, 2):
            return 0
        elif vsebuje(matrika, 1) and not vsebuje(matrika, 2):
            return 2
        elif vsebuje(matrika, 2) and not vsebuje(matrika, 1):
            return 1
        else:
            return 0 #morda kaj drugega, če bo do tega res prihajalo





    #def ugibaj(self, )


bazen_besed = []

with open('/home/neza/Namizje/CODENAMES/codenames_bazen.txt', 'r', encoding='utf-8') as besede:
    for beseda in besede.readlines():
        bazen_besed.append(beseda.upper().strip())


def nova_igra():

    random.seed(time.clock())
    
    polje = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            nova_beseda = random.choice(bazen_besed)
            polje[i][j] = nova_beseda
            bazen_besed.remove(nova_beseda)

    matrika = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    i, j = random.randint(0, 3), random.randint(0, 3)
    matrika[i][j] = 3

    n = 5
    while n > 0:
        k, l = random.randint(0, 3), random.randint(0, 3)
        if matrika[k][l] == 0:
            matrika[k][l] = 1
            n -= 1

    m = 5
    while m > 0:
        o, p = random.randint(0, 3), random.randint(0, 3)
        if matrika[o][p] == 0:
            matrika[o][p] = 2
            m -= 1

    ekipe = [Ekipa('veseliventilčki', 'matija', 'nina'), Ekipa('zvitefeltne', 'domen', 'janez')]

    return Igra(matrika, polje, ekipe)

igra = nova_igra()