# Realizado o teste anterior, e criado um código que passa nesse teste, seguiremos aumentando a quantidade de testes
# para garantirmos que nosso código está preparado para o máximo de cenários possíveis.

# Adicionaremos a assertiva de que caso o valor recebido não seja um inteiro, retorne uma mensagem informando que o tipo
# do dado está errado.

# Se executarmos o teste (test_tdd_4.py), para verificar o método criado no arquivo tdd_3.py

# comando no terminal: python -m unittest app/tests/test_tdd_4.py
# Assim executaremos todos os testes unitários que comecem com test_ e que estiverem no arquivo
# test_tdd_4.py

# Teremos o seguinte cenário:

# ********************************************* Retorno do console *********************************************

# $ py -m unittest app/tests/test_tdd_4.py 
# E
# ======================================================================
# ERROR: test_se_o_numero_eh_par (app.tests.test_tdd_4.TesteComTdd)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\Jonathan\Desktop\Ementa Proway\testes_unitarios\app\tests\test_tdd_4.py", line 29, in test_se_o_numero_eh_par
#     self.assertEqual(o_numero_eh_par('Ronaldo'), 'Erro, o valor informado não é do tipo inteiro.')
#   File "C:\Users\Jonathan\Desktop\Ementa Proway\testes_unitarios\app\tdd\tdd_4.py", line 43, in o_numero_eh_par
#     if valor % 2 == 0:
# TypeError: not all arguments converted during string formatting

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (errors=1)

# ******************************************** Retorno do console **********************************************


# Para resolvermos este cenário, devemos garantir que o retorno do método o_numero_eh_par(valor) deve ser uma mensagem
# de erro quando o valor informado não for do tipo inteiro.

# Para isso iremos refatorar nosso método até que ele passe no teste determinado.
def o_numero_eh_par(valor):
    if not isinstance(valor, int):
    # Se o valor informado não for do tipo inteiro, exibe uma mensagem de erro.
        return 'Erro, o valor informado não é do tipo inteiro.'
    elif valor % 2 == 0:
    # Se o resto da divisão do valor por 2 for igual a zero, retorne True.
        return True
    else:
    # Se o resto da divisão do valor por 2 for diferente de zero, retorne False.
        return False

# Com essa configuração, conseguimos passar no teste.