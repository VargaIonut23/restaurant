import jsonpickle

from Domain.review import review
from Domain.reviewvalidator import reviewvalidator
from Repository.repository import Repository
from Service.restaurantservice import restaurantservice


class reviewservice():
    def __init__(self,
                 repository: Repository,
                 Reviewvalidator: reviewvalidator,
                 Restaurantservice: restaurantservice):
        self.repository = repository
        self.Reviewvalidator = Reviewvalidator
        self.Restaurantservice = Restaurantservice

    def adauga(self, id, numeclient, idrestaurant, comentariu, nota):
        if self.Restaurantservice.repository.read(idrestaurant) is None:
            raise ValueError('id ul clientului trb sa existe')
        Review = review(id, numeclient, idrestaurant, comentariu, nota)
        self.Reviewvalidator.valideaza(Review)
        self.repository.create(Review)

    def getall(self):
        return self.repository.read()

    def cerinta4(self):
        lista = {}
        lista1 = {}
        lista2 = []
        for review in self.repository.read():
            restaurant = self.Restaurantservice.repository.read(review.idrestaurant)
            lista1[restaurant.nume] = 0
            lista[restaurant.nume] = 0
        for review in self.repository.read():
            restaurant = self.Restaurantservice.repository.read(review.idrestaurant)
            lista1[restaurant.nume] += int(review.nota)
            lista[restaurant.nume] += 1
        for restaurant in self.Restaurantservice.repository.read():
            a = int(lista1[restaurant.nume])
            b = int(lista[restaurant.nume])
            c = a / b
            lista2.append({'nume': restaurant.nume,
                           'nota': c})
        return lista2

    def Json(self, filename):
        lista = {}
        for restaurant in self.Restaurantservice.repository.read():
            lista[restaurant.nume] = []
        for review in self.repository.read():
            restaurant = self.Restaurantservice.repository.read(review.idrestaurant)
            lista[restaurant.nume].append(review.comentariu)
        lista1 = []
        for x in lista:
            lista1.append({'nume': x,
                          'comentarii': lista[x]})
        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(lista1))
