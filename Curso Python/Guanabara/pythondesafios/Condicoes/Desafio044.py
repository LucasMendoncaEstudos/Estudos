'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-Á vista dinheiro/cheque: 10% de desconto
-Á vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('Lojas LK '))
preco = float(input('Preço das compras: R$'))
pg = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção? '''))
if pg == 1:
    total = preco - (preco * 10 / 100)
elif pg ==2:
    total = preco - (preco * 5/100)
elif pg == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif pg == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {:.2f} de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0 
    print('OPÇÃO INVÁLIDA de pagament. TENTE novamente')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format (preco,total))