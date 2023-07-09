

class Rectangle:

    def __init__(self, length, wigth):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def resize(self,new_length, new_widgth):
        self.lengt = new_length
        self.width = new_widgth


rect = Rectangle(4, 5)

area = rect.calculate_area()
print(area)

rect.resize(6, 7)
print(rect.calculate_area())