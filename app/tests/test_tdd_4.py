# Importamos o TestCase, para tornarmos nosso teste unitário mais dinâmico
from unittest import TestCase

# Importamos o método que queremos testar
from app.tdd.tdd_4 import o_numero_eh_par

# Criamos uma classe de nome TesteComTdd, para fixarmos a ideia do TDD
class TesteComTdd(TestCase):
    
    # Criaremos o teste, afirmando quais serão as condições que o método deverá atender
    # para que o teste passe com sucesso.
    def test_se_o_numero_eh_par(self):
        # Com este assert, iremos garantir que o método que está sendo testado,
        # deverá resolver a afirmação de que ao chamar o método, o retorno deverá
        # ser True.
        self.assertTrue(o_numero_eh_par(2))

        # Com este segundo assert, iremos garantir que o método que está sendo testado,
        # deverá resolver a afirmação de que ao chamar o método com um número ímpar,
        # o retorno deverá ser False

        self.assertEqual(o_numero_eh_par(3), False)

        # Com este terceiro assert, iremos garantir que o método que está sendo testado,
        # deverá resolver a afirmação de que ao chamar o método com um valor que não seja,
        # um número inteiro, o retorno deverá ser uma mensagem informando que o tipo está
        # errado

        self.assertEqual(o_numero_eh_par('Ronaldo'), 'Erro, o valor informado não é do tipo inteiro.')

