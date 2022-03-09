from Domain import restaurantvalidator
from Domain.restaurant import restaurant
from Repository.repository import Repository


class restaurantservice():
    def __init__(self,
                 repository: Repository,
                 Restaurantvalidator: restaurantvalidator):
        self.repository = repository
        self.Restaurantvalidator = Restaurantvalidator

    def adauga(self, id, nume, adresa, vegetarian):
        if vegetarian == "da":
            vegetarian = True
        elif vegetarian == "nu":
            vegetarian = None
        else:
            raise ValueError("vegetarian trebuie sa fie da sau nu")
        Restaurant = restaurant(id, nume, adresa, vegetarian)
        self.Restaurantvalidator.valideaza(Restaurant)
        self.repository.create(Restaurant)

    def getall(self):
        return self.repository.read()

    def cerinta3(self):
        lista = []
        for restaurant in self.repository.read():
            if restaurant.vegetarian is True:
                lista.append(restaurant)
        return sorted(lista, key=lambda x: x.nume)
