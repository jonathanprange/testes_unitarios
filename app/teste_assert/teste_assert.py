# **************** Testes unitários sem frameworks ***********************

# Python tem uma palavra reservada chamada assert.

# ******************** Funcionamento do assert ***************************

# assert <valor> <condição> <valor>

# A palavra reservada assert verifica se o resultado da condição é verdadeiro

# Se a condição é atendida (resultado True), ele prossegue.
# Se a condição não é atendida (resultado False), ele gera um erro.

# ***************************** Exemplos *********************************

# 1 - assert com condição verdadeira:
assert True
assert 3 == 3
assert 3 < 5
assert 'Ronaldo' == 'Ronaldo'
# Executando o python no terminal, nenhum erro acontece, afirmando que todas as
# condições são verdadeiras.


# 2 - assert com condição falsa
assert 3 == 5
assert 'Ronaldo' == 'Ronaldinho'
assert False
# Executando o python no terminal, a primeira condição incorreta (assert 3 == 5)
# gera um erro, encerrando a execução.

# Resposta do terminal

###     assert 3 == 5
###     AssertionError



# 3 - assert com condição falsa + mensagem de exibição
assert 3 == 5 , 'o primeiro valor não é igual ao segundo valor'
# Executando o python no terminal, quando a condição estiver incorreta,
# será exibida a mensagem padrão descrita após a vírgula.