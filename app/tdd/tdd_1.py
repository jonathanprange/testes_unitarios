# *************** Test Driven Development (Desenvolvimento Orientado por Testes) *************** #

# Primeiro criamos os testes, na sequência criamos o código que atende a condição do teste, depois
# refatoramos e esse ciclo se inicia novamente. 


# Exemplo 1: (Criar um método que verifica se um número é par, retornando True ou False)

    # Para começarmos, iremos criar um método vazio e criarmos os testes para o mesmo
def o_numero_eh_par(valor):
    pass
    # Agora iremos criar o teste para esse método em tests/test_tdd_1.py e depois retornaremos
    # para fazer o teste passar.


# ***************** Retornar somente quando o primeiro teste estiver completo **************** #

# Com o primeiro realizado, vamos executar o comando no terminal:
# python -m unittest app/tests/test_tdd_1.py
# Assim executaremos todos os testes unitários que comecem com test_ e que estiverem no arquivo
# test_tdd_1.py

# Agora que executamos o teste, o mesmo nos retorna uma falha, informando que ele espera que o
# retorno do método seja True, mas que o retorno que ele está recebendo é None. 



# Continuar no tdd_2.py