numero = 35

def calculaFibonacci(numberx):
    y = 0
    z = 1
    while numberx >= y:
        if y == numberx:
            return 'pertence a sequencia'
        aux = z + y
        y = z
        z = aux
    return 'nao pertence a sequencia'
        

print(calculaFibonacci(numero))
