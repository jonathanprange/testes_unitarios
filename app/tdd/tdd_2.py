# Agora iremos refatorar nosso método para que a condição do teste seja atendida

def o_numero_eh_par(valor):
    # Se o resto da divisão do valor por 2 for igual a zero, retorne True.
    if valor % 2 == 0:
        return True

    # Agora iremos verificar se o teste para esse método em tests/test_tdd_2.py 
    # é atendido.

# Para verificar, iremos executar o comando no terminal:
# python -m unittest app/tests/test_tdd_2.py
# Assim executaremos todos os testes unitários que comecem com test_ e que estiverem no arquivo
# test_tdd_2.py

# Agora que executamos o teste, ele nos retorna o seguinte:

# ********************************************* Retorno do console *********************************************

# $ python -m unittest app/tests/test_tdd_2.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# ******************************************** Retorno do console **********************************************

# Informando quantos testes foram rodados, quanto tempo eles levaram para executar e o status do teste.

# Caso o retorno seja um "  .  ", significa que o teste passou com sucesso.
# Caso o retorno seja um "  F  ", significa que o teste falhou e será exibida uma mensagem detalhando o motivo da falha.


# Continuar no tdd_3.py