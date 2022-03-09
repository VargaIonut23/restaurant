from Domain.restaurantvalidator import restaurantvalidator
from Domain.reviewvalidator import reviewvalidator
from Repository.json_repository import JsonRepository
from Service.restaurantservice import restaurantservice
from Service.reviewservice import reviewservice
from UserInterface.console import console
from tests.alltests import alltests


def main():
    alltests()
    restaurantrepository = JsonRepository('restaurant.json')
    Restaurantvalidator = restaurantvalidator()
    Restaurantservice = restaurantservice(restaurantrepository,
                                          Restaurantvalidator)
    reviewrepository = JsonRepository('review.json')
    Reviewvalidator = reviewvalidator()
    Reviewservice = reviewservice(reviewrepository,
                                  Reviewvalidator,
                                  Restaurantservice)
    Console = console(Restaurantservice, Reviewservice)
    Console.RunMenu()


if __name__ == '__main__':
    main()
