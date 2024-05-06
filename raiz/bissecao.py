import math


def bissecao(func, interval, erro=0.01):
    i = 0
    while True:
        xm = (interval[0] + interval[1]) / 2.0

        fa = func(interval[0])
        fb = func(interval[1])

        if func(xm)*fa < 0:
            interval = (interval[0], xm)
        elif func(xm)*fb < 0:
            interval = (xm, interval[1])

        print(f"{i}, {xm}, {interval}")

        if abs(func(xm)) < erro:
            return xm, i

        i += 1

def main():
    result, interation = bissecao(lambda x: math.exp(x) - 2 * math.cos(x), (0, 2))
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")

if __name__ == "__main__":
    main()