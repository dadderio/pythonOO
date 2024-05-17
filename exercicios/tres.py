
# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
#    Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:

    def __init__ (self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
carro_1 = Carro(modelo='Prisma', cor='preto', ano='2010')

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
#    Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

restaurante_1 = Restaurante(nome='Fazenda', categoria='Mineira', ativo=True, capacidade=100, nota_avaliacao=5)

# 3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como 
#    parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# 4. Adicione um método especial __str__ à classe Restaurante para que, 
#    ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. 
#    Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=None, nota_avaliacao=0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome | self.categoria}'

novo_restaurante = Restaurante(nome='Bolinha', categoria='caseira')

print(novo_restaurante)       

# 5. Crie uma classe chamada Cliente e pense em 4 atributos. 
#    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus 
#    atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', cpf=0, telefone=0, endereco=''):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

cliente_1 = Cliente(nome='Mario', cpf=12341234, telefone=44234, endereco='Rua Vinte, SP')

