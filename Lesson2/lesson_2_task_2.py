def is_year_leap(year):
    if (year % 4 == 0):
        print("Год: " + str(year) + " True")
    else:
        print ("Год: " + str(year) + " False")
    return(year)

is_year_leap(int(input("Введите год: ")))
