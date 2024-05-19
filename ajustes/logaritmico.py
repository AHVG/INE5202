import numpy as np

from polinomial import ajuste_polinomial


def ajuste_logaritmico(values_table):
    pass

def main():
    values_table = np.array([[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
                             [3.16, 2.38, 1.75, 1.34, 1.00, 0.74, 0.56]],
                             dtype=float)
    ajuste_logaritmico(values_table)


if __name__ == "__main__":
    main()