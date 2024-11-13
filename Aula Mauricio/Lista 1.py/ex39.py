# 39. Implemente uma função aproxima_pi(n) que calcula uma aproximação do número pi usando n termos da série de Leibniz.
def aproxima_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi

# Teste da função aproxima_pi
print(aproxima_pi(1000))  # Saída aproximada de pi: 3.140592653839794
print(aproxima_pi(10000))  # Saída aproximada de pi: 3.141492653590034

