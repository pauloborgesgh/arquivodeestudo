def quiz():
    questions = [
        {
            "question": "Determinar o preço de venda torna-se tarefa extremamente importante e constitui-se uma das peças \nfundamentais do planejamento empresarial, pois proporcionará rentabilidade, competitividade, crescimento e retorno do capital \ninvestido. O preço é fator importante na decisão de compra, pois, em mercados competitivos, \no cliente considera seu desembolso financeiro altamente relevante.",
            "options": [
                "\nA    modelo de Regressão Linear"
                "\nB    rede do tipo LSTM"
                "\nC    rede do tipo CNN"
               "\nD    modelo k - Means"
                "\nE    modelo HDBSCAN"
            ],
            "answer": "A"
        },
        {
            "question": "Os modelos de regressão logística e regressão linear,\n apresentam semelhanças, além do nome. No entanto, utilizam funções diferentes para obtenção dos valores, apresentando outras diferenças entre si que determinam \nos diferentes uso para os quais os modelos podem ser aplicados.",
            "options": [
                "\nA	o tipo treinamento"
                "\nB	a predição de valores contínuos e discretos"
               "\nC	vetores de atributos com tamanhos distintos"
                "\nD	as categorias utilizadas"
                "\nE	o número de categorias"
            ],
            "answer": "B"

        },{"question": "Como um iniciante na área de ciência de dados, você recebeu uma tarefa de agrupar um conjunto de dados\n de pessoas, utilizando um algoritmo de agrupamento. Você executou a separação utilizando um tutorial de internet,\n mas os resultados não foram satisfatórios. Buscando melhorar os resultados você pediu\n ajuda a um expert que lhe disse apenas o seguinte: “Altere o seu k-means para usar Manhattan ou Mahalanobis\n”.",
            "options": [
                "\nA  utilizasse outro algoritmo"
                "\nB  utilizasse métricas de distância diferentes"
                "\nC  utilizasse uma outra linguagem de programação"
                "\nD  utilizasse um método supervisionado"
                "\nE  utilizasse um framework"


            ],
            "answer": "B"
           },
        {
            "question": "Questão 4/10 - Inteligência Artificial Aplicada\nVocê foi contratado para o posto de cientista de dados, para compor uma equipe,\n que atualmente já trabalha com dados, mas não possui experiência em aprendizagem de máquina. Um das suas primeiras \ntarefas designadas, foi a explanação de trechos de códigos em linguagem relacionados ao treinamento de modelos de aprendizagem de máquina.\n \n mlp_clf = MLPClassifier(warm_start=True, max_iter=500,\n hidden_layer_sizes=(100,))\n \nFoi substituído por:mlp_clf = MLPClassifier(warm_start=True, max_iter=500,\n \n hidden_layer_sizes=(50,50",
            "options": [
                "\nA    alterar o tipo do classificador"
                "\nB    aumentar a quantidade de camadas da rede"
               "\nC     diminuir a quantidade de camadas da rede"
                "\nD    estabilizar as camadas"
                "\n     Eaumentar o número de nós da rede"

            ],
            "answer": "C"
        },{
            "question": " Questão 5/10 - Inteligência Artificial Aplicada\n Você necessita implementar um módulo de detecção de spam. Como o volume e a \nfrequência de e-mails muito alta, você precisa de um algoritmo de classificação que permita obter de \nforma rápida a identificação se o e-mail recebida se trata ou \nnão de um spam, ainda que alguns falsos positivos possam ocorrer.",
            "options": [
            "\nA	classificador bayesiano"
            "\nB	agrupamento hierárquico"
           "\nC	rede neural profunda"
            "\nD	k-NN"
            "\nE	rede neural do tipo CNN"

            ],
            "answer": "A"
        },{
            "question": "Questão 6/10 - Inteligência Artificial Aplicada\n\n Você foi contratado para o posto de cientista \nde dados, para compor uma equipe, que atualmente já trabalha com dados, mas não possui\n experiência em aprendizagem de máquina. Um das suas primeiras tarefas designadas, foi a\n explanação de trechos de códigos em linguagem relacionados ao treinamento de modelos de aprendizagem de máquina.\n\n\nUm dos trechos que a equipe gostaria de compreender se refere a uma troca de códigos, onde o código:\n\n\np_clf = MLPClassifier(warm_start=True, max_iter=500,\nhidden_layer_sizes=(100,))\nFoi substituído por:\n\nmlp_clf = MLPClassifier(warm_start=True, max_iter=500,\n \nhidden_layer_sizes=(50,50))\n\nA equipe gostaria de saber se essa mudança, iria exigir mais memória. Ou seja, se o número de nós da rede aumentaria.",
            "options": [
                "\nA	irá diminuir"
                "\nB	irá dobrar"
                "\nC	reduzirá pela metade"
                "\nD	permanecerá igual"
                "\nE	irá aumenta"
            ],
            "answer": "B"
        },{
            "question": " Questão 7/10 - Inteligência Artificial Aplicada\nVocê foi contratado para o posto de cientista de dados, para compor uma equipe, que atualmente\n já trabalha com dados, mas não possui experiência em aprendizagem de máquina. Um das suas \nprimeiras tarefas designadas, foi a explanação de n\trechos de códigos em linguagem relacionados ao treinamento de modelos de aprendizagem de máquina.\nUm dos trechos que a equipe gostaria de compreender se refere a uma troca de códigos, onde o código:\n mlp_clf = MLPClassifier(warm_start=True, max_iter=500,\n\n hidden_layer_sizes=(100,50,50))\nFoi substituído por:\n\nmlp_clf = MLPClassifier(warm_start=True, max_iter=500,\n\n hidden_layer_sizes=(50,50))",
            "options": [
                "\nA    alterar o tipo do classificador"
                "\nB    aumentar a quantidade de camadas da rede"
                "\nC    diminuir a quantidade de camadas da rede"
                "\nD    estabilizar as camadas"
               " \nE    aumentar o número de nós da rede"

            ],
            "answer": "C"
        },{
            "question": "Questão 8/10 - Inteligência Artificial Aplicada\nOs modelos de aprendizagem de máquina, necessitam que os dados que lhe são fornecidos sejam \nconvertidos para valores numéricos. Assim, quando temos dados que necessitam de conversão, pode-se utilizar um processo de categorizar uma variável. Representando \ncada possível valor por um número distinto, e que, se possível represente uma relação de hierarquia ou precedência entre os possíveis valores.\nDe acordo com os seus conhecimentos sobre dados categóricos e one-hot encoding, podemos dizer que uma grande diferença entre representar uma variável categórica por valores numéricos e one-hot encoding é:",
            "options": [
                "\nA	que a primeira representa melhor que segunda"
                "\nB	que a segunda representa melhor que a primeira"
                "\nC	a primeira serve apenas determinados tipos de valores"
                "\nD	a segunda serve apenas para determinados tipos de valores"
                "\nE	a segunda cria variáveis derivadas, aumentando o número de atributos"

            ],
            "answer": "E"
        },{
            "question": "Questão 9/10 - Inteligência Artificial Aplicada\n O chefe de uma equipe de ciência de dados recebeu o resultado do treinamento de um modelo de aprendizagem de máquina, conforme a imagem acima.\n De acordo  nos seus conhecimentos de  aprendizagem de máquina, a acurácia deste modelo é de aproximadamente:",
            "options": [
               "\nA	33%"
                "\nB	78%"
                "\nC	14%"
                "\nD	64%"
                 "\nE	100%"

            ],
            "answer": "D"
        },{
            "question": "Questão 10/10 - Inteligência Artificial Aplicada\n Você foi contratado para o posto de cientista de dados, para compor uma equipe, que atualmente já \ntrabalha com dados, mas não possui experiência em aprendizagem de máquina. Um das suas primeiras tarefas designadas, foi planejar um modelo de aprendizagem de máquina para buscar determinar o preço\n de produtos com os quais um cliente trabalha. ",
            "options": [
                "\nA	um classificador bayesiano"
               "\n B	um modelo de regressão linear"
                "\nC	uma classificador do tipo k-NN"
                "\nD	uma rede neural do tipo LSTM"
                "\nE	uma rede neura do tipo CNN"

            ],
            "answer": "B"
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
