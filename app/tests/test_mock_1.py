# Vamos então importar o framework padrão do python para testes
from unittest import TestCase
# Com o a classe TestCase, agora podemos herdar dela, tudo que precisamos para começar os testes


# Vamos testar a classe VendinhaDoZe, para isso, precisamos importar ela para nossos testes.
from app.mock.mock import VendinhaDoZe


class TestMock(TestCase):
# Com isso, a classe TestMock, herdou todas as caracteristicas da classe TestCase

    # Vamos então, testar o método imprime_pedido() da classe VendinhaDoZe e verificar se ele atende ao que
    # precisamos que ele faça.
    def test_imprime_pedido(self):
        # O método imprime_pedido(), chama outros três métodos, vamos testar e ver como será o comportamento,
        # a cobertura do nosso teste e depois faremos o mesmo teste utilizando mock

        # Arrange (organizar)
        nova_vendinha_do_ze = VendinhaDoZe()
            # para executarmos nosso teste, precisamos organizar todos os elementos necessários,
            # Neste caso, para executarmos o método imprime_pedido(), é necessário criarmos um objeto da
            # classe VendinhaDoZe()


        # Action (Ação)
        resultado = nova_vendinha_do_ze.imprime_pedido()
            # executaremos a método que queremos testar para verificarmos se ele atende aos comportamentos que
            # esperamos


        # Assertions (Afirmações)
        self.assertEqual(resultado, None)
            # Nosso método não tem "retorno", logo podemos testar se ao chamarmos ele, o resultado é None


# Executando este teste no terminal com o comando py -m unittest app/tests/test_mock_1.py "ou" python -m unittest app/tests/test_mock_1.py
# temos a seguinte resposta do terminal:

    # ***************************** Resposta do terminal *****************************

    # $ python -m unittest app/tests/test_mock_1.py
    # Seu pedido é:
    # 0 unidades de  no valor de 0.0
    # 0 unidades de  no valor de 0.0
    # O valor total da compra é de R$ 0.0
    # .
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.001s

    # OK

# Nosso teste executou o método que foi chamado, esse método chamou outros métodos e depois imprimiu os resultados no terminal.

# Vamos verificar a cobertura do teste, executando o comando: py -m coverage run -m unittest discover "ou" coverage run -m unittest discover

# Na sequência execute no terminal: py -m coverage html "ou" coverage html

# Abra o index.html e vamos verificar a cobertura do método que testamos.

# Se olharmos a cobertura, veremos que o teste cobriu o método que testamos e inclusive cobriu
# os outros três métodos que foram chamados pelo método imprime_pedido()

# Com essas informações, vamos discutir algumas observações:

# * Primeiro, nosso teste executou o código e realizou impressões no terminal.
#       Seria melhor conseguirmos testar esse método sem executar essas impressões no terminal,
#       precisamos somente garantir que nosso método atenda ao comportamento que esperamos dele.
#       Para evitar a impressão no terminal, vamos simular esse comportamento através do objeto
#       da classe mock (explicarei mais conforme montarmos nosso próximo cenário).
#
# * Segundo, nosso teste executou outros três métodos que nós ainda não testamos, observando a cobertura,
#       percebemos que os outros três métodos estão cobertos, mas eles não foram testados diretamente,
#       dessa forma, o teste que executamos agora, além de interferir em outros métodos da classe,
#       depende destes métodos para que execute corretamente.
#       Do ponto de vista do teste unitário, um método deve ser testável por si só, sem a interferência
#       de quaisquer ações externas, somente assim, estamos realmente testando aquela unidade.
#       Para evitar que nosso teste dependa destes outros três métodos, que podem interferir no 
#       resultado de nosso teste, iremos simular esse comportamento através do objeto da classe mock.


# Seguiremos no: app/tests/test_mock_2.py