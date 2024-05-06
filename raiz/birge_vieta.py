import sympy as sp


def birge_vieta(poly, x0, interation=3):
    coeffs = poly.all_coeffs()

    def get_Rs(poly, a):
        bs = [coeffs[0]]
        
        for i, coeff in enumerate(coeffs[1:]):
            print(f"c {coeff} b {bs[i]}")
            bs.append(coeff + bs[i] * a)
            print(bs)

        cs = [bs[0]]

        for i, b in enumerate(bs[1:]):
            cs.append(b + cs[i] * a)

        print(bs)
        print(cs)

        return bs[-1], cs[-2]

    xk = x0

    for i in range(interation):
        R, Rd = get_Rs(poly, xk)
        xk1 = xk - R / Rd
        print(f"{i} {float(xk)} {float(xk1)} {float(R)} {float(Rd)}")
        xk = xk1

    return xk

def main():
    x = sp.symbols('x')
    p = sp.Poly(x**3 + 2*x - 1, x)
    print(p.all_coeffs())
    result = birge_vieta(p, 1)
    print(f"Resultado {float(result)}")


if __name__ == "__main__":
    main()