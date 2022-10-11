def factorialNormal(n):
    r = 1
    i = 2

    while i <= n:
        r *= i
        i += 1
    return r



def factorialRecursiva(fact):
    if fact == 0:
        return 1
    else:
        return fact * factorialRecursiva(fact-1)


print(factorialNormal(4))
print(factorialRecursiva(4))