def month_to_season(n):
    if (n > 12):
        print("Такого месяца не существует!")
    elif (n == 12) or (n == 1) or (n == 2):
        print("Зима")
    elif (n == 3) or (n == 4) or (n == 5):
        print("Весна")
    elif (n == 6) or (n == 6) or (n == 8):
        print("Лето")
    else:
        print("Осень")

month_to_season((int(input("Введите число месяца: "))))