CONDICAO_TESTE = False

def soma():
    if CONDICAO_TESTE:
        metodo_nao_sera_chamado()
    else:
        valor_1 = get_primeiro_valor()
        valor_2 = get_segundo_valor()
        resultado = valor_1 + valor_2
        return resultado

def get_primeiro_valor():
    primeiro_valor = float(input('Informe o primeiro valor: '))
    return primeiro_valor

def get_segundo_valor():
    segundo_valor = float(input('Informe o segundo valor: '))
    return segundo_valor

def metodo_nao_sera_chamado():
    'Eu não faço nada, sou um exemplo.'

