class Person:


    #class attribute
    species = 'Human'

    def __init__(self, name):
        self.name = name

person1 = Person('Ivan')
person2 = Person('Mariq')

print(person1.species)
print((person2.species))


