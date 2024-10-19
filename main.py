print('Hello world!')

a = 2
b = 'hello'
c = True
d = 2.2


class Marker:
    def __init__(self, color='black'):
        self.color = color
        self.weight = 1.22
        self.price = 3
        self.isPresent = True

    def getinfo(self):
        print(f'color:{self.color}-price{self.price}€')

redMarker = Marker('red')
print(redMarker.color)
redMarker.getinfo()

blackMarker = Marker()
print(blackMarker.color)
blackMarker.getinfo()