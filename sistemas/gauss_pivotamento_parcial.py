import numpy as np


def gauss_pivotamento_parcial(A, B):

    print(A)
    print(B)
    print()

    # Usar 4 algarismos significativos?
    for column in range(A.shape[1] - 1):

        max_index = np.argmax(np.abs(A[:, column]))
        A[[column, max_index]] = A[[max_index, column]]
        B[[column, max_index]] = B[[max_index, column]]

        for line in range(column + 1, A.shape[1]):
            factor = - A[line, column] / A[column, column]
            A[line, :] = A[line, :] + factor * A[column, :]
            B[line, :] = B[line, :] + factor * B[column, :]
            print(f"Factor {factor}")
            print(f"A {A}")
            print(f"B {B}")
            print()

    limit = np.finfo(A.dtype).eps
    A[np.abs(A) < limit] = 0.0
    limit = np.finfo(B.dtype).eps
    B[np.abs(B) < limit] = 0.0

    X = np.array(B[A.shape[1] - 1, :] / A[A.shape[1] - 1, A.shape[1] - 1])
    for line in range(A.shape[1] - 2, -1, -1):
        s = np.sum(np.array([A[line, A.shape[0] - i - 1] * value for i, value in enumerate(X)]))
        x = (B[line, :] - s) / A[line, A.shape[0] - X.shape[0] - 1]
        X = np.append(X, x)

    print(f"A {A}")
    print(f"X {X}")
    print(f"B {B}")

    return None

def main():
    A = np.array([
        [-0.421, 0.784, 0.279],
        [0.448, 0.832, 0.193],
        [0.421, 0.784, -0.207]
    ])
    B = np.array([[0.0],
                  [1.0],
                  [0.0]])

    result = gauss_pivotamento_parcial(A, B)
    print(f"result {result}")

if __name__ == "__main__":
    main()