# Iremos nos aprofundar um pouco mais nos testes unitários, garantindo que realmente estamos testando uma unidade por vez.

# Vamos simular a vendinha do Zé, ele terá alguns produtos para comercializar, onde podemos escolher um produto
# e calcular o valor total da compra.


class VendinhaDoZe:
# Temos aqui a classe da vendinha do Zé
    def __init__(self):
        self.salgado = ''
        self.quantidade_de_salgados = 0
        self.valor_do_salgado = 3.50
        self.refrigerante = ''
        self.quantidade_de_refrigerantes = 0
        self.valor_do_refrigerante = 2.50
    # Temos aqui alguns produtos que o a vendinha do Zé comercializa


    def imprime_pedido(self):
        # Temos aqui um método que imprime o pedido realizado pelo cliente, para isso ele chama outros dois
        # métodos da classe, para receber os valores totais para imprimir
        valor_total_dos_refrigerantes = calculo_valor_total_refrigerantes(self.quantidade_de_refrigerantes, self.valor_do_refrigerante)
        valor_total_dos_salgados = calculo_valor_total_salgados(self.quantidade_de_salgados, self.valor_do_salgado)
        valor_total_da_compra = calculo_valor_total_da_compra(valor_total_dos_salgados, valor_total_dos_refrigerantes)
        print('Seu pedido é: ')
        print(f'{self.quantidade_de_salgados} unidades de {self.salgado} no valor de {valor_total_dos_salgados}')
        print(f'{self.quantidade_de_refrigerantes} unidades de {self.refrigerante} no valor de {valor_total_dos_refrigerantes}')
        print(f'O valor total da compra é de R$ {valor_total_da_compra}')


    def realizar_pedido(self):
    # Temos aqui um método que coletará do cliente, as informações para montar um pedido
        self.salgado = input('Informe um salgado [coxinha/pastel/enroladinho]: ')
        self.quantidade_de_salgados = input('Informe quantas unidades de salgado: ')
        self.refrigerante = input('Informe um refrigerante [pepsi/sukita/guaraná]: ')
        self.quantidade_de_refrigerantes = input('Informe quantas unidades de refrigerante: ')
        # Temos aqui os input's para coletarmos as informações de nossos clientes
        

# Temos aqui uma classe completa, com atributos e métodos, vamos testar cada um deles individualmente
# não será necessário criarmos todo nosso programa para garantirmos de cada funcionalidade da nossa classe, 
# com o teste unitário e o mock, vamos testar e simular cada comportamento isoladamente.


def calculo_valor_total_da_compra(valor_total_dos_salgados, valor_total_dos_refrigerantes):
# Temos aqui um método que recebe o valor total de salgados, o valor total de refrigerantes, calcula e retorna 
# o valor total da compra.
    valor_total_da_compra = valor_total_dos_salgados + valor_total_dos_refrigerantes
    return valor_total_da_compra


def calculo_valor_total_salgados(quantidade_de_salgados, valor_do_salgado):
# Temos aqui um método que calcula o valor total dos salgados solicitados pelo cliente e retorna esse valor
    valor_total_dos_salgados = quantidade_de_salgados * valor_do_salgado
    return valor_total_dos_salgados


def calculo_valor_total_refrigerantes(quantidade_de_refrigerantes, valor_do_refrigerante):
# Temos aqui um método que calcula o valor total dos refrigerantes solicitados pelo cliente e retorna esse valor
    valor_total_dos_refrigerantes = quantidade_de_refrigerantes * valor_do_refrigerante
    return valor_total_dos_refrigerantes


# Vamos começar com o test_mock_1.py dentro da pasta tests