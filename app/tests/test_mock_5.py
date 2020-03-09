# Agora vamos mockar também o método input que é padrão do python.

from unittest import TestCase

from unittest.mock import Mock, patch, call, MagicMock

from app.mock.mock import VendinhaDoZe, calculo_valor_total_da_compra, calculo_valor_total_refrigerantes, calculo_valor_total_salgados


class TestInputComMock(TestCase):

    @patch('app.mock.mock.input')
    def test_imprime_pedido_com_mock_todos_comportamentos(self, mock_input):

        # Arrange
        nova_vendinha_do_ze = VendinhaDoZe()

        # Agora iremos ensinar ao nosso mock, como simular o comportamento do método input
        mock_input.side_effect = ['coxinha', 2, 'pepsi', 4]
            # Como o mesmo método é chamado mais de uma vez, iremos ensinar ao nosso mock
            # como se comportar cada vez que ele for chamado, e fazemos isso através do
            # side_effects, atribuímos então, através de uma lista, todos os retornos
            # que o mock terá.

            # Com isso, ao invés de receber um input do terminal, teremos como verificar se o método
            # input foi chamado, quantas vezes foi chamado e com quais argumentos ele foi chamado
            # a cada vez.

            # Além disso, podemos verificar se cada retorno dele foi guardado na variável que 
            # projetamos.


        # Action
        resultado = nova_vendinha_do_ze.realizar_pedido()


        # Assertions
        self.assertEqual(resultado, None)

        mock_input.assert_has_calls([call('Informe um salgado [coxinha/pastel/enroladinho]: '),
                                    call('Informe quantas unidades de salgado: '),
                                    call('Informe um refrigerante [pepsi/sukita/guaraná]: '),
                                    call('Informe quantas unidades de refrigerante: ')])

        # Conseguimos afirmar cada chamada que foi realizada ao método input através do mock que
        # foi chamado no seu lugar.

    
    # Vamos testar agora os outros 3 métodos do arquivo mock.
    def test_calculo_valor_total_salgados(self):
        
        # Action 
        resultado = calculo_valor_total_salgados(10, 3.5)


        # Assertions
        self.assertEqual(resultado, 35.0)

    
    def test_calculo_valor_total_refrigerantes(self):

        # Action
        resultado = calculo_valor_total_refrigerantes(10, 2.5)


        # Assertions
        self.assertEqual(resultado, 25.0)

    
    def test_calculo_valor_total_da_compra(self):

        # Action
        resultado = calculo_valor_total_da_compra(35, 25)


        # Assertions
        self.assertEqual(resultado, 60.0)


# Vamos conhecer mais algumas funcionalidades de mock no arquivo app/tests/test_mock_6.py