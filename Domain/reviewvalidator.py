class reviewvalidator():
    def valideaza(self, review):
        erori = []
        if len(review.numeclient) == 0:
            erori.append('numele nu trb sa fie null')
        if erori:
            raise ValueError(erori)
