def quiz():
    questions = [
        {
            "question": "Questão 1/10 - Redes de Computadores\nO protocolo TCP, por operar na camada de transporte, realiza a segmentação dos dados da camada superior, identificando cada um dos segmentos gerados com a inserção de um identificador. Esse identificador é chamado de número de sequência e será inserido no cabeçalho dos segmentos gerados, sendo que o número de sequência inicial, para uma nova transmissão, é gerado de maneira aleatória.\n\nA partir deste número de sequência, o protocolo TCP poderá realizar a verificação dos segmentos recebidos, identificando eventuais perdas de pacotes no processo de transmissão. Avalie as afirmações a seguir:\n\nI. Para a transmissão de dados do servidor para múltiplos clientes, simultaneamente, é necessário sincronizar os números de sequência e de confirmação entre todos os clientes.\nII. Caso ocorram perdas, o processo de reordenamento irá preencher a falta de um pacote com a cópia do pacote seguinte, evitando a quebra de sequência do identificador.\nIII. A cada segmento enviado, o número de sequência é incrementado, somando-se o número de bytes transmitidos neste novo segmento, para que o próximo segmento contenha a sequência correta dos próximos bytes.\nIV. O número de sequência também possibilita implementar a confiabilidade, pois a perda de pacotes poderá ser detectada através deste mecanismo de identificação dos pacotes.\n\nÉ correto apenas o que se afirma em:",
            "options": [
                "A. I e II.",
                "B. II e III.",
                "C. III e IV.",
                "D. I, II e IV.",
                "E. I, III e IV."
            ],
            "answer": "C"
        },
        {
            "question": "Questão 2/10 - Redes de Computadores\nNo modelo em camadas, uma das camadas é a camada de Rede, que é a camada três do modelo OSI, e que equivale à camada de Internet no modelo TCP/IP. Avalie as afirmações a seguir e identifique quais estão efetivamente relacionadas ao processo de comunicação da camada de rede:\n\nI. Os pacotes da camada de rede são encaminhados através dos dispositivos intermediários, como roteadores, em função da informação contida nestes pacotes, mantendo-os inalterados ao longo do caminho.\nII. Para que ocorra a comunicação na camada de rede, é necessário que o switch local da rede LAN altere o conteúdo do pacote de rede para que ele seja encaminhado corretamente para o roteador local.\nIII. Os dispositivos intermediários de rede, como roteadores, processam os pacotes e alteram suas informações de acordo com o caminho pelo qual os pacotes deverão ser encaminhados.\nIV. O roteador local, na maioria dos casos, fará a alteração das informações da camada de enlace, pois os protocolos utilizados na rede LAN e na rede WAN na camada dois provavelmente serão diferentes.\n\nÉ correto apenas o que se afirma em:",
            "options": [
                "A. I e II.",
                "B. II e III.",
                "C. III e IV.",
                "D. I e IV.",
                "E. I, III e IV."
            ],
            "answer": "D"

        },{"question": "Questão 3/10 - Redes de Computadores\nAlém do controle de fluxo, uma das funções da camada de transporte é garantir a confiabilidade do processo de comunicação. E para isto, o mecanismo básico consiste no reenvio dos segmentos que foram eventualmente descartados, de forma que a aplicação nem perceberá esta perda de pacotes. Assim, antes de entregar os dados para a camada de aplicação, poderá ser feita a correção deste erro, com a retransmissão dos pacotes perdidos.\nConsiderando o processo de controle de fluxo da camada de transporte, apresentado no texto da rota, avalie as asserções a seguir.\nI. Para a identificação da perda de pacotes, é utilizado um número sequencial, inserido nos pacotes, permitindo que o receptor analise esta informação e identifique eventuais segmentos faltantes.\nII. Caso seja detectada a falta de um pacote, o receptor poderá fazer a solicitação de reenvio para o transmissor, de forma a corrigir esta perda.\nIII. O controle de fluxo é estabelecido a partir do número de segmentos recebidos, que é aumentado cada vez que ocorre uma perda de pacotes.\nIV. A confiabilidade do processo é garantida pois, caso algum pacote seja perdido no processo de transmissão, ele poderá ser retransmitido.\nÉ correto apenas o que se afirma em",
            "options": [
                "A    I e II"
                "B    II e III."
                "C    III e IV."
                "D    I, II e IV."
                "E    I, III e IV"


            ],
            "answer": "D"
           },

        {
            "question": " Questão 4/10 - Redes de Computadores\nUma das tarefas realizadas pelo protocolo TCP é o controle de fluxo, que irá garantir que os terminais que estão executando o protocolo TCP possam receber e processar os dados de forma confiável.Assim, o TCP realiza o controle de fluxo, ajustando a taxa de envio de dados entre o remetente e o destinatário, durante o processo de comunicação em uma determinada sessão. Desta forma, considerando a operação do protocolo TCP, em relação ao processo de controle de fluxo, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nI. O protocolo TCP insere, em seu cabeçalho, um campo identificado como tamanho de janela, que representa o número de bytes que o dispositivo de destino de uma sessão TCP pode aceitar e processar, antes de enviar a solicitação para o envio de mais segmentos.\nPORQUE\nII. Com esta informação, os dispositivos de rede, tal como os roteadores, irão definir a prioridade destes pacotes, priorizando o fluxo deste tráfego.\nA respeito dessas asserções, assinale a opção correta.:",
            "options": [
               " A    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
               " B    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira."
                "C    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
                "D    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
                "E    Tanto a primeira quanto a segunda asserções são proposições falsas."
            ],
            "answer": "C"
        },{
            "question": "Questão 5/10 - Redes de Computadores \nOs protocolos da camada de transporte inserem as informações necessárias, para a implementação das suas funções, em campos específicos, que são acrescidos ao cabeçalho de cada segmento transmitido.\nAssim, considerando o cabeçalho gerado pelo protocolo TCP, que possui um tamanho total de 20 bytes, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nI. Para cada segmento gerado será necessária a inserção de um cabeçalho TCP, que conterá os campos de Porta de Origem e Porta de Destino, entre outros.\nII\n. Dois campos que são inseridos no cabeçalho TCP são o Número de Sequência e o Número de Confirmação, que identificam a ordem dos segmentos.\nIII. Um dos campos inseridos no cabeçalho TCP é o Endereço IP do destinatário, para que este segmento seja encaminhado pela rede corretamente.\nIV. Caso seja necessário dividir o segmento em segmentos menores, para adequar aos protocolos da camada inferior, será inserido no cabeçalho TCP o campo que identifica o Número do Fragmento.\nÉ correto apenas o que se afirma em",
            "options": [
             "A  I e II. "
             "B  II e III."
             "C  III e IV."
             "D  I, II e IV."
             "E  I, III e IV."

            ],
            "answer": "A"
        },{
            "question": "Questão 6/10 - Redes de ComputadoresUma das camadas, descritas no modelo de rede, e que fica localizada acima da camada de rede, é a camada de transporte. E esta camada possui a mesma identificação tanto no modelo OSI quanto no modelo TCP/IP, possuindo as mesmas atribuições nos dois modelos.\nAssim, considerando as características da camada de transporte, conforme visto na rota, avalie as afirmações a seguir.\nI. Uma das funções da camada de transporte é estabelecer as sessões de comunicação, de maneira temporária, entre as aplicações, permitindo a transferência de dados entre estas sessões.\nII. Como a camada de transporte não tem como função realizar o controle de fluxo, esta tarefa deverá ser executada pelas camadas superiores, tal como a camada de aplicação.\nIII. Para que sejam identificadas as conversas de camadas superiores, a camada de rede deverá fornecer, para a camada de transporte, o endereço IP de cada conexão.\nIV. Uma das tarefas das camada de transporte é realizar a segmentação dos dados recebidos da camada superior, para adequá-los à estrutura de pacote da camada de rede.\nÉ correto apenas o que se afirma em",
            "options": [
               " A    I e II."
                "B    II e III."
                "C    III e IV."
               "D    I e IV."
               " E    I, III e IV."
            ],
            "answer": "D"
        },{
            "question": "Questão 7/10 - Redes de Computadores Uma das funções da camada de transporte é realizar a interface entre as aplicações e a camada de rede, e assim adequar os dados a serem transmitidos, de acordo com a demanda das aplicações, para que possam ser encapsulados corretamente pelo protocolo de camada de rede. E uma das características associadas a este processo de encapsulamento é o tamanho do conteúdo da carga nestes pacotes, o que dependerá do protocolo que está sendo utilizado na camada de rede.\nConsiderando este processo de encapsulamento, e as características de operação de um protocolo da camada de transporte, apresentadas no texto da rota, avalie as asserções a seguir.\nI. O modelo em camadas define que os protocolos, que operam em cada uma das camadas, deverão seguir um padrão único em relação ao tamanho do conteúdo de carga que eles suportam.\nPORQUE\n\nII. A quantidade de dados a serem transmitidos pelo protocolo de rede pode ser maior do que o tamanho dos pacotes da camada de rede, sendo necessário dividir estes dados em segmentos.\nA respeito dessas asserções, assinale a opção correta.",
            "options": [
                "A    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
                "B    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira."
                "C    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
               " D    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
            ],
            "answer": "D"
        },{
            "question": "Questão 8/10 - Redes de Computadores\nUm dos protocolos mais utilizados na camada de transporte, nas redes de dados, é o protocolo TCP, que deverá então executar a multiplexação das aplicações das camadas superiores, garantir a confiabilidade do processo de comunicação e realizar o controle de fluxo.\nAssim, considerando a operação do protocolo TCP, em relação ao processo de multiplexação, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nIII. O protocolo TCP insere, em seu cabeçalho, os campos que contém os identificadores de porta de origem e porta de destino, que possuem um comprimento de 16 bits cada um deles.\nPORQUE\n\nIV. Com esta informação o destinatário dos segmento TCP poderá identificar para qual das aplicações ele deverá encaminhar o conteúdo dos dados, que foram recebidos dentro do segmento.\nA respeito dessas asserções, assinale a opção correta.",
            "options": [
                "A    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
                "B    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira"
                "C    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
                "D    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
                "E    Tanto a primeira quanto a segunda asserções são proposições falsas"

            ],
            "answer": "A"
        },{
            "question": "Questão 9/10 - Redes de Computadores Como protocolos da camada de transporte, no modelo TCP/IP, temos os procolos TCP e UDP. E uma das diferenças entre os protocolos TCP e UDP está associada ao estabelecimento da sessão, que é implementada apenas pelo protocolo TCP. Assim, antes do início da transmissão dos dados, o protocolo TCP irá estabelecer uma sessão entre o cliente e o servidor.\nE para o estabelecimento de uma sessão TCP, temos três etapas distintas, envolvendo a troca de mensagens entre os dispositivos. Assim, considerando este processo de inicialização de sessão do protocolo TCP, conforme apresentado no texto da rota, avalie as afirmações a seguir.\nI. O processo de inicia com o envio de uma requisição, pelo cliente, para o estabelecimento de uma nova sessão, com destino ao servidor.\nII. Após o recebimento de uma solicitação de uma nova sessão, o servidor responde ao cliente, também solicitando a abertura de uma sessão, do tipo servidor-cliente.\nIII. Após a troca das duas mensagens iniciais, a sessão já estará estabelecida, não sendo necessária nenhuma mensagem adicional.\nIV. Quando o cliente identificar que não existem mais dados a serem recebidos, ele encerra a sessão, não sendo necessário enviar nenhuma mensagem adicional ao servidor.",
            "options": [
                "A    I e II."
                "B    II e III"
                "C    III e IV."
                "D    I, II e IV."
                "E    I, III e IV."

            ],
            "answer": "A"
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
