# https://computeel.org/LOM3260/assets/aulas/pdf/Aula-integracao.pdf

def simpson(func, a, b):
    return (b - a) / 6.0 * (func(a) + 4 * func(a + (b - a) / 2.0) + func(b))

def simpson_composta(func, a, b, n):
    h = (b - a) / n
    print(h)
    odd = 4.0 * sum(func(a + i * h) for i in range(1, n, 2))
    even =  2.0 * sum(func(a + i * h) for i in range(2, n, 2))
    print(odd)
    print(even)
    print(even + odd)
    area = ((h / 3.0) * (func(a) + even + odd + func(b)))
    return area

def main():
    func = lambda x: 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5
    a = 0.0
    b = 0.8
    n = 4

    area = simpson(func, a, b)
    print("Area da curva é %s" % area)

    area = simpson_composta(func, a, b, n)
    print("Area da curva é %s" % area)


if __name__ == "__main__":
    main()

