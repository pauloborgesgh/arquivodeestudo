def quiz():

    questions = [
        {
            "question": "Questão 1/12 - Redes de Computadores\nUm dos processos de comunicação mais usual nas redes de dados é o modelo chamado de Cliente/Servidor, que é o modelo utilizado quando acessamos um site na Internet, onde o nosso computador, ou um smartphone, \né utilizado como o terminal do cliente e o equipamento onde está armazenado o conteúdo, que está sendo acessado por este cliente, é o chamado Servidor.Neste processo de comunicação os dois terminais farão o papel de transmissor e de receptor, porém com algumas diferenças entre eles.\n Assim, considerando as diferenças entre o cliente e o servidor, em um processo de comunicação através das redes de dados, avalie as afirmações a seguir.\n I. Uma das diferenças entre o transmissor e o receptor é a capacidade de processamento, pois o servidor\n irá responder às solicitações de comunicação de muitos clientes, necessitando de uma maior capacidade de processamento.\nII. Quando o terminal de usuário operar como destinatário das mensagens do servidor, este processo irá exigir que ele tenha a mesma capacidade de processamento do servidor.\nIII. Os aplicativos utilizados pelo cliente e pelo servidor poderão ser diferentes, porém, o processo de codificação das mensagens, utilizados pelos dois, deverá ser o mesmo.\nIV. Tanto o terminal do cliente quanto o servidor poderão estabelecer um processo de comunicação com diversos outros terminais simultaneamente, porém utilizando aplicações diferentes, nos clientes e nos servidores.",
            "options": [
                "A. I e II.",
                "B. II e III.",
                "C. III e IV.",
                "D. I, II e IV.",
                "E. I, III e IV."
            ],
            "answer": "E"
        },
        {
            "question": "Questão 2/12 - Redes de Computadores\nO processo de multiplexação das conversas das camadas superiores é uma função da camada de transporte. Assim, podemos ter várias aplicações sendo executadas no terminal de usuário, simultaneamente, demandando a comunicação através da rede.\nConsiderando este processo de multiplexação, com o encaminhamento dos segmentos de cada uma das aplicações através da camada de transporte, conforme apresentas no texto da rota, avalie as asserções a seguir.\nI. Cada um dos segmentos, gerados pela camada de transporte, associado à cada uma das aplicações, receberá um identificador, que é o número de porta.\nPORQUE\nII. Na camada de rede este número será trocado pelo endereço IP, correspondente ao destinatário dos segmentos, para que os pacotes sejam encaminhados corretamente através da rede, até o destinatário.\n\nA respeito dessas asserções, assinale a opção correta.",
            "options": [
               "\n A	As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
               " \nB	As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira."
                "\nC	A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
               "\nD	A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'"
                "\nE	Tanto a primeira quanto a segunda asserções são proposições falsas."
            ],
            "answer": "C"

        },{"question": "Questão 3/12 - Redes de Computadores\nUma das atribuições da camada de enlace, além do processo de encapsulamento e desencapsulamento dos pacotes recebidos da camada superior e da codificação dos dados para a transmissão através do meio físico, é o controle de acesso ao meio. E este processo dependerá da topologia da camada física, ou seja, de como os dispositivos estão conectados, e do processo de comunicação entre eles.\nAssim, considerando a operação do protocolo de enlace, em uma topologia do tipo multiacesso, em barramento, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nI. O protocolo de controle de enlace deverá verificar, inicialmente, se o meio de transmissão está livre, para então iniciar o processo de transmissão de dados através deste meio.\nPORQUE\nII. É necessário que os terminais tenham a garantia de que o meio físico irá atender a velocidade de transmissão demandada pela aplicação, evitando a perda de pacotes.A respeito dessas asserções, assinale a opção correta.\n",
            "options": [
                '\nA	As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.'
                '\nB	As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.'
                '\nC	A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.'
                '\nD	A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'
                '\nE	Tanto a primeira quanto a segunda asserções são proposições falsas.'
            ],
            "answer": "B"
           },

        {
            "question": "Questão 4/12 - Redes de Computadores\nUma das classificações empregadas para diferenciar as redes de computadores está associada aos recursos disponibilizados na rede, bem como dos tipos de usuários que tem permissão para acessar estes recursos. Assim, a partir destas características são definidos três tipos de redes, que são a Intranet, a Extranet e a Internet.\nA Intranet pode ser considerada basicamente uma rede WAN de acesso restrito, diferentemente da Internet, que é uma rede pública, sem restrição de acesso. Por isso a rede do tipo Intranet também é chamada de rede provada. Considerando as características de uma rede do tipo Intranet apresentadas acima e também no texto da rota, avalie as afirmações a seguir.\nI. A Internet pode ser considerada uma Intranet, quando o terminal do usuário está acessando um servidor WEB da empresa.\nII. Para a implementação da Intranet, as empresas contratam o serviço de uma empresa de telecomunicações, ou, ainda, de um provedor de acesso à Internet.\nIII. Um dos protocolos empregados na implementação de uma Intranet é o protocolo IP/MPLS (IP multi-protocol label switching).\nIV. Um Extranet é formada pela conexão de várias Intranets, semelhante à conexão das redes LAN através de uma rede WAN..\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA	I e II.'
                '\nB	II e III.'
                '\nC	III e IV.'
                '\nD	I, II e IV.'
                '\nE	I, III e IV.'
            ],
            "answer": "B"
        },{
            "question": "Questão 5/12 - Redes de Computadores\nUma classificação usual em relação à infraestrutura de redes, considerando a sua abrangência geográfica, é divisão das redes em redes LAN e redes WAN. Uma rede LAN é uma rede cuja infraestrutura abrange uma área geográfica\n limitada, interconectando os dispositivos finais em uma área limitada, tal como uma residência, escola, edifício de escritórios ou campus, concentrando as conexões com a utilização de switches e Access Points.\n\nOutra característica que diferencia as redes LAN e WAN é a largura de banda, em função da demanda de tráfego das conexões. Assim, considerando esta característica, em relação às redes LAN e WAN, analise as conexões descritas abaixo.\n\nI. As redes LAN operam com uma largura de banda maior do que as redes WAN, onde teremos uma grande quantidade de terminais conectados em um concentrador.\n\nII. As redes WAN operam com menores larguras de banda do que as redes LAN, pois encaminharão apenas o tráfego entre as redes LAN, interconectando estas redes.III. Um dos equipamentos que permite a conexão entre a rede LAN e a rede WAN é o Access Point, pois, necessariamente, ele opera como um roteador.\n\nIV. Para a conexão das redes residenciais à rede WAN é utilizado o Switch, que é disponibilizado pelo provedor de acesso à Internet.\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA	I e II.'
                '\nB	II e III.'
                '\nC	III e IV.'
                '\nD	I, II e IV.'
                '\nE	I, III e IV.'

            ],
            "answer": "E"
        },{
            "question": "Questão 6/12 - Redes de Computadores\nQuando enviamos um e-mail, estamos utilizando um processo de comunicação onde temos os três componentes básicos, que são o transmissor, o receptor e o meio de transmissão. O transmissor será o terminal do usuário que está enviando o e-mail e o receptor será o terminal do usuário que receberá o e-mail. E meio de transmissão será a rede de computadores, que é a Internet. Mas neste processo de comunicação teremos ainda outros componentes, que incluem o processo de codificação e de decodificação.\n\nE como a Internet é uma rede de dados digitais, considere o processo de adequação da mensagem, a este meio de comunicação, conforme visto na rota, e avalie as afirmações a seguir.\n\nI. Os pacotes. que serão transmitidos através da rede de dados. conterão a mensagem de texto, após esta mensagem ser digitalizada e codificada pelo transmissor.\nII. Para e transmissão da mensagem, é necessário que os elementos que formam a rede, ou seja, que implementam o meio de transmissão, conheçam qual foi o processo de digitalização da mensagem.\nIII. O receptor da mensagem deverá estar conectado diretamente ao transmissor, através de um meio dedicado, pois a transmissão de mensagens digitais é realizada apenas entre terminais idênticos.\n\nIV. Para que o destinatário consiga interpretar a mensagem enviada pelo transmissor, é necessário que ocorra o processo de decodificação da mensagem, no terminal do receptor, de acordo com o processo de codificação realizado pelo transmissor.\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA	I e II.'
                '\nB	II e III.'
                '\nC	III e IV.'
                '\nD	I e IV.'

            ],
            "answer": "D"
        },{
            "question": "Questão 7/12 - Redes de Computadores\nBaseado no modelo TCP/IP, o IETF definiu uma série de protocolos, que operam nas camadas de Aplicação, Transporte e Internet, porém, não definiu nenhum protocolo específico para a camada de Acesso à rede. E um destes protocolos é o TCP, que inclusive está citado na designação do próprio modelo.\nConsiderando a operação do protocolo TCP, empregado para o estabelecimento de sessões entre os dispositivos conectados na rede de dados, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\n\nI. O protocolo TCP/IP gerencia as conversas individuais, sendo responsável por garantir a entrega confiável das informações.PORQUE\n\nII. O protocolo TCP/IP opera na camada de Rede, gerenciando o controle de fluxo entre os dispositivos finais.A respeito dessas asserções, assinale a opção correta.\n",
            "options": [
                '\nA	As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.'
                '\nB	As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.'
                '\nC	A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.'
                '\nD	A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'
                '\nE	Tanto a primeira quanto a segunda asserções são proposições falsas.'
            ],
            "answer": "C"
        },{
            "question": "Questão 8/12 - Redes de Computadores\nOs dispositivos de segurança deverão garantir a proteção tanto para as possíveis ameaças que possam existir nas redes LAN, que são as redes locais, quanto em relação às ameaças existentes na rede externa, que é a chamada rede WAN, Além disso, estes dispositivos, ou sistemas de segurança, deverão ser utilizados em todos os tamanhos de redes, nas redes de pequeno ou de grande porte. Ou seja, as técnicas e mecanismos de segurança de rede também deverão ser escaláveis.\nPorém existem diversos tipos de ameaças, sendo que estas poderão ser classificadas em internas e externas, com medidas de segurança adequadas para cada tipo de ameaça. Assim, considerando esta diferença entre os dispositivos e os tamanhos de redes, avalie as asserções a seguir.\n\nI. O Firewall é um dispositivo amplamente utilizado para a implementação da segurança, que pode ser implementado em hardware dedicado, ou seja, em um dispositivo físico específico para esta finalidade, quanto em software, podendo ser instalado em um computador ou servidor.\nPORQUE\nII. Para a implementação de segurança de uma rede de pequeno porte, apenas as soluções em hardware são viáveis, pois não é possível instalar uma aplicação de firewall no computador do usuário.\nA respeito dessas asserções, assinale a opção correta.\n",
            "options": [
                '\nA	As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.'
                '\nB	As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.'
                '\nC	A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.'
                '\nD	A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'
                '\nE	Tanto a primeira quanto a segunda asserções são proposições falsas.'

            ],
            "answer": "C"
        },{
            "question": "Questão 9/12 - Redes de Computadores\nPara a classificação dos diversos protocolos empregados no processo de comunicação nas redes de dados temos o chamado modelo OSI, que define sete camadas envolvidas no processo de comunicação, sendo que cada protocolo será associado à uma destas camadas.\nE as sete camadas descritas no modelo OSI são referenciadas através do seu número ou da sua designação (nome). Porém, podemos encontrar a referência ao modelo OSI com a sigla que inclui o termo em inglês, que é o “layer”. Assim, se tivermos um switch descrito como sendo L3 (Layer 3), podemos considerar que este dispositivo:\n\nI. Poderá ser acessado remotamente, pois este dispositivo também opera na camada de aplicação.\nII. Poderá encaminhar o tráfego baseado na informação dos pacotes IP, pois ele opera na camada de rede.\nIII. Poderá encaminhar o tráfego baseado na informação dos quadros Ethernet, pois ele opera na camada de enlace de dados.\nIV. Deverá ser conectado à um roteador, pois ele não opera na camada física, apenas nas camadas superiores.É correto apenas o que se afirma em\n",
                "options": [
                    '\nA	I e II.'
                    '\nB	II e III.'
                    '\nC	III e IV.'
                    '\nD	I, II e IV.'
                    '\nE	I, III e IV.'


            ],
            "answer": "B"
        },
        {
            "question": "Questão 10/12 - Redes de Computadores\nPara a implementação da confiabilidade de uma rede, ou seja, para garantir que a conectividade entre os clientes e os servidores, no acesso às aplicações, seja garantido, com a qualidade necessária e no momento em que o usuário necessitar acessar estas aplicações, temos alguns requisitos que devem ser atendidos por esta rede. Assim, as quatro características básicas de uma rede, para que ela seja considera uma rede confiável, são a escalabilidade, a tolerância a falhas, a Qualidade de serviço (QoS) e a segurança.\nAssim, para atender ao requisito de escalabilidade, avalie as características descritas a seguir, e identifique quais estão efetivamente relacionadas à escalabilidade\nI. Um equipamento de rede, com apenas duas portas de conexão, tal como um roteador residencial, não atenderá o requisito de escalabilidade, pois não terá redundância de conectividade.\n\nII. O equipamento utilizado para a conexão de uma rede residencial à Internet não é escalável, pois o Firewall instalado no roteador não permite a configuração das regras de bloqueio de tráfego.\n\nIII. Um equipamento utilizado em uma rede residencial, para atender alguns clientes, poderá não ser adequado para ser utilizado em uma rede corporativa, para atender a conexão de muitos usuários, ou seja, não atenderia o requisito de escalabilidade.\n\nIV. O protocolo da rede wireless, conhecido como padrão WiFi, é dito escalável, pois pode ser utilizado tanto em uma rede residencial como em uma rede corporativa.\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA	I e II.'
                '\nB	II e III.'
                '\nC	III e IV.'
                '\nD	I e IV.'
                '\nE	I, III e IV.'
            ],
            "answer": "C"
        },
        {
            "question": "Questão 11/12 - Redes de Computadores\nPara a representação das interconexões dos equipamentos de rede temos a elaboração de um diagrama chamado de topologia da rede, que irá indicar como ocorre a comunicação entre os diversos dispositivos em uma rede. E podemos ter diagramas distintos, para a representação uma determinada rede, que são referentes à topologia física e à topologia lógica da rede. Além disso, podemos ter ainda diferentes topologias para as redes LAN e WAN, em função da forma como os dispositivos intermediários de rede estão interconectados\n\nAssim, considerando as características das topologias típicas utilizadas nas redes WAN, conforme visto na rota, avalie as afirmações a seguir.\nI. Na topologia em estrela temos todo o tráfego da rede passando por um único dispositivo, que está conectado, através de links ponto a ponto, com os demais dispositivos.\n\nII. O custo de uma topologia em estrela torna esta topologia viável apenas para redes com poucos dispositivos, pois o número de dispositivos necessários, para a conexão com o dispositivo central, se torna muito elevado, para redes maiores.\nIII. A topologia em malha completa é a que apresenta a maior simplicidade de implementação e a maior disponibilidade, sendo, desta forma, a topologia mais empregada nas redes.\n\nIV. Podemos ter uma topologia lógica do tipo ponto a ponto, entre dois equipamentos de rede, porém, com vários caminhos e dispositivos intermediários, com uma topologia física em malha completa, por exemplo.\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA	I e II.'
                '\nB	II e III.'
                '\nC	III e IV.'
                '\nD	I e IV.'
                '\nE	I, III e IV.'
            ],
            "answer": "D"
        },
        {
            "question": "Questão  - Redes de Computadores\nOs dispositivos de segurança deverão garantir a proteção tanto para as possíveis ameaças que possam existir nas redes LAN, que são as redes locais, quanto em relação às ameaças existentes na rede externa, que é a chamada rede WAN,\n Além disso, estes dispositivos, ou sistemas de segurança, deverão ser utilizados em todos os tamanhos de redes, \nnas redes de pequeno ou de grande porte. Ou seja, as técnicas e mecanismos de segurança de rede também deverão ser escaláveis.\nPorém existem diversos tipos de ameaças, sendo que estas poderão ser classificadas em internas e externas, com medidas de segurança adequadas para cada tipo de ameaça. Assim, considerando esta diferença entre os dispositivos e os tamanhos de redes, avalie as asserções a seguir.\nI. O Firewall é um dispositivo amplamente utilizado para a implementação da segurança, que pode ser implementado em hardware dedicado, ou seja, em um dispositivo físico específico para esta finalidade, quanto em software, podendo ser instalado em um computador ou servidor.\nPORQUE\n\nII. Para a implementação de segurança de uma rede de pequeno porte, apenas as soluções em hardware são viáveis, pois não é possível instalar uma aplicação de firewall no computador do usuário.\nA respeito dessas asserções, assinale a opção correta.\n",
            "options": [
                '\nA    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.'
                '\nB    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.'
                '\nC    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.'
                '\nD    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'
               ' \nE    Tanto a primeira quanto a segunda asserções são proposições falsas.'

            ],
            "answer": "C"
        },
        {
            "question": "Questão 11/12 - Redes de ComputadoresA rede WAN mais utilizada é a Internet, que é formada pela interconexão das redes WAN de diversos provedores e empresas\n de telecomunicações. Assim, a internet não é de propriedade de nenhum indivíduo ou grupo, utilizando tecnologias e \n padrões consistentes e comumente reconhecidos, para garantir uma comunicação eficaz através desta infraestrutura.\nPara garantir estes padrões, existem diversas instituições que publicam estas normas, sendo que a principal organização é o IEFT (Internet Engineering Task Force) que definiu o protocolo IP, que é a base da Internet. Considerando esta necessidade de padronização, analise as afirmações a seguir, tendo como base o texto da rota\n\nI. O IETF também definiu que, para que os computadores acessem a Internet, é necessário que os switches suportem o protocolo TCP/IP.\n\nII. A conexão dos terminais dos usuários com a Internet será feita por um roteador, conectando uma rede do tipo Intranet à Internet.\nIII. Para garantir que os endereços IP sejam corretamente utilizados pelos provedores de acesso à Internet, os RIRs (Regional Internet Registries) são responsáveis pela atribuição destes endereços.\n\nIV. Um dos registros gerenciados pelo IANA (Internet Assigned Numbers Authority) é o registro de domínios, realizando a manutenção do sistema de DNS raiz da Internet.É correto apenas o que se afirma em\n",
            "options": [
               ' \nA    I e II.'
               ' \nB    II e III.'
                '\nC  III e IV.'
                '\nD    I, II e IV.'

            ],
            "answer": "C"
        },
        {
            "question": " Questão 12/12 - Redes de Computadore\nAlém dos dispositivos finais das redes d\n computadores, temos ainda os dispositivos intermediários e os meios físicos. Os dispositivos intermediários permitirão o acesso dos terminais de usuário à rede, e, também, farão a interconexão com os demais\n dispositivos intermediários, formando a estrutura da rede de dados. E os meios físicos é que estabelecerão a conectividade entre os dispositivos terminais e os\n dispositivos intermediários, bem como a interconexão dos dispositivos\nintermediários.\n\nConsiderando a função dos componentes das redes de computadores apresentadas acima, e as características destes componentes apresentadas no texto da rota, avalie as asserções a seguir.\n\nI. O ponto de acesso para redes sem fio, também chamado de Access Point, é classificado como sendo um dispositivo de rede intermediário.PORQUE\n\nII. O Access Point utiliza como meio físico o espaço livre, para a propagação de ondas eletromagnéticas, também chamada de rádio frequência (RF).A respeito dessas asserções, assinale a opção correta.\n",
            "options": [

               ' \nA    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.'
                '\nB    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.'
                '\nC    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.'
                '\nD    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.'
              '  \nE    Tanto a primeira quanto a segunda asserções são proposições falsas.'

            ],
            "answer": "B"
        },
        {
            "question": "Questão 1/10 - Redes de Computadores\nO protocolo TCP, por operar na camada de transporte, realiza a segmentação dos dados da camada superior, identificando cada um dos segmentos gerados com a inserção de um identificador. Esse identificador é chamado de número de sequência e será inserido no cabeçalho dos segmentos gerados, sendo que o número de sequência inicial, para uma nova transmissão, é gerado de maneira aleatória.\n\nA partir deste número de sequência, o protocolo TCP poderá realizar a verificação dos segmentos recebidos, identificando eventuais perdas de pacotes no processo de transmissão. Avalie as afirmações a seguir:\n\nI. Para a transmissão de dados do servidor para múltiplos clientes, simultaneamente, é necessário sincronizar os números de sequência e de confirmação entre todos os clientes.\nII. Caso ocorram perdas, o processo de reordenamento irá preencher a falta de um pacote com a cópia do pacote seguinte, evitando a quebra de sequência do identificador.\nIII. A cada segmento enviado, o número de sequência é incrementado, somando-se o número de bytes transmitidos neste novo segmento, para que o próximo segmento contenha a sequência correta dos próximos bytes.\nIV. O número de sequência também possibilita implementar a confiabilidade, pois a perda de pacotes poderá ser detectada através deste mecanismo de identificação dos pacotes.\n\nÉ correto apenas o que se afirma em:",
            "options": [
                "\nA. I e II.",
                "\nB. II e III.",
                "\nC. III e IV.",
                "\nD. I, II e IV.",
                "\nE. I, III e IV."
            ],
            "answer": "C"
        },
        {
            "question": "Questão 2/10 - Redes de Computadores\nNo modelo em camadas, uma das camadas é a camada de Rede, que é a camada três do modelo OSI, e que equivale à camada de Internet no modelo TCP/IP. Avalie as afirmações a seguir e identifique quais estão efetivamente relacionadas ao processo de comunicação da camada de rede:\n\nI. Os pacotes da camada de rede são encaminhados através dos dispositivos intermediários, como roteadores, em função da informação contida nestes pacotes, mantendo-os inalterados ao longo do caminho.\nII. Para que ocorra a comunicação na camada de rede, é necessário que o switch local da rede LAN altere o conteúdo do pacote de rede para que ele seja encaminhado corretamente para o roteador local.\nIII. Os dispositivos intermediários de rede, como roteadores, processam os pacotes e alteram suas informações de acordo com o caminho pelo qual os pacotes deverão ser encaminhados.\nIV. O roteador local, na maioria dos casos, fará a alteração das informações da camada de enlace, pois os protocolos utilizados na rede LAN e na rede WAN na camada dois provavelmente serão diferentes.\n\nÉ correto apenas o que se afirma em:\n",
            "options": [
                '\nA. I e II.'
                '\nB. II e III.'
                '\nC. III e IV.'
                '\nD. I e IV.'
                '\nE. I, III e IV.'
            ],
            "answer": "D"

        }, {
            "question": "Questão 3/10 - Redes de Computadores\nAlém do controle de fluxo, uma das funções da camada de transporte é garantir a confiabilidade do processo de comunicação. E para isto, o mecanismo básico consiste no reenvio dos segmentos que foram eventualmente descartados, de forma que a aplicação nem perceberá esta perda de pacotes. Assim, antes de entregar os dados para a camada de aplicação, poderá ser feita a correção deste erro, com a retransmissão dos pacotes perdidos.\nConsiderando o processo de controle de fluxo da camada de transporte, apresentado no texto da rota, avalie as asserções a seguir.\nI. Para a identificação da perda de pacotes, é utilizado um número sequencial, inserido nos pacotes, permitindo que o receptor analise esta informação e identifique eventuais segmentos faltantes.\nII. Caso seja detectada a falta de um pacote, o receptor poderá fazer a solicitação de reenvio para o transmissor, de forma a corrigir esta perda.\nIII. O controle de fluxo é estabelecido a partir do número de segmentos recebidos, que é aumentado cada vez que ocorre uma perda de pacotes.\nIV. A confiabilidade do processo é garantida pois, caso algum pacote seja perdido no processo de transmissão, ele poderá ser retransmitido.\nÉ correto apenas o que se afirma em\n",
            "options": [
                '\nA    I e II'
                '\nB    II e III.'
                '\nC    III e IV.'
                '\nD    I, II e IV.'
                '\nE    I, III e IV'

            ],
            "answer": "D"
            },

        {
            "question": " Questão 4/10 - Redes de Computadores\nUma das tarefas realizadas pelo protocolo TCP é o controle de fluxo, que irá garantir que os terminais que estão executando o protocolo TCP possam receber e processar os dados de forma confiável.Assim, o TCP realiza o controle de fluxo, ajustando a taxa de envio de dados entre o remetente e o destinatário, durante o processo de comunicação em uma determinada sessão. Desta forma, considerando a operação do protocolo TCP, em relação ao processo de controle de fluxo, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nI. O protocolo TCP insere, em seu cabeçalho, um campo identificado como tamanho de janela, que representa o número de bytes que o dispositivo de destino de uma sessão TCP pode aceitar e processar, antes de enviar a solicitação para o envio de mais segmentos.\nPORQUE\nII. Com esta informação, os dispositivos de rede, tal como os roteadores, irão definir a prioridade destes pacotes, priorizando o fluxo deste tráfego.\nA respeito dessas asserções, assinale a opção correta.:",
            "options": [
                " \nA    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
                "\n B    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira."
                "\nC    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
                "\nD    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
                "\nE    Tanto a primeira quanto a segunda asserções são proposições falsas."
            ],
            "answer": "C"
        }, {
            "question": "Questão 5/10 - Redes de Computadores \nOs protocolos da camada de transporte inserem as informações necessárias, para a implementação das suas funções, em campos específicos, que são acrescidos ao cabeçalho de cada segmento transmitido.\nAssim, considerando o cabeçalho gerado pelo protocolo TCP, que possui um tamanho total de 20 bytes, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nI. Para cada segmento gerado será necessária a inserção de um cabeçalho TCP, que conterá os campos de Porta de Origem e Porta de Destino, entre outros.\nII\n. Dois campos que são inseridos no cabeçalho TCP são o Número de Sequência e o Número de Confirmação, que identificam a ordem dos segmentos.\nIII. Um dos campos inseridos no cabeçalho TCP é o Endereço IP do destinatário, para que este segmento seja encaminhado pela rede corretamente.\nIV. Caso seja necessário dividir o segmento em segmentos menores, para adequar aos protocolos da camada inferior, será inserido no cabeçalho TCP o campo que identifica o Número do Fragmento.\nÉ correto apenas o que se afirma em\n",
            "options": [
                "\nA  I e II. "
                "\nB  II e III."
                "\nC  III e IV."
                "\nD  I, II e IV."
                "\nE  I, III e IV."

            ],
            "answer": "A"
        }, {
            "question": "Questão 6/10 - Redes de ComputadoresUma das camadas, descritas no modelo de rede, e que fica localizada acima da camada de rede, é a camada de transporte. E esta camada possui a mesma identificação tanto no modelo OSI quanto no modelo TCP/IP, possuindo as mesmas atribuições nos dois modelos.\nAssim, considerando as características da camada de transporte, conforme visto na rota, avalie as afirmações a seguir.\nI. Uma das funções da camada de transporte é estabelecer as sessões de comunicação, de maneira temporária, entre as aplicações, permitindo a transferência de dados entre estas sessões.\nII. Como a camada de transporte não tem como função realizar o controle de fluxo, esta tarefa deverá ser executada pelas camadas superiores, tal como a camada de aplicação.\nIII. Para que sejam identificadas as conversas de camadas superiores, a camada de rede deverá fornecer, para a camada de transporte, o endereço IP de cada conexão.\nIV. Uma das tarefas das camada de transporte é realizar a segmentação dos dados recebidos da camada superior, para adequá-los à estrutura de pacote da camada de rede.\nÉ correto apenas o que se afirma em",
            "options": [
                "\n A    I e II."
                "\nB    II e III."
                "\nC    III e IV."
                "\nD    I e IV."
                " \nE    I, III e IV."
            ],
            "answer": "D"
        }, {
            "question": "Questão 7/10 - Redes de Computadores Uma das funções da camada de transporte é realizar a interface entre as aplicações e a camada de rede, e assim adequar os dados a serem transmitidos, de acordo com a demanda das aplicações, para que possam ser encapsulados corretamente pelo protocolo de camada de rede. E uma das características associadas a este processo de encapsulamento é o tamanho do conteúdo da carga nestes pacotes, o que dependerá do protocolo que está sendo utilizado na camada de rede.\nConsiderando este processo de encapsulamento, e as características de operação de um protocolo da camada de transporte, apresentadas no texto da rota, avalie as asserções a seguir.\nI. O modelo em camadas define que os protocolos, que operam em cada uma das camadas, deverão seguir um padrão único em relação ao tamanho do conteúdo de carga que eles suportam.\nPORQUE\n\nII. A quantidade de dados a serem transmitidos pelo protocolo de rede pode ser maior do que o tamanho dos pacotes da camada de rede, sendo necessário dividir estes dados em segmentos.\nA respeito dessas asserções, assinale a opção correta.",
            "options": [
                "\nA    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
                "\nB    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira."
                "\nC    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
                "\n D    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
            ],
            "answer": "B"
        }, {
            "question": "Questão 8/10 - Redes de Computadores\nUm dos protocolos mais utilizados na camada de transporte, nas redes de dados, é o protocolo TCP, que deverá então executar a multiplexação das aplicações das camadas superiores, garantir a confiabilidade do processo de comunicação e realizar o controle de fluxo.\nAssim, considerando a operação do protocolo TCP, em relação ao processo de multiplexação, e com base nas informações apresentadas no texto da rota, avalie as asserções a seguir:\nIII. O protocolo TCP insere, em seu cabeçalho, os campos que contém os identificadores de porta de origem e porta de destino, que possuem um comprimento de 16 bits cada um deles.\nPORQUE\n\nIV. Com esta informação o destinatário dos segmento TCP poderá identificar para qual das aplicações ele deverá encaminhar o conteúdo dos dados, que foram recebidos dentro do segmento.\nA respeito dessas asserções, assinale a opção correta.\n",
            "options": [
                "\nA    As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira."
                "\nB    As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira"
                "\nC    A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa."
                "\nD    A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira."
                "\nE    Tanto a primeira quanto a segunda asserções são proposições falsas"

            ],
            "answer": "A"
        }, {
            "question": "Questão 9/10 - Redes de Computadores Como protocolos da camada de transporte, no modelo TCP/IP, temos os procolos TCP e UDP. E uma das diferenças entre os protocolos TCP e UDP está associada ao estabelecimento da sessão, que é implementada apenas pelo protocolo TCP. Assim, antes do início da transmissão dos dados, o protocolo TCP irá estabelecer uma sessão entre o cliente e o servidor.\nE para o estabelecimento de uma sessão TCP, temos três etapas distintas, envolvendo a troca de mensagens entre os dispositivos. Assim, considerando este processo de inicialização de sessão do protocolo TCP, conforme apresentado no texto da rota, avalie as afirmações a seguir.\nI. O processo de inicia com o envio de uma requisição, pelo cliente, para o estabelecimento de uma nova sessão, com destino ao servidor.\nII. Após o recebimento de uma solicitação de uma nova sessão, o servidor responde ao cliente, também solicitando a abertura de uma sessão, do tipo servidor-cliente.\nIII. Após a troca das duas mensagens iniciais, a sessão já estará estabelecida, não sendo necessária nenhuma mensagem adicional.\nIV. Quando o cliente identificar que não existem mais dados a serem recebidos, ele encerra a sessão, não sendo necessário enviar nenhuma mensagem adicional ao servidor.\n",
            "options": [
                "\nA    I e II."
                "\nB    II e III."
                "\nC    III e IV."
                "\nD    I, II e IV."
                "\nE    I, III e IV."

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
            print("Resposta correta!\n")
            score += 10
        else:
            print(f"Resposta incorreta. A resposta correta é: {q['answer']}\n")

    print(f"Sua pontuação final é: {score}/100")

quiz()
