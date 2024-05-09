import numpy as np

from utils import set_zeros


def gauss_pivotamento_parcial_virtual(A, B):
    n = len(B)
    O = np.array(list(range(n)))

    for column in range(A.shape[1] - 1):

        max_index = column
        value = np.abs(A[O[column], column])

        for i in range(column + 1, n):
            if value < np.abs(A[O[i], column]):
                max_index = i
                value = A[O[i], column]

        O[[column, max_index]] = O[[max_index, column]]

        for line in O[column + 1:]:
            factor = - A[line, column] / A[O[column], column]
            A[line, :] = A[line, :] + factor * A[O[column], :]
            B[line, :] = B[line, :] + factor * B[O[column], :]

    set_zeros(A)
    set_zeros(B)

    X = np.zeros((n, B.shape[1]), dtype=float)

    for line in range(n - 1, -1, -1):
        X[line] = (B[O[line], :] - np.dot(A[O[line], :], X)) / (A[O[line], line])

    return A, B, O, X

def main():
    A = np.array([
        [-0.421, 0.784, 0.279],
        [0.448, 0.832, 0.193],
        [0.421, 0.784, -0.207]
    ])
    B = np.array([[0.0],
                  [1.0],
                  [0.0]])
    A, B, O, X = gauss_pivotamento_parcial_virtual(A, B)
    print(A)
    print(B)
    print(O)
    print(X)

if __name__ == "__main__":
    main()