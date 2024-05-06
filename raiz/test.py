import math
import inspect

from bissecao import bissecao
from falsa_posicao import falsa_posicao
from falsa_posicao_modificada import falsa_posicao_modificada


def test(method, f, interval):
    print("-" * 100)
    source_code = inspect.getsource(f)
    print(f"Método {method.__name__}")
    print(f"Função {source_code.strip()}")
    result, interation = method(f, interval)
    print()
    print(f"Resultado: {result}")
    print(f"Interação: {interation}")
    print("-" * 100)
    print()

def main():
    func = lambda x: math.exp(x) + x
    interval = (-1, 0)

    test(bissecao, func, interval)
    test(falsa_posicao, func, interval)
    test(falsa_posicao_modificada, func, interval)

    func = lambda x: math.exp(x) - 2 * math.cos(x)
    interval = (0, 2)

    test(bissecao, func, interval)
    test(falsa_posicao, func, interval)
    test(falsa_posicao_modificada, func, interval)

if __name__ == "__main__":
    main()