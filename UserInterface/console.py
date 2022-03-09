from Service.restaurantservice import restaurantservice
from Service.reviewservice import reviewservice


class console():
    def __init__(self,
                 Restaurantservice: restaurantservice,
                 Reviewservice: reviewservice):
        self.Restaurantservice = Restaurantservice
        self.Reviewservice = Reviewservice

    def RunMenu(self):
        while True:
            print('1. Adauga restaurant')
            print('a1. Afiseaza restaurant')
            print('2. Adauga review')
            print('a2. Afiseaza review')
            print('3. Ordonare restaurante vegetariene in ordine alfabetica')
            print('4. Nota')
            print('5. Export Json')
            optiune = input('dati optiunea: ')
            if optiune == '1':
                self.uicerinta1()
            if optiune == 'a1':
                self.afisare(self.Restaurantservice.getall())
            if optiune == '2':
                self.uicerinta2()
            if optiune == 'a2':
                self.afisare(self.Reviewservice.getall())
            if optiune == '3':
                self.uicerinta3()
            if optiune == '4':
                self.uicerinta4()
            if optiune == '5':
                self.Json()

    def uicerinta1(self):
        try:
            id = input('dati id ul: ')
            nume = input('dati numele: ')
            adresa = input('dati adresa: ')
            vegetarian = input('vegetarian?')
            self.Restaurantservice.adauga(id, nume, adresa, vegetarian)
        except Exception as e:
            print(e)

    def afisare(self, entitati):
        for entitate in entitati:
            print(entitate)

    def uicerinta2(self):
        try:
            id = input('dati id ul')
            numeclient = input('dati numele clientului')
            idrestaurant = input('dati id ul restaurantului')
            comentariu = input('dati comentariu')
            nota = int(input('dati nota'))
            self.Reviewservice.adauga(id, numeclient, idrestaurant, comentariu, nota)
        except Exception as e:
            print(e)

    def uicerinta3(self):
        entitati = self.Restaurantservice.cerinta3()
        for entitate in entitati:
            print(entitate)

    def uicerinta4(self):
        entitati = self.Reviewservice.cerinta4()
        for entitate in entitati:
            print(entitate)

    def Json(self):
        try:
            filename = input("Dati numele fisierului in care se "
                             "va face exportul: ")
            self.Reviewservice.Json(filename)
        except Exception as e:
            print(e)

