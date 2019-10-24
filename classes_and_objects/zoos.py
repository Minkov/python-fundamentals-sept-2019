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

    def get_species_plural(self, singular):
        if singular == 'mammal':
            return 'Mammals'
        elif singular == 'fish':
            return 'Fishes'
        else:
            return 'Birds'

    def add_animal(self, species, animal):
        animals = self.get_animals_by_species(species)
        animals.append(animal)
        self.__animals += 1

    def get_info_by_species(self, species):
        animals = self.get_animals_by_species(species)
        return f'{self.get_species_plural(species)} in {self.name}: {", ".join(animals)}'

    def get_info_animals(self):
        return f'Total animals: {self.__animals}'

    def get_info(self, species):
        return self.get_info_by_species(species) + '\n' + \
               self.get_info_animals()


zoo = Zoo(input())

animals_count = int(input())

for _ in range(animals_count):
    [species, animal] = input().split(' ')
    zoo.add_animal(species, animal)

species = input()

print(zoo.get_info(species))
