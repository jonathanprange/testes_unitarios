# Agora vamos além de mockar os métodos que criamos, vamos mockar também o método print
# que é padrão do python.

from unittest import TestCase

from unittest.mock import Mock, patch, call

from app.mock.mock import VendinhaDoZe


class TestComMockTodosComportamentos(TestCase):

    @patch('app.mock.mock.print')
    @patch('app.mock.mock.calculo_valor_total_refrigerantes')
    @patch('app.mock.mock.calculo_valor_total_salgados')
    @patch('app.mock.mock.calculo_valor_total_da_compra')
    def test_imprime_pedido_com_mock_todos_comportamentos(self, mock_valor_total_da_compra, \
                                                                mock_valor_total_salgados, \
                                                                mock_valor_total_refrigerantes, \
                                                                mock_print):

        # Arrange
        nova_vendinha_do_ze = VendinhaDoZe()

        mock_valor_total_refrigerantes.return_value = 100
        mock_valor_total_salgados.return_value = 100
        mock_valor_total_da_compra.return_value = 200

        # Agora iremos ensinar ao nosso mock, como simular o comportamento do método print
        mock_print.side_effect = ['print_1','print_2','print_3','print_4']
            # Como o mesmo método é chamado mais de uma vez, iremos ensinar ao nosso mock
            # como se comportar cada vez que ele for chamado, e fazemos isso através do
            # side_effects, atribuímos então, através de uma lista, todos os retornos
            # que o mock terá.

            # Com isso, ao invés de imprimir no terminal, teremos como verificar se o método
            # print foi chamado, quantas vezes foi chamado e com quais argumentos ele foi chamado
            # a cada vez.


        # Action
        resultado = nova_vendinha_do_ze.imprime_pedido()


        # Assertions
        self.assertEqual(resultado, None)

        mock_valor_total_refrigerantes.assert_called_once_with(0, 2.5)
        mock_valor_total_salgados.assert_called_once()
        mock_valor_total_da_compra.assert_called_once_with(100, 100)

        mock_print.assert_has_calls([call('Seu pedido é: '),
                                    call('0 unidades de  no valor de 100'),
                                    call('0 unidades de  no valor de 100'),
                                    call('O valor total da compra é de R$ 200')])

        # Com o assert_has_calls conseguimos afirmar através do método call, cada uma das chamadas que
        # foram feitas ao mock e quais foram os parâmetros passados para ele.


# Com isso nós conseguimos isolar totalmente o nosso teste, simular e afimar cada um dos comportamentos.

# Continuaremos no test_mock_5.py para verificar mais algumas coisas que podemos fazer com mock.