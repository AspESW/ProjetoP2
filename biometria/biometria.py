import random
import os
import json


class Biometria():
    
    def __init__(self):
        self.bio = []
        self.path = './bancodedados/biometrias/'

    def criar(self, nomeArquivo):
        lista = {}
        self.bio = [[random.randint(1, 256) for i in range(1, 255)] for x in range(1, 256)]
        with open(f'{self.path}{nomeArquivo}.json', 'w', encoding='UTF-8') as arquivo:
            for i, line in enumerate(self.bio, 1):
                lista[i] = line
            json.dump(lista, arquivo, indent=4)   
        resultado = self.gerarCodigo(nomeArquivo)
        os.rename(f'{self.path}{nomeArquivo}.json', f'{self.path}{resultado}.json')     

    def leArquivo(self, nomeArquivo):
        listaDeLinhas = []
        with open(f'{self.path}{nomeArquivo}.json', 'r', encoding='UTF-8') as arquivo:
            listaDeLinhas = json.load(arquivo)
        return listaDeLinhas

    def gerarCodigo(self, nomeArquivo):
        listaDeLinhas = self.leArquivo(nomeArquivo)
        valorLinhas = []
        for k in listaDeLinhas.keys():
            linha = listaDeLinhas[k]
            soma = sum(linha)
            valorLinhas.append(soma)
        somaTotal = sum(valorLinhas)
        return somaTotal

    def pegarNomes(self):
        files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir(path=self.path) if f.endswith('.json')]
        return files_no_ext


b = Biometria()
for i in range(10):
    b.criar(f'{i}')

print(b.pegarNomes())