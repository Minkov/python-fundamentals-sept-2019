class Person:
    def __init__(self, first_name, middle_name, last_name, age = 0):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age

    def get_full_info(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} {self.age}'

def get_full_info(first_name, middle_name_1, last_name, age):
    return f'{first_name} {middle_name_1} {last_name} {age}'

p = Person('Gosho', 'Dimitrov', 1)

first_name_1 = 'Gosho'
middle_name_1 = 'Dimitrov'
last_name_1 = 'Dimitrov'
age_1 = 1
result = get_full_info(first_name_1, middle_name_1, last_name_1, age_1)
