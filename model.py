from estruturadedados import binaryTree as tree
from biometria import biometria as bio
from bancodedados.paths import BIO, VACBIO, VACCPF, VACI, USU

class GerenciadorPrincipal():
    
    def __init__(self):
        self.gerVacina = GerenciadorVacina()
        self.gerUsuario = GerenciadorUsuario()
        self.gerVacinados = GerenciadorVacinados()

    def carregarDados(self):
        pass
    
    def salvarVacina(self):
        pass

    def procurarPessoaCPF(self):
        pass

    def obterListaVacinadosCPF(self):
        self.gerVacinados.obterListaPessoasCPF()
        pass

class GerenciadorVacinados():
    
    def __init__(self):
        self.arvorePessoasCPF = tree.AVL()
        self.arvorePessoasBiometria = tree.AVL()
        self.biometria = bio.Biometria()

    def carregarPessoasCPF(self):
        pass

    def carregarPessoasBiometria(self):
        pass

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







