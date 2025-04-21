#1
def func(a, b):
    print(max(a, b))

func(243, 1)

#2
def comparison(a, b):
    if a - b == 135 or b - a == 135:
        print("yes")
    else:
        print("No")

comparison(2, 137)

#3
def season(month):
    if month == 1 or month == 2 or month == 12:
        print("winter")
    elif month in range(3,6):
        print("spring")
    elif month in range(6,9):
        print("summer")
    elif month in range(9,12):
        print("fall")

season(9)

#4
def func_3(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

func_3(23, 54, 3)
