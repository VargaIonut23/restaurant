class restaurantvalidator():
    def valideaza(self, restaurant):
        erori = []
        if len(restaurant.nume) == 0:
            erori.append('numele nu trb sa fie null')
        if erori:
            raise ValueError(erori)
