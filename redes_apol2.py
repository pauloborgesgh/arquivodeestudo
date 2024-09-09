# Dicionário contendo as questões, opções e a resposta correta
questoes = [
    {
        "enunciado": "Questão 1/10 - Redes de Computadores",
        "texto": """Uma das atribuições da camada de enlace, além do processo de encapsulamento e desencapsulamento dos pacotes recebido, é o controle de acesso ao meio...
                    A respeito dessas asserções, assinale a opção correta.""",
        "opcoes": [
            "A) As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.",
            "B) As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.",
            "C) A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.",
            "D) A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.",
            "E) Tanto a primeira quanto a segunda asserções são proposições falsas."],
        "correta": "B"
    },
    {
        "enunciado": "Questão 2/10 - Redes de Computadores",
        "texto": """Os dispositivos de segurança deverão garantir a proteção tanto para as possíveis ameaças que possam existir nas redes LAN quanto em relação às ameaças existentes na rede externa...
                    A respeito dessas asserções, assinale a opção correta.""",
        "opcoes": [
            "A) As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.",
            "B) As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.",
            "C) A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.",
            "D) A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.",
            "E) Tanto a primeira quanto a segunda asserções são proposições falsas."],
        "correta": "C"
    },

    {"question": "Questão 3/10 - Redes de Computadores\n\nQuando estamos navegando na internet, normalmente acessamos vários sites simultaneamente, abrindo várias abas em novas janelas. Cada nova aba que abrimos estabelece uma nova comunicação com um site diferente, ou seja, novas sessões são abertas. Este processo ocorre na camada de sessão, que é a camada cinco do modelo OSI, responsável por abrir estas novas sessões de comunicação com vários destinos diferentes.\n\nConsiderando este processo de abertura de sessões e as características da operação da camada de sessão, avalie as asserções a seguir.\n\nI. Para cada novo processo de comunicação do computador do usuário com um outro servidor externo, será aberta uma nova sessão com um número de porta, estabelecido pela camada de transporte.\n\nPORQUE\n\nII. As sessões devem ser identificadas pela camada de rede, sendo que este número de porta é que será utilizado pelo protocolo para identificar o destinatário da sessão.\n\nA respeito dessas asserções, assinale a opção correta.",
        "options": [
            "A) As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.",
            "B) As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.",
            "C) A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.",
            "D) A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.",
            "E) Tanto a primeira quanto a segunda asserções são proposições falsas."
        ],
        "answer": "C"
    },
    {
        "question": "Questão 4/10 - Redes de Computadores\n\nUm dos meios de transmissão empregados em redes são as fibras ópticas, sendo que temos dois tipos diferentes de fibras, que são as fibras monomodo (SMF - Single-mode fiber) e as fibras multimodo (MMF - Multimode fiber). Porém, em relação à sua estrutura, estes dois tipos de fibras são constituídos de três elementos distintos, que são o núcleo, a casca e o revestimento. A transmissão dos sinais óticos ocorre de tal forma que o sinal óptico vai sofrendo a reflexão na interface entre o núcleo e a casca, sendo propagado ao longo do cabo óptico. Este conjunto é protegido por um revestimento, para evitar que elementos externos afetem o processo de propagação do sinal ou alterem as características através de reação química com algum outro material.\n\nConsiderando este processo de propagação do sinal óptico, e as características das fibras monomodo e multimodo, avalie as asserções a seguir.\n\nI. A fibra multimodo (MMF) permite a propagação do sinal óptico por distâncias muito maiores do que a fibra monomodo (SMF), sendo mais adequada para uso em redes de longa distância.\n\nPORQUE\n\nII. A fibra multimodo tem um núcleo de 50 ou de 62,5 micrometros, que é maior do que o núcleo da fibra monomodo, que é de aproximadamente 8 a 10 micrometros, permitindo diversos ângulos de injeção do sinal óptico.\n\nA respeito dessas asserções, assinale a opção correta.",
        "options": [
            "A) As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.",
            "B) As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.",
            "C) A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.",
            "D) A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.",
            "E) Tanto a primeira quanto a segunda asserções são proposições falsas."
        ],
        "answer": "D"
    },
    {
        "question": "Questão 5/10 - Redes de Computadores\n\nConsiderando as características das topologias típicas utilizadas nas redes WAN, conforme visto na rota, avalie as afirmações a seguir:\n\nI. Na topologia em estrela, todo o tráfego da rede passa por um único dispositivo, que está conectado, através de links dedicados, aos demais dispositivos.\n\nII. O custo de uma topologia em estrela torna esta topologia viável apenas para redes com poucos dispositivos, pois o número de links necessários, para a conexão com o dispositivo central, se torna muito elevado, para redes maiores.\n\nIII. A topologia em malha completa é a que apresenta a maior simplicidade de implementação e a maior disponibilidade, sendo a mais empregada nas redes.\n\nIV. Podemos ter uma topologia lógica do tipo ponto a ponto, entre dois equipamentos de rede, porém, com vários caminhos entre eles, tal como ocorre com uma topologia física em malha completa, por exemplo.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I e IV.",
            "E) I, III e IV."
        ],
        "answer": "C"
    },
    {
        "question": "Questão 6/10 - Redes de Computadores\n\nPara a implementação da confiabilidade de uma rede, ou seja, para garantir que a conectividade entre os clientes e os servidores de aplicações seja garantida, com a qualidade necessária e no momento em que o usuário necessitar acessar estas aplicações, vários requisitos devem ser atendidos por esta rede. Assim, as quatro características básicas de uma rede, para que ela seja considerada confiável, são a escalabilidade, a tolerância a falhas, a Qualidade de Serviço (QoS) e a segurança.\n\nAssim, para atender ao requisito de escalabilidade, avalie as características descritas a seguir e identifique quais estão efetivamente relacionadas à escalabilidade:\n\nI. Um equipamento de rede, com apenas duas portas de conexão, tal como um roteador residencial, não atenderá o requisito de escalabilidade, pois não terá redundância de conectividade.\n\nII. O equipamento utilizado para a conexão de uma rede residencial à Internet não é escalável, pois o Firewall instalado possui limitações na configuração das regras de bloqueio de tráfego.\n\nIII. Um equipamento utilizado em uma rede residencial, para atender alguns clientes, poderá não ser adequado para uma rede corporativa, para atender a conexão de muitos usuários, ou seja, não atenderia o requisito de escalabilidade.\n\nIV. O protocolo da rede wireless, conhecido como padrão WiFi, é dito escalável, pois pode ser utilizado tanto em uma rede residencial quanto em uma rede corporativa.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I e IV.",
            "E) I, III e IV."
        ],
        "answer": "E"
    },
    {
        "question": "Questão 7/10 - Redes de Computadores\n\nUma das classificações empregadas para diferenciar as redes de computadores está associada aos recursos disponibilizados e aos tipos de usuários que têm permissão para acessar estes recursos. Assim, a partir destas características, são definidos três tipos de redes: a Intranet, a Extranet e a Internet.\n\nA Intranet pode ser considerada basicamente uma rede WAN de acesso restrito, diferentemente da Internet, que é uma rede de acesso aberto. Por isso a rede do tipo Intranet também é chamada de rede privada. Considerando as características de uma rede do tipo Intranet, conforme apresentado acima e também no texto da rota, avalie as afirmações a seguir:\n\nI. A Internet pode ser considerada uma Intranet, quando o terminal do usuário está acessando um servidor WEB da empresa.\n\nII. Para a implementação da Intranet, as empresas contratam o serviço de uma empresa de telecomunicações, ou, ainda, de um provedor de Internet.\n\nIII. Um dos protocolos empregados na implementação de uma Intranet é o protocolo IP/MPLS (IP multi-protocol label switching).\n\nIV. Uma Extranet é formada pela conexão de várias Intranets, semelhante à conexão das redes LAN através de uma rede WAN.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I, II e IV.",
            "E) I, III e IV."
        ],
        "answer": "C"
    }, {
        "question": "Questão 8/10 - Redes de Computadores\n\nQuando enviamos um e-mail, estamos utilizando um processo de comunicação onde temos os três componentes básicos: transmissor, receptor e o meio de transmissão. O transmissor será o terminal do usuário que está enviando o e-mail e o receptor será o servidor de e-mail que receberá o e-mail. O meio de transmissão será a rede de computadores, que é a Internet. Mas neste processo de comunicação, existem outros componentes, que incluem o processo de codificação e de decodificação.\n\nE como a Internet é uma rede de dados digitais, considere o processo de adequação da mensagem a este meio de comunicação e avalie as afirmações a seguir:\n\nI. Os pacotes que serão transmitidos através da rede de dados conterão a mensagem de texto, após esta mensagem ser digitalizada pelo transmissor.\n\nII. Para a transmissão da mensagem, é necessário que os elementos que formam a rede, ou seja, que implementam o meio físico, compreendam qual foi o processo de digitalização da mensagem.\n\nIII. O receptor da mensagem deverá estar conectado diretamente ao transmissor, através de um meio dedicado, pois a transmissão é realizada apenas entre terminais idênticos.\n\nIV. Para que o destinatário consiga interpretar a mensagem enviada pelo transmissor, é necessário que ocorra o processo de decodificação da mensagem, no terminal do receptor, de acordo com o processo de codificação realizado pelo transmissor.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I e IV."
        ],
        "answer": "D"
    },
    {
        "question": "Questão 9/10 - Redes de Computadores\n\nNo modelo em camadas, na Camada Física, que é a camada um do modelo OSI, é onde ocorre a codificação dos sinais, para que eles sejam transmitidos adequadamente através do meio físico empregado para a conexão entre dois terminais. E o protocolo a ser utilizado, para realizar a transmissão dos dados digitais, dependerá do meio físico empregado para a conexão dos dispositivos de rede, que pode ser implementado com cabos de cobre, ondas de rádio frequência ou fibra óptica.\n\nEm relação ao meio físico fibra óptica, avalie as características descritas a seguir, e identifique quais estão efetivamente relacionadas ao seu uso:\n\nI. A fibra óptica já é empregada na comunicação nas redes WAN há muito tempo, pois estas redes devem cobrir grandes distâncias e possuem maior capacidade de transmissão.\n\nII. O custo do cabo óptico não viabiliza a sua utilização em redes locais, que são as redes LAN, sendo obrigatória a utilização de cabos de cobre blindados, quando é necessária a passagem dos cabos em um ambiente com muito ruído eletromagnético.\n\nIII. Comparativamente, os cabos de fibra óptica apresentam uma maior atenuação do que os cabos metálicos, e por este motivo não são utilizados em redes que exigem uma maior capacidade de transmissão.\n\nIV. A capacidade de transmissão da fibra óptica, em relação à largura de banda, também é um grande diferencial deste meio físico em comparação aos cabos de cobre e redes wireless, apresentando uma capacidade muito maior do que estes outros dois tipos de meios físicos.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I e IV.",
            "E) I, III e IV."
        ],
        "answer": "D"
    },
    {
        "question": "Questão 10/10 - Redes de Computadores\n\nA identificação dos terminais, no protocolo Ethernet, é realizada através do endereço MAC Ethernet, que consiste de um conjunto de dígitos representados em hexadecimal. Assim, o endereço MAC Ethernet é, normalmente, representado por um valor hexadecimal com 12 dígitos hexadecimais.\n\nAlém do endereço individual de cada dispositivo, o protocolo Ethernet possibilita a identificação de um conjunto de destinatários, através do endereço MAC de broadcast, que é utilizado quando desejamos que todos os terminais conectados em uma rede processem o quadro de dados. Assim, considerando este processo de comunicação do protocolo Ethernet, avalie as afirmações a seguir:\n\nI. Para que todos os dispositivos que receberem o quadro façam o seu processamento, o endereço MAC de destino a ser utilizado é o endereço de Broadcast.\n\nII. O endereço MAC de broadcast dependerá do endereçamento de rede, que é o endereçamento IP, utilizado em cada rede LAN.\n\nIII. O endereço atribuído a cada interface de rede, pelo fabricante do equipamento, é o endereço chamado de unicast.\n\nIV. O endereço utilizado para o envio de tráfego para um determinado conjunto de destinatários é chamado de endereço de multicast.\n\nÉ correto apenas o que se afirma em:",
        "options": [
            "A) I e II.",
            "B) II e III.",
            "C) III e IV.",
            "D) I, II e IV.",
            "E) I, III e IV."
        ],
        "answer": "E"
    }

]


# Função para apresentar as questões e avaliar respostas
def aplicar_simulado(questoes):
    acertos = 0
    total_questoes = len(questoes)

    for i, questao in enumerate(questoes):
        print(f"{questao['enunciado']}\n")
        print(f"{questao['texto']}\n")
        for opcao in questao["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta: ").upper()

        if resposta == questao["correta"]:
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Incorreto! A resposta correta é: {questao['correta']}\n")

    print(f"Você acertou {acertos} de {total_questoes} questões.")


# Executando o simulado
aplicar_simulado(questoes)
