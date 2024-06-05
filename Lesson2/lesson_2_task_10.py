def bank(X, Y):
    money = X
    for _ in range(Y):
        money = money * 1.1
    return(money)
    
X = float(input("Введите количество денег: "))
Y = int(input("Введите количество лет: "))
print(bank(X,Y))

