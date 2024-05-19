import numpy as np

from polinomial import ajuste_polinomial


def ajuste_exponencial(values_table):
    Z = np.array([np.log(i) for i in values_table[1, :]], dtype=float)
    C = ajuste_polinomial(np.array([values_table[0, :], Z], dtype=float), 1)
    Io = np.exp(C[0][0])
    return Io, C[1][0]

def main():
    values_table = np.array([[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
                             [3.16, 2.38, 1.75, 1.34, 1.00, 0.74, 0.56]],
                             dtype=float)
    i, x = ajuste_exponencial(values_table)
    print(i)
    print(x)

    values_table = np.array([[0.1, 1.5, 3.3, 4.5, 5.0],
                             [1.77, 2.17, 2.48, 2.99, 3.15]],
                             dtype=float)
    i, x = ajuste_exponencial(values_table)
    print(i)
    print(x)

    values_table = np.array([[-1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.0],
                             [36.547, 17.264, 8.155, 3.852, 1.82, 0.860, 0.406, 0.246]],
                             dtype=float)
    i, x = ajuste_exponencial(values_table)
    print(i)
    print(x)


if __name__ == "__main__":
    main()