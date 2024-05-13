import mymodule

name = input("Введите ваше имя: ")
mymodule.greet(name)
side_length = float(input("Введите длину стороны квадрата: "))
area = mymodule.calculate_square_area(side_length)
print("Площадь квадрата:", area)
mymodule.module_description()
