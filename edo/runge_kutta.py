
def RK_segunda_ordem(func, y0, a, b, h):    
    x0 = a
    while x0 < b:
        k1 = h * func(x0, y0)
        k2 = h * func(x0 + h, y0 + k1)
        y0 = y0 + 1.0 / 2.0 * (k1 + k2)
        x0 = x0 + h

    return x0, y0

def RK_quarta_ordem(func, y0, a, b, h):
    x0 = a
    while x0 < b:
        print(x0)
        print(y0)
        k1 = h * func(x0, y0)
        k2 = h * func(x0 + h / 2.0, y0 + k1 / 2.0)
        k3 = h * func(x0 + h / 2.0, y0 + k2 / 2.0)
        k4 = h * func(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        x0 = x0 + h
        print(k1)
        print(k2)
        print(k3)
        print(k4)
        print()

    return x0, y0

def main():
    func = lambda x, y: -2.0 * x - y
    y0 = -1.0
    a = 0.0
    b = 0.5
    h = 0.1

    x, y = RK_segunda_ordem(func, y0, a, b, h)
    print(f"A solução é {x}, {y}")
    x, y = RK_quarta_ordem(func, y0, a, b, h)
    print(f"A solução é {x}, {y}")


if __name__ == "__main__":
    main()