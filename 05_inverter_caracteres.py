texto = str(input("Digite o texto: \n"))

#Maneira um
print('Maneira um:')
print(texto[:: -1])

#Maneira dois
print('\nManeira dois:')
novo_texto = ""
for c in range(-1, -len(texto) -1, -1):
    novo_texto += texto[c]

print(novo_texto)
