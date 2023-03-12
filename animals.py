class AnimalsInZoo:
    def __init__(self, name, weight, height, numOfPlace, noise):
        self.weight = weight
        self.height = height
        self.numOfPlace = numOfPlace
        self.noise = noise
        self.lenght = 100
        self.name = name

    def make_noise(self):
        print("I am ", self.name)
        print("My weight ", self.weight)
        print("My height is ", self.height)
        print("You can find me on the place ", self.numOfPlace)
