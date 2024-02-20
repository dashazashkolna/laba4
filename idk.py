print('Hello Cillian Murphy')

def nsd(a,b):
    while b > 0:
        a, b = b, a % b
    return a