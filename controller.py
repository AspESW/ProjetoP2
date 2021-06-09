from view import *

Intview = Interface()

class Controlador():
    Intview.inicializaInterface()

    def iniciar(self):
        while True:
            opcaoMenu = (Intview.menuPrincipal())
            if (opcaoMenu == "1"):
                Cadrua = Intview.cadastromoradorrua()
                Intview.adicionandobiometria()
                Intview.lendobiometria()
                Intview.cadastrosucesso()
            elif opcaoMenu == "2":
                Cadmor = Intview.cadastromoradornormal()
                Intview.cadastrando()
                Intview.cadastrosucesso()
            elif opcaoMenu == "3":
                Cadvacina = Intview.cadastrovacina()
                Intview.cadastrando()
                Intview.cadastrosucesso()
            elif opcaoMenu == "4":
                Buscar = Intview.buscar()
                if Buscar == "1":
                    Intview.buscarmoradornormal()
                    Intview.procurando()
                elif Buscar == "2":
                    Intview.buscarmoradorderua()
                    Intview.procurando()
                elif Buscar == "3":
                    Intview.buscarvacinas()
                    Intview.procurando()
                elif Buscar == "4":
                    Intview.carregando()
                    Intview.procurando()
                else:
                    Intview.opcaoInvalida()
            elif opcaoMenu == "5":
                Intview.saindodosistema()
                break
            else:
                Intview.opcaoInvalida()
