def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 5 == 0 and x % 5 == 0:
            print("FizzBuzz")      
        else:
            print(x)
fizz_buzz((int(input("Введите целое число: "))))