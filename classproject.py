
class animal():
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    def talk(self):
        if self.name == 'cat':
            return 'meooo'
        else:
            return 'I am not a cat'

    def move(self):
        return f'{self.name} can run'

class animal_sub(animal):
    def __init__(self, name, colour, age, height):
        super().__init__(name, colour, age)
        self.height = height

class animal_sub1(animal):
    def off(self):
        return f'{self.name} can sleep'

data = animal_sub1('dog', 'black', '23 months')
print(data.off())