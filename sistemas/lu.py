import numpy as np


def successive_replacement(A, B):
    n = len(B)
    X = np.zeros((n, B.shape[1]), dtype=float)

    for line in range(n - 1, -1, -1):
        X[line] = (B[line, :] - np.dot(A[line, :], X)) / (A[line, line])

    return X


def lu(A, B):
    n = len(B)
    L = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)
    Y = np.zeros((n, 1), dtype=float)
    X = np.zeros((n, 1), dtype=float)
    
    L[:, 0] = np.copy(A[:, 0])
    U[0, 1:] = np.copy(A[0, 1:]) / L[0,0]

    for i in range(n):
        U[i,i] = 1

    for i in range(1, n):
        for line in range(i, n):
            L[line, i] = A[line, i] - np.dot(L[line, :i], U[:i, i])

        for column in range(i + 1, n):
            U[i, column] = (A[i, column] - np.dot(L[i, :], U[:, column])) / L[i, i]

    Y = successive_replacement(np.flip(L), np.flip(B))
    X = successive_replacement(U, np.flip(Y))

    return L, U, Y, X, n

def main():
    A = np.array([[4.0, 2.0, 3.0],
                  [2.0, -4.0, -1.0],
                  [-1.0, 1.0, 4.0]])
    B = np.array([[7.0],
                  [1.0],
                  [-5.0]])

    L, U, Y, X, n = lu(A, B)

    print(X)

if __name__ == "__main__":
    main()