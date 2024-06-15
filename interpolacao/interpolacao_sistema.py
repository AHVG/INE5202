import numpy as np


def interpolacao_sistema_linear(values_table):
    x = values_table[0, :]
    y = values_table[1, :]

    A = np.zeros((len(x), len(x)), dtype=float)

    for line in range(len(x)):
        A[line, :] = np.array([x[line]**i for i in range(len(x))])

    return np.linalg.solve(A, y)

if __name__ == "__main__":
    values_table = np.array([[2.0, 2.05, 2.1, 2.15],
                             [0.693, 0.718, 0.742, 0.765]], dtype=float)
    
    a = interpolacao_sistema_linear(values_table)
    
    p = np.poly1d(np.flip(a))
    print(p)
    print(p(2.14))