from unittest import TestCase
from unittest.mock import patch, Mock, call

from app.exemplos_mock.exemplos_mock_2 import Email, Telefone, Imprime

class TestExemplosClasses(TestCase):

    # Vamos testar a classe Imprime, ela recebe duas outras classes quando é criada
    # para tornar nosso teste isolado, precisamos mockar as duas classes.
    # Vamos ver como fazer isso:
    
    @patch('app.exemplos_mock.exemplos_mock_2.print')
    def test_class_imprime(self, mock_print):
        # Arrange
        mock_email = Mock()
        mock_email.get_email.return_value = 'ronaldinho_gaucho@gmail.com'
            # Criamos um objeto mock, que tem um método chamado get_email e quando for chamado
            # retornará a string: 'ronaldinho_gaucho@gmail.com'
        mock_telefone = Mock()
        mock_telefone.get_telefone.return_value = '47 98765-4321'
            # Criamos um objeto mock, que tem um método chamado get_telefone e quando for chamado
            # retornará a string: '47 98765-4321'

        # Agora que criamos nossos mock's, vamos usá-los para isolar nosso teste de comportamentos
        # externos.

        nova_impressao = Imprime(mock_email, mock_telefone)
            # Com isso, passamos os objetos mock no lugar dos objetos reais que seriam recebidos pela
            # classe imprime. Como a classe teria dois objetos, com métodos próprios, nós através do mock
            # simulamos os métodos que serão usados pela classe Imprime, assim podemos fazer afirmações
            # quanto as chamadas desses métodos e seus conteúdos.

    

        # Action
        resultado = nova_impressao.imprime_email_e_telefone()
            # Executamos o método que queremos testar

            # no @patch, mockamos o método print que será executado nessa ação, não precisamos 
            # dar um retorno para o mock_print, somente verificar suas chamadas e os argumentos.

        
        # Assertions
        self.assertEqual(resultado, None)
        mock_email.get_email.assert_called_once_with()
        mock_telefone.get_telefone.assert_called_once_with()
        mock_print.assert_has_calls([call('ronaldinho_gaucho@gmail.com'), 
                                     call('47 98765-4321')])

        # Os mocks que criamos foram chamados cada um uma vez, e não foram passados argumentos
        # quando eles foram chamados.

        # O mock do print nos deu uma segunda visualização de que nossos objetos mock estão funcinando,
        # o primeiro print imprimiu o email que ensinamos ao nosso mock_email e o segundo print imprimiu o
        # telefone que ensinamos ao nosso mock_telefone.


# Com essas informações, conseguimos mockar o que criamos, o que é padrão do python e também frameworks,
# micro-frameworks, etc.

# Como tudo em python são objetos, estes objetos podem ser mockados, por consequência os métodos destes
# objetos também podem ser mockados.