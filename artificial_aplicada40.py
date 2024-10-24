def quiz():
    questions = [
        {
            "question": "Questão 1/10 - Inteligência Artificial Aplicada\n Como um iniciante na área de ciência de dados, você executou o agrupamento de uma massa de dados utilizando o algoritmo k-means.\n Contudo, você gostaria de ter uma visualização dos agrupamentos obtidos, mas o vetor de atributos de suas instâncias \npossui dimensão 20, o que impede que você plote um gráfico.Você pediu ajuda a colega mais experiente e ele enviou o seguinte trecho de código:\n \nfrom sklearn.decomposition import PCA\ndados_clientes = carrega_dados()\npca = PCA(n_components=2)\npca.fit(dados_clientes)\nUtilizando o seu conhecimento de aprendizagem de máquina, o código enviado irá criar um modelo do tipo PCA e:nVocê pediu ajuda a colega mais experiente e ele enviou o seguinte trecho de código:\nfrom sklearn.decomposition import PCA\ndados_clientes = carrega_dados()\nnpca = PCA(n_components=2)\npca.fit(dados_clientes)",
            "options": [

               " \nA    reduzir a dimensão dos dados"
               " \nB    aumentar a dimensão dos dados"
                "\n C    duplicar a dimensão dos dado"
                "\nD    selecionar uma parte dos dados"
                "\nE    excluir uma parte dos dados"

            ],
            "answer": "A"
        },
        {
            "question": "Questão 2/10 - Inteligência Artificial Aplicada \nClassificadores como o classificador bayesiano pode apresentar uma espécie de desequilíbrio ao obterem valores e confianças excessivamente altos ou \nbaixos para determinadas classes. Sendo necessário um ajuste para evitar que os valores extremos de confiança prejudiquem o processo de predição.",
            "options": [

                "\nA    reajuste"
                "\nB    calibração"
                "\nC    redução"
                "\nD    precisão"
               " \nE    diminuição"



            ],
            "answer": "B"

        },{"question": "Questão 3/10 - Inteligência Artificial Aplicada \nEssa técnica acaba suprindo o problema com muitas combinações. Isso se deve ao fato de testar \ncombinações aleatórias e os melhores resultados funciona como um guia para a escolha dos próximos hiperparâmetros. Contudo, \npercebemos claramente que isso poderá levar em sua maioria, para o mínimo local e não para o mínimo global.”\nO texto acima descreve um procedimento de busca de valores de hiperparâmetros para modelos de redes neurais. Considerando o \ntexto acima e o seu conhecimento sobre treinamento de modelos de aprendizagem, a descrição trata do método:",
            "options": [
               " \nA	FastSearch"
                "\nB	GridSearch"
                "\nC 	k-Search"
                "\nD  RandomSearch"
                "\nE  SimpleSearch"
            ],
            "answer": "D"
           },
        {
            "question": "Questão 4/10 - Inteligência Artificial Aplicada Você foi contratado para o posto de cientista de dados, para compor uma equipe, que atualmente já trabalha com dados, mas não possui \nexperiência em aprendizagem de máquina. Um das suas primeiras tarefas designadas foi a avaliação de modelos treinados.",
            "options": [

                "\nA    deveria ser aumentado o número de camadas"
                "\nB    não havia dados suficientes para treino"
                "\nC    deveria ser utilizando um kNN"
                "\nD    o modelo estava pronto para ser colocado em produção"
                "\nE	as informações das imagens não estavam em concordância"

            ],
            "answer": "E"
        },{
            "question": "Questão 5/10 - Inteligência Artificial Aplicada \n Questão 5/10 - Inteligência Artificial Aplicada\nObserve as afirmações abaixo sobre o tema de algoritmos genéticos (Aula 6):\nI. O operador de seleção é comparável ao que encontramos na natureza sobre a lei da seleção natural, relativo à sobrevivência daqueles que melhor se adaptam ao ambiente.\nII. Um dos métodos mais utilizados para perfazer a seleção é o método da roleta viciada ou roleta ponderada. Esse método dá mais probabilidade para que um indivíduo de maior fitness seja escolhido em contrapartida a outro elemento que tenha menor fitness\nIII. O crossover ou cruzamento ocorre pela mistura de duas soluções ou indivíduos, com o objetivo de criar dois novos indivíduos. Esse cruzamento tende a formar novos indivíduos, que possuem características dos “pais”, e que têm a possibilidade de atender melhor o fitness.\nIV. A mutação embute no AG uma característica totalmente aleatória. Conforme uma taxa especificada no algoritmo, alguns genes dentro dos cromossomos são escolhidos de forma randômica e alterados para outros valores permitidos pelo alfabeto do cromossomo. ",
            "options": [
                "\nA    Somente I e II estão corretas."
                "\nB    Somente II e IV estão corretas."
                "\nC    Somente III e IV estão corretas."
                "\nD    Somente I, II e III estão corretas."
                "\nE    Todas estão corretas."

            ],
            "answer": "E"
        },{
            "question": "Questão 6/10 - Inteligência Artificial Aplicada\nTrata-se de um diagrama que mostra um relacionamento hierárquico entre instâncias. Ele é obtido por meio da execução de um algoritmo de agrupamento hierárquico.",
            "options": [
                "A	um gráfico de desempenho"
                "B	um diagrama de treinamento"
                "C	um diagrama de teste"
                "D    um dendrograma"
                "E    uma gráfico de inércia"
            ],
            "answer": "D"
        },{
            "question": "Questão 7/10 - Inteligência Artificial Aplicada \nMachine Learning atualmente é considerada como uma subárea da Inteligência Artificial, e nós devemos diferenciá-la dos métodos de Inteligência Artificial (IA) que lidam com problemas de busca, \nagentes inteligentes e resolução de problemas, como por exemplo fazer com que o computador consiga definir a melhor jogada em uma partida\n de xadrez ou encontrar a saída de um labirinto.”  ",
            "options": [
               "\nA Uma grande vantagem dos métodos de Machine Learning é que o processo de aprendizagem não depende de visão computacional ligada as estruturas de\n busca mas sim buscas em sistemas especialistas."
               "\nB Machine Learning pode ser compreendida como um conjunto de técnicas ou métodos que permitem às máquinas\naprender por meio de exemplos"
               "\nC A vantagem dos métodos de Machine Learning se perde quando o processo de aprendizagem pode ser\n automatizado, neste caso devemos usar IA clássica"
               "\nD Machine Learning pode ser compreendida como um conjunto de técnicas ou métodos que permitem às máquinas\nobter a capacidade de raciocínio líquido, utilizando o conhecimento armazenado, permitindo novas\nconclusões, durante a comunicação."
            ],
            "answer": "B"
        },{
            "question": "Questão 8/10 - Inteligência Artificial Aplicada\nComo um iniciante na área de ciência de dados, você executou o agrupamento de uma massa de dados utilizando o a\nlgoritmo k-means. Contudo, você gostaria de ter uma visualização dos agrupamentos obtidos, mas o vetor de atributos de suas \ninstâncias possui dimensão 20, o que impede que você plote um gráfico.",
            "options": [

                "\nA    utilizar um algoritmo k - NN"
                "\nB    utilizar apenas 2 características do vetor de atributos"
                "\nC    utilizar um método PCA reduzindo para 2 dimensões"
               "\n D    utilizar uma biblioteca gráfica especializada"
                "\nE    plotar apenas os centroides"
            ],
            "answer": "C"
        },{
            "question": " Questão 9/10 - Inteligência Artificial Aplicada\nEm seu trabalho como cientista de dados, você realizou o treinamento de um modelo de aprendizagem e repassou o modelo treinado para a área de testes. \nApós algum tempo, você recebeu da equipe de testes a seguinte mensagem:",
            "options": [

             "  \nA    reavaliar todos os dados de treino"
               "\nB    transformar os dados de teste em treino e vice - versa"
                "\nC    realizar um novo treinamento, buscando uma melhor generalização do modelo"
                "\nD    treinar um novo modelo e unir ao modelo anterior"
                "\nE    utilizar um outro algoritmo de aprendizagem"

            ],
            "answer": "C"
        },{
            "question": "Questão 10/10 - Inteligência Artificial Aplicada\nUm colega seu de trabalho necessita executar o treinamento de um modelo de \naprendizagem. Para isso ele buscou um enorme dataset na internet, contendo milhares de instâncias. Contudo\n, ele não encontrou nenhuma informação sobre a qualidade dados ou sobre modelos que tenham sido treinados com esse \ndataset. Preocupado, ele pediu a sua opinião.",
            "options": [
                "\nA    não usar a base de dados e denunciar o site que a forneceu"
                "\nB    usar o dataset, pois não havia problemas"
                "\nC    usar o dataset apenas para o treinamento e não para os testes"
                "\nD    avaliar uma amostra do dataset e executar um treinamento de teste nela"
                "\nE    treinar normalmente, pois quantidade é o que importa para o treinamento"


            ],
            "answer": "D"
        },




    ]

    score = 0
    for i, q in enumerate(questions):
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Escolha a alternativa correta: ").strip().upper()
        if answer == q["answer"]:
            print("Você acertou!\n")
            score += 10
        else:
            print(f"Resposta incorreta. A resposta correta é: {q['answer']}\n")

    print(f"Sua pontuação final é: {score}/100")

quiz()
