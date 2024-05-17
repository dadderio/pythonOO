class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

if restaurante_praca.ativo:
    print('Restaurante está ativo')
else:
    print ('Restaurante está inativo')


nome = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food')
else:
    print('Não é categoria Fast Food')


restaurante_pizza.ativo = True

print(f'O nome é {restaurante_pizza.nome} e a categoria é {restaurante_pizza.categoria}')