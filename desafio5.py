palavra = input('digite uma string')
lista = []
lista2 = []

for x in palavra:
    lista.append(x)

for x in palavra:
    lista2.append(lista.pop())

print(''.join(lista2))