# O unittest é um framework padrão do python que nos auxilia nos testes unitários,
# para utilizar suas funcionalidades, devemos criar uma pasta com o nome tests,
# dentro dela devemos criar arquivos python onde iremos escrever os nossos testes.
# cada teste unitário será realizado por um método e deverá iniciar seu nome com
# test_ para ser encontrado pelo unittest e executado.

# ************************* Exemplos para serem testados via unittest *****************************

# Método soma
def soma(x, y):
    resultado = x + y
    return resultado

# Método subtração
def subtracao(x, y):
    resultado = x - y
    return resultado

# classe carro
class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca