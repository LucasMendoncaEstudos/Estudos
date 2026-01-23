from modulo.restaurante import Restaurante
from modulo.cardapio.bebida import Bebida
from modulo.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmert')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pãozinho', 2, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
sobre_mesa = Prato('Pudim', 7.00, 'Pudim de leite com calda de caramelo')
sobre_mesa.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobre_mesa)

def main():
    restaurante_praca.exibir_cardapio

if __name__=='__main__':
    main()