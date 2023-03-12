from animals import AnimalsInZoo


class listOfAnimals(AnimalsInZoo):
    def __init__(self, name, weight, height, numOfPlace, noise):
        super().__init__(name, weight, height, numOfPlace, noise)
        self.name = name


kanarek1 = listOfAnimals("kanarek", 0.5, 0.10, 1, "I am kanarek")
kanarek1.make_noise()

Lew1 = listOfAnimals("lew", 500, 1.50, 2, "I am lew")
Lew1.make_noise()

orzeł1 = listOfAnimals("orzeł", 400, 1.50, 3, "I am orzeł")
orzeł1.make_noise()

sójka1 = listOfAnimals("sójka", 0.5, 0.10, 4, "I am sójka")
sójka1.make_noise()

ślimak1 = listOfAnimals("slimak", 0.1, 0.1, 5, "I am slimak")
ślimak1.make_noise()

wąż1 = listOfAnimals("wąż", 0.1, 0.30, 6, "I am wąż")
wąż1.make_noise()

boa1 = listOfAnimals("boa", 0.1, 0.1, 7, "I am boa")
boa1.make_noise()

antylopa1 = listOfAnimals("antylopa", 300, 1.80, 8, "I am antylopa")
antylopa1.make_noise()

żaba1 = listOfAnimals("żaba", 0.1, 0.1, 9, "I am żaba")
żaba1.make_noise()

chrząszcz1 = listOfAnimals("chrząszcz", 200, 1.1, 10, "I am chrząszcz")
chrząszcz1.make_noise()

modliszka1 = listOfAnimals("modliszka", 50, 1.1, 11, "I am modliszka")
modliszka1.make_noise()

sum1 = listOfAnimals("sum", 50, 1.1, 12, "I am sum")
sum1.make_noise()

rekin1 = listOfAnimals("rekin", 0.1, 0.1, 13, "I am rekin")
rekin1.make_noise()
