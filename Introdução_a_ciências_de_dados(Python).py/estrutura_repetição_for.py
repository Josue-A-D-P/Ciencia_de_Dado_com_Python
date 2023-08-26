texto = input('Informe o texto: ')
VOGAIS = 'AEIOU'

# Exemplo iteravel:
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra , end= " ")
else:
    print()# adiciona uma quebra de linha

# Exemplo com range:

for num in range(0,51,5):
    print(num, end= " ")