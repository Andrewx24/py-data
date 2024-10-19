
x= int(input("how much did you earn last year?"))


def tax(x):
    if x < 10000:
        return 0
    elif x < 20000:
        return 0.1
    elif x < 30000:
        return 0.2
    else:
        return 0.3
    

print(tax(x))