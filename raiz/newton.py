from sympy import symbols, diff, exp, cos


# passar só a função?
def newton(func, x, interval, erro=0.01, max_interactions=10000):
    der = diff(func, x)
    xk = (interval[0] + interval[1]) / 2.0
    i = 0

    while True:
        xk1 = xk - func.subs(x, xk) / der.subs(x, xk)

        if func.subs(x, xk1) < erro or i > max_interactions:
            return xk1, i 

        xk = xk1
        i += 1

def main():
    x = symbols('x')
    func = exp(x) - 2 * cos(x)

    result, interactions = newton(func, x, (0,2))
    print(f"Resultado: {result}")
    print(f"Interação: {interactions}")

    x = symbols('x')
    func = exp(x) + x

    result, interactions = newton(func, x, (-1,0))
    print(f"Resultado: {result}")
    print(f"Interação: {interactions}")



if __name__ == "__main__":
    main()