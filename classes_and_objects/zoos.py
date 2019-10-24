class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.birds = []
        self.mammals = []
        self.fish = []

    def get_animals_by_species(self, species):
        animals = []
        if species == 'mammal':
            animals = self.mammals
        elif species == 'fish':
            animals = self.fish
        elif species == 'bird':
            animals = self.birds
        return animals

    def add_animal(self, species, animal):
        animals = self.get_animals_by_species(species)
        animals.append(animal)
        self.__animals += 1

    def get_info(self, species):
        animals = self.get_animals_by_species(species)
        print(animals)
        print(self.__animals)


zoo = Zoo(input())

animals_count = int(input())

for _ in range(animals_count):
    [species, animal] = input().split(' ')
    zoo.add_animal(species, animal)

species = input()

zoo.get_info(species)