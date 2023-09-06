def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

sum = somar
sub = subtrair

print(sum(10,10))
print(sub(10,10))