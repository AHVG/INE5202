
def trapezio_composta(func, a, b, n):
    h = (b - a) / n
    area = (h / 2.0 ) *(func(a) + sum(func(a + i * h) for i in range(n)) + func(b))
    return area

def main():
    func = None
    a = None
    b = None
    n = None

    area = trapezio_composta(func, a, b, n)
    print("Area da curva é %s" % area)


if __name__ == "__main__":
    main()
