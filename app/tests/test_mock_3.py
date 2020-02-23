# Agora de forma mais limpa, vamos replicar o conhecimento do mock para os outros dois métodos
# que são chamados pelo método imprime_pedido()

from unittest import TestCase

from unittest.mock import Mock, patch

from app.mock.mock import VendinhaDoZe

class TestComMockDosMetodosCriados(TestCase):

    @patch('app.mock.mock.calculo_valor_total_refrigerantes')
    @patch('app.mock.mock.calculo_valor_total_salgados')
    @patch('app.mock.mock.calculo_valor_total_da_compra')
    def test_imprime_pedido_com_mock_dos_metodos_criados(self, mock_valor_total_da_compra, \
                                                               mock_valor_total_salgados, \
                                                               mock_valor_total_refrigerantes):

        # Primeiro informamos ao mock o caminho de cada um dos métodos que queremos simular e 
        # atribuímos cada um desses caminhos a uma variável.


        # Arrange
        nova_vendinha_do_ze = VendinhaDoZe()

        mock_valor_total_refrigerantes.return_value = 100
        mock_valor_total_salgados.return_value = 100
        mock_valor_total_da_compra.return_value = 200
            # Ensinamos a cada um dos mocks, quais serão seus comportamentos


        # Action
        resultado = nova_vendinha_do_ze.imprime_pedido()
            # Executamos o método a ser testado.


        # Assertions
        self.assertEqual(resultado, None)

        mock_valor_total_refrigerantes.assert_called_once_with(0, 2.5)
        mock_valor_total_salgados.assert_called_once()
            # podemos fazer afirmações da quantidade de vezes que foi chamado, sem a necessidade
            # de perguntarmos com quais parâmetros foi chamado aquele método, mas torna nosso teste
            # mais fraco na questão de garantirmos os comportamentos.
        mock_valor_total_da_compra.assert_called_once_with(100, 100)

        # Conseguimos fazer afirmações para cada um dos métodos mockados, com isso conseguimos inclusive
        # Ver que o retorno do mock_valor_total_refrigerantes e do mock_valor_total_salgados
        # estão sendo passados como parâmetros para o mock_valor_total_da_compra

    
    # Executando nosso teste temos o seguinte cenário:

    # python -m unittest app/tests/test_mock_3.py "ou" py -m unittest app/tests/test_mock_3.py

    # **************************** Resposta do terminal **************************************

    # $ python -m unittest app/tests/test_mock_3.py
    # Seu pedido é: 
    # 0 unidades de  no valor de 100
    # 0 unidades de  no valor de 100
    # O valor total da compra é de R$ 200
    # .
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.001s

    # OK

    # **************************** Fim da Resposta do terminal ******************************


# Se verificarmos a cobertura do nosso teste, agora nosso teste está cobrindo somente o método que está
# sendo testado, no contexto do teste unitário, estamos cada vez mais perto do cenário ideal, onde 
# testamos cada unidade isoladamente.


# Para nosso cenário ficar completamente isolado de comportamentos externos, utilizaremos o mock para
# simular também os 4 métodos print que estão sendo utilizados em nosso código.


# Seguiremos no arquivo test_mock_4.py