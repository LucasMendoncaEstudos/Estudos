lista = []
maior = menor = soma = media = 0
while len(lista) < 7:
    numero = input('Digite um valor: ')
    if numero.isdigit():
        numero = int(numero)
        lista.append(numero)
        soma += numero
        media = soma / len(lista)
        if len(lista) == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    else:
        print('Digite um valor válido!')
print(f'Os valores digitados foram: {lista}')
print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media:.2f}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')