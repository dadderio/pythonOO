from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Re', 5)
restaurante_praca.receber_avaliacao('Dri', 4)
restaurante_praca.receber_avaliacao('Deia', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()