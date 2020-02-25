class Email():
    def __init__(self):
        self.valor = ''

    def set_email(self):
        self.valor = input('Informe seu email: ')

    def get_email(self):
        return self.valor


class Telefone():
    def __init__(self):
        self.valor = ''

    def set_telefone(self):
        self.valor = input('Informe seu telefone: ')

    def get_telefone(self):
        return self.valor


class Imprime():
    def __init__(self, Email, Telefone):
        self.email = Email
        self.telefone = Telefone

    def imprime_email_e_telefone(self):
        print(self.email.get_email())
        print(self.telefone.get_telefone())