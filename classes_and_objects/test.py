class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self, name):
        print(f"{self.name} says 'Hi' to {name}!")


gosho = Person('Gosho')
pesho = Person('Pesho')

print(gosho.__dict__)
print(pesho.__dict__)

gosho.name = 'George'
print('-' * 20)
print(gosho.__dict__)
print(pesho.__dict__)
