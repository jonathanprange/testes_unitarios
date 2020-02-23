# Começaremos os testes unitários como nas aulas anteriores e depois iremos conhecer um pouco sobre mock

# Vamos então importar o framework padrão do python para testes
from unittest import TestCase
# Com o a classe TestCase, agora podemos herdar dela, tudo que precisamos para começar os testes


# Vamos testar a classe VendinhaDoZe, para isso, precisamos importar ela para nossos testes.
from app.mock.mock import VendinhaDoZe


class TestIntroducaoAoMock(TestCase):
# Com isso, a classe TestIntroducaoAoMock, herdou todas as caracteristicas da classe TestCase


    # Vamos então, testar o método __init__() da classe VendinhaDoZe e verificar se ele atende ao que
    # precisamos que ele faça.
    def test_init(self):
        # Daqui para frente, seguiremos o padrão AAA (Arrange, Action, Assertions) para organizarmos nossos testes,
        # que é o mais comum de encontrarmos no mercado.


        # Arrange (organizar)
            # Neste caso não será necessário uma organização prévia para podermos testar o __init__(), veremos adiante
            # casos onde serão necessários orgarnizarmos situações para nossos testes.
            # A parte de organização, pode ser composta de zero ou mais preparações, para que possamos realizar uma ação.

        # Action (Ação)
        nova_vendinha_do_ze = VendinhaDoZe()
            # Estamos criando um objeto da classe VendinhaDoZe, para testarmos se ela se comporta como precisamos.
            # A parte de ação, sempre será composta por uma única ação, que será a ação que queremos testar.

        # Assertions (afirmações)
        self.assertIsInstance(nova_vendinha_do_ze, VendinhaDoZe)
        self.assertEqual(nova_vendinha_do_ze.salgado, '')
        self.assertEqual(nova_vendinha_do_ze.quantidade_de_salgados, 0)
        self.assertEqual(nova_vendinha_do_ze.valor_do_salgado, 3.50)
        self.assertEqual(nova_vendinha_do_ze.refrigerante, '')
        self.assertEqual(nova_vendinha_do_ze.quantidade_de_refrigerantes, 0)
        self.assertEqual(nova_vendinha_do_ze.valor_do_refrigerante, 2.50)
            # A parte de afirmações, pode ser composta de uma ou mais afirmações, quantas forem necessárias para 
            # garantirmos que todas as situações previstas foram atendidas.
            # Neste caso, estamos verificando se o objeto nova_vendinha_do_ze pertence a classe VendinhaDoZe
            # e se a construção inicial do objeto, está conforme previmos.


# Vamos agora visualizar a área de cobertura de nosso teste, para vizualizarmos a nossa progressão

    # Execute no terminal: py -m pip install coverage "ou" pip3 install coverage

# Com a instalação do coverage, conseguiremos melhorar a visualização de nossos testes
# vamos visualizar quantos testes foram executados:

    # Execute no terminal: py -m coverage run -m unittest discover "ou" 
    # coverage run -m unittest discover

    # ***************************** Resposta do terminal *****************************

    # ........
    # ----------------------------------------------------------------------
    # Ran 8 tests in 0.003s

    # OK

    # ************************* Fim da resposta do terminal **************************

    # Cada ponto informa um teste que passou com sucesso
    # Se no lugar do ponto tivermos um F, informa quantos testes falharam
    # Se no lugar do ponto tivermos um E, aconteceu um erro ao tentar executar o teste


# Agora vamos ver a cobertura total de nossos testes, via terminal:

    # Execute no terminal: py -m coverage report -m "ou" coverage report -m

    # Name                                                      Stmts   Miss  Cover   Missing
    # ---------------------------------------------------------------------------------------
    # app\__init__.py                                               0      0   100%
    # app\mock\__init__.py                                          0      0   100%
    # app\mock\mock.py                                             30     17    43%   21-24, 31-37, 43-44, 49-50, 55-56
    # app\tdd\__init__.py                                           0      0   100%
    # app\tdd\tdd_1.py                                              2      0   100%
    # app\tdd\tdd_2.py                                              3      0   100%
    # app\tdd\tdd_3.py                                              4      0   100%
    # app\tdd\tdd_4.py                                              6      0   100%
    # app\teste_assert\__init__.py                                  0      0   100%
    # app\teste_assert\teste_assert.py                              8      3    62%   27-40
    # app\teste_com_framework\__init__.py                           0      0   100%
    # app\teste_com_framework\teste_unitario_com_unittest.py       10      0   100%
    # app\teste_sem_framework\__init__.py                           0      0   100%
    # app\teste_sem_framework\teste_unitario_sem_framework.py      16     11    31%   25-43
    # app\tests\__init__.py                                         0      0   100%
    # app\tests\test_com_framework.py                              13      0   100%
    # app\tests\test_introducao_mock.py                            12      0   100%
    # app\tests\test_tdd_1.py                                       5      0   100%
    # app\tests\test_tdd_2.py                                       5      0   100%
    # app\tests\test_tdd_3.py                                       6      0   100%
    # app\tests\test_tdd_4.py                                       7      0   100%
    # ---------------------------------------------------------------------------------------
    # TOTAL                                                       127     31    76%    


    # Agora conseguimos visualizar para cada arquivo de código que criamos, qual a porcentagem de cobertura,
    # além de visualizarmos a quantidade de linhas com códigos escritos e a quantidade de linhas que não estamo
    # cobrindo com nossos testes. É possível visualizar inclusive, exatamente quais as linhas que não estamos
    # cobrindo com nossos testes.


# Por último, podemos melhorar ainda mais nossa visualização de cobertura, gerando um relatório em html.

    # Execute no terminal: py -m coverage html "ou" coverage html

    # Após a execução deste comando, será criado uma pasta chamada htmlcov, dentro dessa pasta estarão diversos arquivos
    # em html, procure por index.html e abra o mesmo em seu navegador internet de sua preferência.

    # No navegador, será possível visualizar a cobertura total, de forma parecida com o relatório anterior,
    # mas também será possível entrar em cada arquivo e visualizar todo o código com a informação linha a linha,
    # sendo com um fundo em verde para as linhas cobertas pelos testes e sendo com um fundo em vermelho para as 
    # linhas não cobertas pelos testes.



# Continuaremos no arquivo test_mock_1.py