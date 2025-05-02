#1
class Rectangular:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def area(self):
        print(self.width * self.hight)

    def perimeter(self):
        print(self.width * 2 + self.hight * 2)

object_1 = Rectangular(4, 5)
object_1.area(), object_1.perimeter()

object_2 = Rectangular(3, 1)
object_2.area(), object_2.perimeter()

object_3 = Rectangular(6, 2)
object_3.area(), object_3.perimeter()

#2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

variables = Math(4,3)
variables.addition(), variables.multiplication()
variables.division(), variables.subtraction()

#3
class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)
button_1 = Button("Text Box", "Кнопка", "")
button_2 = Button("Check Box", "Кнопка", "")
button_3 = Button("Radio Button", "Кнопка", "")
button_4 = Button("Web Tables", "Кнопка", "")
button_5 = Button("Buttons", "Кнопка", "")
button_6 = Button("Links", "Кнопка", "")
button_7 = Button("Broken Links - Images", "Кнопка", "")
button_8 = Button("Upload and Download", "Кнопка", "")
button_9 = Button("Dynamic Properties", "Кнопка", "")
print(button_1.text)
print(button_1.click())
print(button_2.text)
print(button_2.click())
print(button_3.text)
print(button_3.click())
print(button_4.text)
print(button_4.click())
print(button_5.text)
print(button_5.click())
print(button_6.text)
print(button_6.click())
print(button_7.text)
print(button_7.click())
print(button_8.text)
print(button_8.click())
print(button_9.text)
print(button_9.click())
