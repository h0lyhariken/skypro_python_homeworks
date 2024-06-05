#Выведите на экран первый и последний элементы
#Первый вариант
lst = ["Виноград", "Персик", "Груша", "Апельсин", "Банан", "Яблоко"]
first_elem = lst[0]
last_elem = lst[5]
print(first_elem, last_elem)

#Второй вариант
first_fruit = lst[0]
last_fruit = lst[-1]
print(first_fruit, last_fruit)

#Нашел еще третий вариант
first = lst[0]
last = lst[len(lst) - 1]
print(first, last)