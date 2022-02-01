
# 1 Creation of functions
# A. Implement polynomial function
def polynome(x):
    result = (x**3 - 1.5*(x**2) - 6*x + 5)
    return result

# B. Implement factorielle function
def factorielle(x):
    result = x
    n = x
    # While loop until n = 0
    while n > 1:
        n = n - 1
        result = result * n
    return result

# C. Implement la suite de Fibonnaci
def fibonnaci(suite_size):
    fib_suite = [0, 1]
    for n in range(2, suite_size):
        fib_element = fib_suite[n-1] + fib_suite[n-2]
        fib_suite.append(fib_element)
    return fib_suite


if __name__ == '__main__':
    # Exercice 1 - a
    if polynome(5) == 62.5:
        print("Exercice 1.a - Test pass")
    else:
        print("Exercice 1.a - Test fail")

    # Exercice 1 - b
    if factorielle(5) == 120:
        print("Exercice 1.b - Test pass")
    else:
        print("Exercice 1.b - Test fail")

    # Exercice 1 - c
    if fibonnaci(6) == [0, 1, 1, 2, 3, 5]:
        print("Exercice 1.c - Test pass")
    else:
        print("Exercice 1.c - Test fail")