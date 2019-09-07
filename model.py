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
        self.matrika = matrika
        self.polje = polje
        self.ekipe = {1: ekipe[0], 2: ekipe[1]}
        self.ekipa_na_potezi = 1
        self.trenutna_asociacija = ''
        self.st_ugibov = 0

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
            return -1 #morda kaj drugega, če bo do tega res prihajalo

    def poteza_govorca(asociacija, st_ugibov):
        self.trenutna_asociacija = asociacija
        self.st_ugibov = st_ugibov
    
    def ugibaj(i, j):
        if self.matrika[i][j] == 3:
            print('BOMBA!')
            zamenjaj_ekipo()
            for i in range(4):
                for j in range(4):
                    if matrika[i][j] == self.ekipa_na_potezi:
                        matrika[i][j] = 0
            #KONEC IGRE BO
        elif self.matrika[i][j] == self.ekipa_na_potezi:
            self.matrika[i][j] = 0
            print('Bravo! Ugib je pravilen.')
        elif self.matrika[i][j] == 0:
            print('To polje je sivo.')
        else:
            self.matrika[i][j] = 0
            print('Nasprotniki se ti zahvaljujejo za pomoč.')
        self.st_ugibov -= 1


bazen_besed = []

with open('codenames_bazen.txt', 'r', encoding='utf-8') as besede:
    for beseda in besede.readlines():
        bazen_besed.append(beseda.upper().strip())


def nova_igra(e1_ime, e1_govorec, e1_ugibalec, e2_ime, e2_govorec, e2_ugibalec):

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


    ekipe = [Ekipa(e1_ime, e1_govorec, e1_ugibalec), Ekipa(e2_ime, e2_govorec, e2_ugibalec)]

    return Igra(matrika, polje, ekipe)


class Codenames:

    def __init__(self):
        self.igre = {}
        return

    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i 

    def nova_igra(self, e1_ime, e1_govorec, e1_ugibalec, e2_ime, e2_govorec, e2_ugibalec):
        igra = nova_igra(e1_ime, e1_govorec, e1_ugibalec, e2_ime, e2_govorec, e2_ugibalec)
        id = self.prost_id_igre()
        self.igre[id] = (igra)
        return id

    def ugibaj(self, id_igre, i, j):
        # Pridobi igro
        igra = self.igre[id_igre]
        igra.ugibaj(i, j)
        self.igre[id_igre] = igra
    
    def poteza_govorca(self, id_igre, asociacija, st_ugibov):
        igra = self.igre[id_igre]
        igra.poteza_govorca(asociacija, st_ugibov)
        self.igre[id_igre] = igra

        