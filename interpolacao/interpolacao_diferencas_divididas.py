import numpy as np

def diferencas_divididas(ys, xs):
    if len(ys) == 1:
        return ys[0]
    return (diferencas_divididas(ys[1:], xs[1:]) - diferencas_divididas(ys[:-1], xs[:-1])) / (xs[-1] - xs[0])

def interpolacao_diferencas_divididas(values_table):
    xs = values_table[0, :]
    ys = values_table[1, :]
    a = [diferencas_divididas(ys[:i], xs[:i]) for i in range(1, len(xs) + 1)]

    def P(x):
        result = a[0]
        dx = 1
        for i in range(1, len(a)):
            dx *= (x - xs[i - 1])
            result += a[i]*dx
        return result

    return P

def interpolacao_diferencas_divididas_poly(values_table):
    xs = values_table[0, :]
    ys = values_table[1, :]
    a = [diferencas_divididas(ys[:i+1], xs[:i+1]) for i in range(len(xs))]

    # Inicializa o polinômio com o termo constante
    P = np.poly1d([a[0]])
    for i in range(1, len(a)):
        # Cria um polinômio (x - xs[0]) * (x - xs[1]) * ... * (x - xs[i-1])
        term = np.poly1d([1])
        for j in range(i):
            term *= np.poly1d([1, -xs[j]])
        # Adiciona o termo ao polinômio acumulado, multiplicado pelo coeficiente apropriado
        P += a[i] * term

    return P

if __name__ == "__main__":
    values_table = np.array([[0.1, 0.3, 2.0],
                             [4.0, 1.0, -1.0]],
                            dtype=float)
    p = interpolacao_diferencas_divididas(values_table)
    print(p(-1))
    print(p(0))
    print(p(2))

    values_table = np.array([[0.1, 0.3, 0.5, 0.7],
                             [0.101, 0.327, 0.625, 1.043]], dtype=float)
    p = interpolacao_diferencas_divididas_poly(values_table)
    print(p)
    print(p(0.4))
