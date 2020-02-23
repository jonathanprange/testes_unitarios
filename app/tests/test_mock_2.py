# Vamos então importar o framework padrão do python para testes
from unittest import TestCase
# Com o a classe TestCase, agora podemos herdar dela, tudo que precisamos para começar os testes


# Vamos então importar a classe Mock, que faz parte do framework padrão Unittest
from unittest.mock import Mock, patch
# Com o Mock, iremos simular os comportamentos necessários para que nossos testes aconteçam isoladamente,
# garantindo que o teste não terá interferencia externa para funcionar.

# Com o patch, iremos informar para o mock, o caminho do comportamento que ele deve simular.


# Vamos testar a classe VendinhaDoZe, para isso, precisamos importar ela para nossos testes.
from app.mock.mock import VendinhaDoZe

class TestMetodoMock(TestCase):
# Com isso, a classe TestMock, herdou todas as caracteristicas da classe TestCase

    # Agora iremos testar o método imprime_pedido com o mock, para simular todos os 
    # comportamentos dentro do método.

    @patch('app.mock.mock.calculo_valor_total_refrigerantes')
    # Com o @patch, informamos ao mock o caminho do método que será simulado.
    # Esse método que será simulado, devemos passar como parâmetros para uma variável
    def test_imprime_pedido_com_mock(self, mock_valor_total_refrigerantes):
        # Arrange(organizar)
        nova_vendinha_do_ze = VendinhaDoZe()
            # Com o objeto nova_vendinha_do_ze criado, precisamos simular o método que será testado.
            # Dentro do método imprime_pedido, o primeiro método chamado é o calculo_valor_total_refrigerantes()
            # Para simularmos o comportamento deste método, devemos importar o mesmo para dentro do nosso teste
            # para importarmos, devemos utilizar a função patch que faz parte do framework unittest
        
        # Agora que atribuímos o método que queremos simular na variável mock_valor_total_refrigerantes
        # Vamos ensinar ao nosso mock, qual comportamente ele deve ter.
        mock_valor_total_refrigerantes.return_value = 100
            # Com isso, estou dizendo para o mock que quando nosso código chamar o método:
            # calculo_valor_total_refrigerantes(), ao invés de executar esse método, quem será realmente
            # chamado é o mock_valor_total_refrigerantes e que quando o mock_valor_total_refrigerantes
            # for chamado, ele irá retornar para nós o valor 100

            # Dizemos que ensinamos um comportamento ao mock, e sempre que ele for chamado,
            # ele executará esse comportamento.

        # Agora executaremos nosso teste normalmente, mas mudaremos a forma como faremos nossas afirmações.

        # Action (Ação)
        resultado = nova_vendinha_do_ze.imprime_pedido()

        # Assertions (Afirmações)
        self.assertEqual(resultado, None)
            # Fizemos essa afirmação anteriormente, que era o único comportamento que conseguíamos
            # garantir com o nosso teste.

            # Agora iremos ter mais um comportamento para garantir conforme abaixo:
        mock_valor_total_refrigerantes.assert_called_once_with(0 , 2.5)
        # Com essa afirmação, estamos dizendo o seguinte:
        # Confirma para mim que o mock_valor_total_refrigerantes foi chamado uma vez (caso seja chamado
        # mais de uma vez ou não seja chamado, nosso teste quebrará), e que os valores que foram
        # passados como parâmetros, foram o valor 0 e o valor 2.5 (caso os valores forem diferentes
        # dos previstos, o teste quebrará)

        # Por qual motivo estou perguntando se os valores passados foram 0 e 2.5?
        # Se olharmos nosso código, veremos que quando ele é executado, ele passa dois valores como parâmetros
        # que são os valores contidos dentro dos atributos da classe: self.quantidade_de_refrigerantes e
        # self.valor_do_refrigerante.
        # se não informarmos nenhum valor para o self.quantidade_de_refrigerantes, seu valor inicial é 0
        # e inicialmente o self.valor_do_refrigerante tem o valor de 2.5.

        # Então com esse mock, conseguimos garantir que nosso código, terá esse comportamento 
        # visto que o mock simula exatamente o comportamento do método que seria chamado e com isso
        # conseguimos ter certeza de que nosso código faz exatamente o que esperamos que ele faça.


        # Vamos executar o teste e verificar se temos alguma nova informação para avaliarmos.

        # python -m unittest app/tests/test_mock_2.py "ou" py -m unittest app/tests/test_mock_2.py


        # **************************** Resposta do terminal **************************************

        # $ python -m unittest app/tests/test_mock_2.py
        # Seu pedido é: 
        # 0 unidades de  no valor de 0.0
        # 0 unidades de  no valor de 100
        # O valor total da compra é de R$ 100.0
        # .
        # ----------------------------------------------------------------------
        # Ran 1 test in 0.001s

        # OK

        # **************************** Fim da Resposta do terminal ******************************


        # Verificamos com a resposta do terminal que, o valor 100 que ensinamos ao mock como retorno,
        # foi retornado e inclusive impresso no final.

        # Com isso, podemos usar o mock em diversos cenários e simular diversos comportamentos,
        # garantindo que nosso código se comporte exatamente como previsto e em caso de erros,
        # podemos identificar imediatamente uma falha em nosso código que antes só seria identificada
        # na execução do nosso código. 
        
        # Dependendo da complexidade do código, podemos levar meses em um projeto, até que ele esteja
        # pronto para execução e quando isso ocorrer, nosso código provavelmente terá erros,
        # muitos desses erros, além de gerar retrabalho para sua resolução, podem gerar retrabalhos
        # em outras partes de código que dependem diretamente dele.

        # Por esses e outros fatores, a importância dos testes unitários, podemos garantir muitos cenários,
        # prever erros, diminuir retrabalhos e aos poucos, mudar nossa forma de desenvoler,
        # pois um método é muito mais fácil de ser testado, se ele tiver somente uma responsabilidade.

        # Com cada método tendo uma única responsabilidade, conseguimos garantir que nossos métodos
        # não dependam um dos outros para executar suas responsabilidades, logo um erro em um método
        # específico, não tem impacto em outros métodos.

# Vamos continuar no arquivo app/tests/test_mock_3.py