
def trapezio(func, a, b):
    return (b - a) / 2.0 * (func(a) + func(b))

def trapezio_composta(func, a, b, n):
    h = (b - a) / n
    area = (h / 2.0 ) *(func(a) + sum(func(a + i * h) for i in range(n)) + func(b))
    return area

def main():
    func = lambda x: 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5
    a = 0.0
    b = 0.8
    n = 10

    area = trapezio(func, a, b)
    print("Area da curva é %s" % area)

    area = trapezio_composta(func, a, b, n)
    print("Area da curva é %s" % area)


if __name__ == "__main__":
    main()
