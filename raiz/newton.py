from sympy import symbols, diff, exp, cos


def newton(func, x, interval, erro=0.01):
    der = diff(func, x)
    xk = (interval[0] + interval[1]) / 2.0
    i = 0

    while True:
        xk1 = xk - func.subs(x, xk) / der.subs(x, xk)

        print(f"{i} {xk} {xk1}")

        if func.subs(x, xk1) < erro:
            return xk1, i 

        xk = xk1
        i += 1


def main():
    x = symbols('x')
    func = exp(x) - 2 * cos(x)

    result, interation = newton(func, x, (0,2))
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")

    x = symbols('x')
    func = exp(x) + x

    result, interation = newton(func, x, (-1,0))
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")



if __name__ == "__main__":
    main()