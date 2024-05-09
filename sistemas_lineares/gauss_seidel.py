import numpy as np


def gauss_seidel(A, B, Xo, error=0.001, max_interactions=10000):
    n = len(B)
    X = np.copy(Xo)

    interaction = 0
    while True:
        interaction += 1
        for i in range(n):
            aux_A = np.delete(A[i, :], i)
            aux_X = np.delete(X, i)
            X[i, 0] = (B[i, 0] - np.dot(aux_X, aux_A)) / A[i,i]


        R = np.max(np.array([B[i, 0] - np.dot(X[:, 0], A[i, :]) for i in range(n)]))

        if R < error or interaction > max_interactions:
            return X, interaction

def main():
    A = np.array([
        [3.0, -1.0, -1.0],
        [1.0, 3.0, 1.0],
        [2.0, -2.0, 4.0]
    ])
    B = np.array([
        [1.0],
        [5.0],
        [4.0]
    ])
    Xo = np.array([
        [0.0],
        [0.0],
        [0.0]
    ])
    X, interactions = gauss_seidel(A, B, Xo)
    print(X)
    print(interactions)

if __name__ == "__main__":
    main()
