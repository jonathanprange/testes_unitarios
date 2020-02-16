# Todos os testes unitários derivam do assert, tanto sem framework quanto com framework
# todos os testes terão uma assertiva, afirmando que a condição entre dois valores é
# verdadeiro. Caso a assertiva falhe, um erro é exibido.

# ************************* Testes unitários sem framework ****************************

# Exemplo 1 (método de soma):

def soma(x , y):
    resultado_da_soma = x + y
    return resultado_da_soma

# assert com condição verdadeira
assert soma(2 , 2) == 4
# Executando o python no terminal, nenhum erro acontece, afirmando que a condição é verdadeira.

# assert com condição falsa
assert soma(2, 3) == 3, 'o resultado da soma não é igual ao valor esperado'
# Executando o python no terminal, a condição incorreta gera um erro, encerrando a execução
# e exibindo a mensagem de erro descrita após a vírgula.


# Exemplo 2 (classe pessoa):

class Pessoa:
    nome = ''

nova_pessoa = Pessoa()
nova_pessoa.nome = 'Jonathan'

assert nova_pessoa.nome == 'Jonathan'
# Executando o python no terminal, nenhum erro acontece, afirmando que a condição é verdadeira.


# Exemplo 3 (classe carro):
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

novo_carro = Carro('Celta')

assert isinstance(novo_carro, Carro)
assert novo_carro.modelo == 'Celta'
# Executando o python no terminal, nenhum erro acontece, afirmando que as condições são verdadeiras.