# Definindo a estrutura de um Nodo para a lista encadeada
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == 'DF':
            return 7
        else:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % 10

    def inserir(self, sigla, nomeEstado):
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo


    def imprimir(self):
        for i in range(10):
            print(f" {i}: ", end="")
            nodo = self.tabela[i]
            while nodo:
                print(f"{nodo.sigla} -> ", end="")
                nodo = nodo.proximo
            print("None")



def inserir_estados(tabela):
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"), ("GO", "Goiás"), ("MA", "Maranhão"),
        ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
        ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"),
        ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"),
        ("SC", "Santa Catarina"), ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"),
        ("PB", "Paulo Borges")
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)



tabela_hash = TabelaHash()


inserir_estados(tabela_hash)

tabela_hash.imprimir()
