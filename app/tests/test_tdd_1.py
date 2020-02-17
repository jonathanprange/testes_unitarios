# Importamos o TestCase, para tornarmos nosso teste unitário mais dinâmico
from unittest import TestCase

# Importamos o método que queremos testar
from app.tdd.tdd_1 import o_numero_eh_par

# Criamos uma classe de nome TesteComTdd, para fixarmos a ideia do TDD
class TesteComTdd(TestCase):
    
    # Criaremos o teste, afirmando quais serão as condições que o método deverá atender
    # para que o teste passe com sucesso.
    def test_se_o_numero_eh_par(self):
        # Com este assert, iremos garantir que o método que está sendo testado,
        # deverá resolver a afirmação de que ao chamar o método, o retorno deverá
        # ser True.
        self.assertTrue(o_numero_eh_par(2))
        # Agora, somente continuaremos os testes com TDD, quando conseguirmos fazer o 
        # método o_numero_eh_par(valor) passar no teste.