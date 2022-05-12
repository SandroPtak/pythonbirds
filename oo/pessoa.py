class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Sandro = Pessoa(nome='Sandro')
    Batata = Pessoa(Sandro, nome='Batata')
    print(Pessoa.cumprimentar(Batata))
    print(id(Batata))
    print(Batata.cumprimentar())
    print(Batata.nome)
    print(Batata.idade)
    for filho in Batata.filhos:
        print(filho.nome)
