from salvando_json import CAMINHO_ARQUIVO, Pessoa
import json

pessoas = []

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    
    
for pessoa in dados:
    nova_pessoa = Pessoa(pessoa['nome'], pessoa['idade'])
    pessoas.append(nova_pessoa)

for p in pessoas:
    print(f"Nome: {p.nome}, Idade: {p.idade}")
  
