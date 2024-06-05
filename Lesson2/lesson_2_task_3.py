import math

def square(side):
    S = side * side
    return(S)

side = float(input("Введите длину стороны квадрата: "))
result = square(side)
rounded_result = math.ceil(result)
print("Округленная в большую сторону площадь квадрата:", rounded_result)
