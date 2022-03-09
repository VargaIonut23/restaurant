import os

from Domain.restaurantvalidator import restaurantvalidator
from Domain.reviewvalidator import reviewvalidator
from Repository.json_repository import JsonRepository
from Service.restaurantservice import restaurantservice
from Service.reviewservice import reviewservice


def alltests():
    testcerinta1()
    testcerinta2()
    testcerinta3()
    testJson()

def clearFile(filename):
    with open(filename, "w") as f:
        pass


def testcerinta1():
    clearFile('restauranttest.json')
    restaurantrepository = JsonRepository('restauranttest.json')
    Restaurantvalidator = restaurantvalidator()
    Restaurantservice = restaurantservice(restaurantrepository,
                                          Restaurantvalidator)
    Restaurantservice.adauga('1', '1', '1', 'da')
    Restaurantservice.adauga('2', '2', '2', 'da')
    lista = Restaurantservice.repository.read()
    assert len(lista) == 2
    assert lista[0].id_entity == '1'
    assert lista[1].id_entity == '2'


def testcerinta2():
    clearFile('restauranttest.json')
    clearFile('reviewtest.json')
    restaurantrepository = JsonRepository('restauranttest.json')
    Restaurantvalidator = restaurantvalidator()
    Restaurantservice = restaurantservice(restaurantrepository,
                                          Restaurantvalidator)
    reviewrepository = JsonRepository('reviewtest.json')
    Reviewvalidator = reviewvalidator()
    Reviewservice = reviewservice(reviewrepository,
                                  Reviewvalidator,
                                  Restaurantservice)
    Restaurantservice.adauga('1', '1', '1', 'da')
    Restaurantservice.adauga('2', '2', '2', 'da')
    Reviewservice.adauga('1', '1', '1', '1', 10)
    Reviewservice.adauga('2', '2', '2', '2', 10)
    lista = Reviewservice.repository.read()
    assert len(lista) == 2
    assert lista[0].id_entity == '1'
    assert lista[1].id_entity == '2'

def testcerinta3():
    clearFile('restauranttest.json')
    restaurantrepository = JsonRepository('restauranttest.json')
    Restaurantvalidator = restaurantvalidator()
    Restaurantservice = restaurantservice(restaurantrepository,
                                          Restaurantvalidator)
    Restaurantservice.adauga('1', 'c', '1', 'da')
    Restaurantservice.adauga('2', 'a', '2', 'da')
    lista = Restaurantservice.cerinta3()
    assert len(lista) == 2
    assert lista[0].id_entity == '2'
    assert lista[1].id_entity == '1'

def testJson():
    clearFile('restauranttest.json')
    clearFile('reviewtest.json')
    restaurantrepository = JsonRepository('restauranttest.json')
    Restaurantvalidator = restaurantvalidator()
    Restaurantservice = restaurantservice(restaurantrepository,
                                          Restaurantvalidator)
    reviewrepository = JsonRepository('reviewtest.json')
    Reviewvalidator = reviewvalidator()
    Reviewservice = reviewservice(reviewrepository,
                                  Reviewvalidator,
                                  Restaurantservice)
    Restaurantservice.adauga('1', '1', '1', 'da')
    Restaurantservice.adauga('2', '2', '2', 'da')
    Reviewservice.adauga('1', '1', '1', '1', 10)
    Reviewservice.adauga('2', '2', '2', '2', 10)
    lista = Reviewservice.repository.read()

    Reviewservice.Json("test_export.json")

    assert os.path.isfile("test_export.json") is True
    clearFile("test_export.json")