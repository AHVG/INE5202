import math


def secante(func, interval, erro=0.01):
    xk = interval[0]
    xk1 = interval[1]
    i = 0

    while True:
        xk2 = xk1 - ((xk1 - xk) * func(xk1)) / (func(xk1) - func(xk))
        
        print(f"{i} {xk} {xk1} {xk2} {func(xk2)}")

        if abs(func(xk2)) < erro:
            return xk2, i
        
        xk = xk1
        xk1 = xk2

        i += 1


def main():
    result, interation = secante(lambda x: math.exp(x) - 2 * math.cos(x), (0, 2))
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")


if __name__ == "__main__":
    main()