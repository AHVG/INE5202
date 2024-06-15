# https://computeel.org/LOM3260/assets/aulas/pdf/Aula-integracao.pdf

def simpson_composta(func, a, b, n):
    h = (b - a) / n
    odd = 4.0 * sum(func(a + i * h) for i in range(1, n, 2))
    even =  2.0 * sum(func(a + i * h) for i in range(0, n + 1, 2))
    area = ((h / 3.0) * (func(a) + even + odd + func(b)))
    return area

def main():
    func = None
    a = None
    b = None
    n = None

    area = simpson_composta(func, a, b, n)
    print("Area da curva é %s" % area)


if __name__ == "__main__":
    main()

