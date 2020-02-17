# Unittest é um framework que vem por padrão no python para nos auxiliar nos testes unitários

from unittest import TestCase
# TesteCase é a classe padrão do framework unittest que nos permitirá herdar características
# para que possamos tornar nossos testes unitários mais dinâmicos e fáceis de visualizar.


# Para realizarmos os testes unitários, devemos importar os métodos e asvclasses que queremos 
# testar.
from app.teste_com_framework.teste_unitario_com_unittest import soma, subtracao, Carro


# *************************** Classe de teste usando unittest *******************************

class TesteExemplo(TestCase):
# Nossa classe TesteExemplo está agora herdando métodos e características da classe TestCase
    
    # Método da classe TesteExemplo que testa o método soma criado anteriormente
    def test_soma(self):
        # Dentro do framework unittest, continuamos usando o assert para os testes unitários,
        # mas agora ele é um atributo da classe TestCase, que no nosso caso foi herdado pela
        # TesteExemplo.
        self.assertEqual(soma(2,2), 4)
        self.assertIsInstance(soma(2,2),int)

# Para rodar esse teste no terminal, devemos abrir o terminal e executar o arquivo com os
# testes, que no nosso caso é o test_3.py que está dentro da pasta testes.
# Comando para execução do teste via terminal:
# python -m unittest app/tests/test_3.py


# Se os testes ocorrerem com sucesso, será exibido uma mensagem com a quantidade de testes
# que foram executados, apresentando o status ok e quanto tempo o python levou para executar
# estes testes.


# se os testes não ocorrerem com sucesso, será exibido uma mensagem com o primeiro teste que
# falhou e qual foi o erro apresentado.

    def test_subtracao(self):
        self.assertEqual(subtracao(10,5), 5)

# Testando a classe Carro
    def test_classe_carro(self):
        # Criado um novo objeto da classe carro
        novo_carro = Carro('celta', 'chevrolet')
        
        self.assertEqual(novo_carro.modelo, 'celta')
        self.assertEqual(novo_carro.marca, 'chevrolet')
        self.assertIsInstance(novo_carro, Carro)

# Conseguimos testar diversas situações com o unittest, desde teste de igualdade, 
# testes com quaisquer condições, inclusive em listas e dicionários, até objetos
# de classes.