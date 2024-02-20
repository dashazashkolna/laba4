def factorial(a):
    if a == 1 or a == 0:
        return 1

    return a * (a - 1)

def proste(el):
    for d in range(2, int(el**0.5)+1):
        if el % d == 0:
            return "Це число не є просте"
    return "Це число є просте"


def power5(num):
    if num <= 0:
        return False
    while num % 5 == 0:
        num //= 5
    return num == 1

def power2(num):
    if num <= 0:
        return False
    while num % 2 == 0:
        num //= 2
    return num == 1

