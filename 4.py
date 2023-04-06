def f1():
    a = int(input("введите число"))
    if a % 3 == 0:
        print("число делится на 3")
    else:
        print("число не делится на 3")

def f2():
    try:
        a = int(input("введите число "))
        b = 100 / a
    except ValueError:
        print("нужны числа")
    except ZeroDivisionError:
        print("зачем ноль?")
    else:
        print("ответ: " + str(b))

def f3():
    a = input("введите дату")
    a = a.split(".")
    if int(a[0]) * int(a[1]) == int(a[2][2 : 4]):
        print("число магическое")
    else:
        print("число не магическое")

def f4():
    a = input("введите номер билета")
    b = 0
    t = 0
    if len(a) % 2 == 0:
        for i in a[0:int(len(a) / 2)]:
            b += int(i)
        for i in a[:int(len(a) / 2)]:
            t += int(i)
        if b == t:
            print("число магическое")
        else:
            print("число  не магическое")
    else:
        print("купите еще билет")

