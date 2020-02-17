# Realizado o teste anterior, e criado um código que passa nesse teste, seguiremos aumentando a quantidade de testes
# para garantirmos que nosso código está preparado para o máximo de cenários possíveis.

# Adicionaremos a assertiva de que caso o número não seja par, o retorno deverá ser False.

# Se executarmos o teste (test_tdd_3.py), para verificar o método criado no arquivo tdd_2.py
# comando no terminal: python -m unittest app/tests/test_tdd_3.py
# Assim executaremos todos os testes unitários que comecem com test_ e que estiverem no arquivo
# test_tdd_3.py

# Teremos o seguinte cenário:

# ********************************************* Retorno do console *********************************************

# $ python -m unittest app/tests/test_tdd_3.py
# F
# ======================================================================
# FAIL: test_se_o_numero_eh_par (app.tests.test_tdd_3.TesteComTdd)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\jonathan.prange\Desktop\Ementa proway\testes_unitarios\app\tests\test_tdd_3.py", line 22, in test_se_o_numero_eh_par
#     self.assertEqual(o_numero_eh_par(3), False)
# AssertionError: None != False

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)

# ******************************************** Retorno do console **********************************************


# Para resolvermos este cenário, devemos garantir que o retorno do método o_numero_eh_par(valor) deve ser False
# quando o valor informado for ímpar.

# Para isso iremos refatorar nosso método até que ele passe no teste determinado.
def o_numero_eh_par(valor):
    # Se o resto da divisão do valor por 2 for igual a zero, retorne True.
    if valor % 2 == 0:
        return True
    else:
    # Se o resto da divisão do valor por 2 for diferente de zero, retorne False.
        return False

# Com essa configuração, conseguimos passar no teste.
# Agora podemos explorar mais cenários que nosso código possa ter, incluir esse cenário nos testes
# e posteriormente fazer nosso código passar nestes novos cenários.


# Continuaremos no arquivo tdd_4.py