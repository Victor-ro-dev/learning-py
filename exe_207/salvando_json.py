# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula127.json'



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), vars(p2), vars(p3)] #Utiliza-se vars para pegar o dict (dicionário) das instancias p1, p2, p3

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    print('FAZENDO DUMP')
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)




