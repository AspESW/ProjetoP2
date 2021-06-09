from estruturadedados.avltree import AVL as tree
from biometria import biometria as bio
from bancodedados.paths import BIO, VACBIO, VACCPF, VACI, USU
import os

class GerenciadorPrincipal():
    
    def __init__(self):
        self.gerVacina = GerenciadorVacina()
        self.gerUsuario = GerenciadorUsuario()
        self.gerVacinados = GerenciadorVacinados()
        self.gerBiometria = GerenciadorBiometria()

    def carregarDados(self):
        self.gerBiometria.carregarArvore()
    
    def salvarVacina(self):
        pass

    def procurarPessoaCPF(self):
        pass

    def obterListaVacinadosCPF(self):
        self.gerVacinados.obterListaPessoasCPF()

class GerenciadorVacinados():
    
    def __init__(self):
        self.arvorePessoasCPF = tree.AVL()
        self.arvorePessoasBiometria = tree.AVL()
        self.biometria = bio.Biometria()

    def carregarPessoasCPF(self):
        pass

    def carregarPessoasBiometria(self):
        pass

    def associarBiometria(self, vacinado, biometria):
        vacinado.associarBio(biometria)

class GerenciadorBiometria():

    def __init__(self):
        self.arvoreBiometrias = tree.AVL()
        self.listaNomes = self.pegarNomes()
        self.biometria = bio.Biometria()

    def cadastrarBiometria(self):
        self.biometria.criar('_')
        return  self.biometria.somaTotal

    def pegarNomes():
        files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir(path=BIO) if f.endswith('.json')]
        return files_no_ext

    def carregarArvore(self):
        for item in self.listaNomes:
            self.arvoreBiometrias.add(item)

class Pessoa():
    pass 

class PessoaCPF(Pessoa):
    pass

class PessoaDeRua(Pessoa):
    pass

class GerenciadorUsuario():
    pass

class Usuario(Pessoa):
    pass

class GerenciadorVacina():
    pass    

class Vacina():
    pass

g = GerenciadorBiometria()


g.carregarArvore()
g.arvoreBiometrias.inOrder()
print(g.arvoreBiometrias.height())