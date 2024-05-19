import numpy as np

def interpolacao_lagrange(values_table):
    xs = values_table[0, :]
    y = values_table[1, :]
    
    def P(x):
        def L(x, j):
            result = 1
            for i in range(len(xs)):
                if i != j:
                    result *= (x - xs[i]) / (xs[j] - xs[i])
            return result

        return sum(y[term] * L(x, term) for term in range(len(xs)))
    
    return P


if __name__ == "__main__":
    values_table = np.array([[1.0, 1.3, 1.6],
                             [0.7652, 0.6200, 0.4540]],
                            dtype=float)
    p = interpolacao_lagrange(values_table)

    print(p(1.2))