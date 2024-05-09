
import sympy as sp
import numpy as np


def gauss(F, vars, X0, erro=0.01, max_interactions=10000):
    J = F.jacobian(vars)

    F_lamb = sp.lambdify(vars, F, 'numpy')
    J_lamb = sp.lambdify(vars, J, 'numpy')

    interactions = 0

    while True:
        interactions += 1
        F_val = F_lamb(*X0)
        J_val = J_lamb(*X0)

        d = np.linalg.solve(J_val, -F_val)
        X0 = X0 + d[:,0]

        if np.sum(np.abs(d)) < erro or interactions > max_interactions:
            return X0, interactions

def main():
    x1, x2 = sp.symbols('x1 x2')
    vars = sp.Matrix([x1, x2])
    
    f1 = sp.exp(x1) + x2 - 1.0
    f2 = x1**2 + x2**2 - 4.0
    F = sp.Matrix([f1, f2])
    print(gauss(F, vars, np.array([1.0, -1.0]), 0.0000007))

if __name__ == "__main__":
    main()
