


class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None


def inserirSemPrioridade(self, nodo):
    if self.head is None:
        self.head = nodo
    else:
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = nodo


def inserirComPrioridade(self, nodo):
    if self.head is None or self.head.cor == 'V':
        nodo.proximo = self.head
        self.head = nodo
    else:
        atual = self.head
        while atual.proximo is not None and atual.proximo.cor == 'A':
            atual = atual.proximo
        nodo.proximo = atual.proximo
        atual.proximo = nodo


def inserir(self):
    cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
    numero = int(input("Digite o número do cartão: "))
    nodo = Nodo(numero, cor)

    if self.head is None:
        self.head = nodo
    elif cor == 'V':
        self.inserirSemPrioridade(nodo)
    elif cor == 'A':
        self.inserirComPrioridade(nodo)


def imprimirListaEspera(self):
    atual = self.head
    while atual is not None:
        print(f'Cartão: {atual.numero}, Cor: {atual.cor}')
        atual = atual.proximo


def atenderPaciente(self):
    if self.head is None:
        print("Não há pacientes na fila de espera.")
    else:
        print(f'Chamando paciente com cartão numero {self.head.numero}')
        self.head = self.head.proximo


def menu(self):
    while True:
        print("1 – Adicionar paciente a fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            self.inserir()
        elif opcao == 2:
            self.imprimirListaEspera()
        elif opcao == 3:
            self.atenderPaciente()
        elif opcao == 4:
            print("Encerrando o programa.")
            break
        else:
            print("Opção invalida, por favor tente novamente.")


class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        numero = int(input("Digite o número do cartão: "))

        nodo = Nodo(numero, cor)

        if self.head is None:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head

        while atual is not None:
            print(f'[Cor: {atual.cor},Cartão: {atual.numero}]')
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila de espera.")
        else:
            print('Chamando Paciente...')
            print(f'Cartão Cor: {self.head.cor} número {self.head.numero} ')
            self.head = self.head.proximo

    def menu(self):
        while True:
            print("------------------------------")
            print("1 – Adicionar paciente a fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar paciente")
            print("4 – Sair")
            print("------------------------------")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                self.inserir()
            elif opcao == 2:
                self.imprimirListaEspera()
            elif opcao == 3:
                self.atenderPaciente()
            elif opcao == 4:
                print("Encerrando o programa.")
                break
            else:
                print("Opção invalida, por favor tente novamente.")


if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.menu()


