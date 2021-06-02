# ProjetoP2
 
	P2 – Braga e Alessandra
	
Tema

    • Sistema para cadastro de pessoas de rua vacinadas. Uma vez que uma pessoa de rua raramente tem identidade ou vai guardar caderneta de vacinação e coisas assim, seria importante armazenar dados significativos para poder encontrar a pessoa novamente ou identificá-la se reencontrá-la.
    • Assuma que será possível usar Biometria, então, vamos simular a biometria através de um arquivo. Assim que a pessoa for inserida no sistema, o seu programa deve gerar um arquivo, que pode ser feito de 255 linhas com 255 números separados por vírgulas. Essa geração é meramente para demonstração então vocês podem repetir os códigos de identidade do usuário ou algo assim.
    •  O sistema deve armazenar as pessoas em um arquivo.
    •  O sistema deve permitir buscas rápidas então deve manter os usuários na memória em uma árvore binária.



Model
	Class Pessoa(super) - Rodrigo
		Atributos:
			Nome
			Idade
			Endereço
			Vacinado
			Vacina			
Class Usuário(sub)
	Atributos:
		Login
		Senha
Class PessoaCPF(sub)
	Atributos:
		CPF
Class PessoaDeRua(sub)
	Atributos:
		Biometria
Class Vacina - Renan
	Atributos:
		Fabricante
		Lote
		Validade
Class BancoDeDados - Almir
	Armazenar e carregar dados
Class Biometria
	Métodos
		Leitura
		Gravação
		Comparação
Class Arvore Binária – Pedro Carvalho
	Controlar a biometria
Class Gerenciador – Pedro Carvalho
	Controlar



View

class Interface – Rafael Pinheiro
	Métodos 
		Menu
		Prints



Controller

class Controlador – Deivid Hugo

	Metodos
		Executar
		Validar input