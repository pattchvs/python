import math

print("Vamos calcular as raízes de uma equação de segundo grau (ax² + bx + c)")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raizes reais para essa equação.")
elif delta == 0:
    raiz = -b / (2*a)
    print("Esta equação possui uma raiz: ", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("Esta equação possui duas raízes: ", raiz1, " e ", raiz2)