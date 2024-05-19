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

if __name__ == "__main__":
    values_table = np.array([[-1.0, 0.0, 2.0],
                             [4.0, 1.0, -1.0]],
                            dtype=float)
    p = interpolacao_diferencas_divididas(values_table)
    print(p(-1))
    print(p(0))
    print(p(2))