# Primeiro de tudo, existem no mínimo centenas de formas de se trabalhar com o mock
# Uma base do que se pode fazer está contida na própria documentação do unittest

# https://docs.python.org/3/library/unittest.mock.html

# Podemos enxergar várias formas de fazer a mesma coisa, além de conseguirmos 
# simular situações mais complexas.

# Darei alguns exemplos de tipos de asserts e algumas manipulações com mock.
# Com base nisso você consegue se aprofundar e testar diversos cenários.

from unittest import TestCase
from unittest.mock import patch, call

# Usaremos métodos e classes criados no arquivo exemplos_mock.py
from app.exemplos_mock.exemplos_mock_1 import *


class TestExemplosMetodos(TestCase):

    @patch('app.exemplos_mock.exemplos_mock_1.metodo_nao_sera_chamado')
    @patch('app.exemplos_mock.exemplos_mock_1.get_segundo_valor')
    @patch('app.exemplos_mock.exemplos_mock_1.get_primeiro_valor')
    def test_soma(self, mock_get_primeiro_valor, mock_get_segundo_valor, mock_metodo_nao_sera_chamado):
        # Arrange
        mock_get_primeiro_valor.return_value = 2
        mock_get_segundo_valor.return_value = 5

        # Action
        resultado = soma()

        # Assertions
        self.assertEqual(resultado, 7)
        mock_get_primeiro_valor.assert_called() # Se o método foi chamado
        mock_get_primeiro_valor.assert_called_once() # Se o método foi chamado uma única vez
        mock_get_primeiro_valor.assert_called_once_with() # Se o método foi chamado uma única vez com (*args, **kwargs)
        mock_get_primeiro_valor.assert_any_call() # Se houve alguma chamada do método
        mock_get_primeiro_valor.assert_has_calls([call()]) 
        # Se o método foi chamado a quantidade de vezes e com os argumentos de cada chamada
        mock_metodo_nao_sera_chamado.assert_not_called() # Se o método não foi chamado
        self.assertEqual(mock_get_segundo_valor.call_count, 1) # Quantas vezes o método foi chamado


# Continuaremos no test_mock_7.py