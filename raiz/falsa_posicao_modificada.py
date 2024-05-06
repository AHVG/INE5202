import math


def falsa_posicao_modificada(func, interval, erro=0.01):
    i = 0
    while True:
        fa = func(interval[0])
        fb = func(interval[1])

        xk = interval[0] - (fa * (interval[1] - interval[0])) / (fb - fa)
        
        if func(xk) * fa < 0:
            fator = fb / (fb + func(xk))
            interval = (interval[0] * fator, xk)
        elif func(xk) * fb < 0:
            fator = fa / (fa + func(xk))
            interval = (xk, interval[1] * fator)

        print(f"{i}, {xk}, {interval}")

        if abs(func(xk)) < erro:
            return xk, i

        i += 1

def main():
    result, interation = falsa_posicao_modificada(lambda x: math.exp(x) + x, (-1, 0))
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")


if __name__ == "__main__":
    main()