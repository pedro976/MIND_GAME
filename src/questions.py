# ==============================================================================
# ARQUIVO: src/questions.py
# ... (header mantido)
# ==============================================================================

PERGUNTAS = [
    {
        'alternativas': [
            'Forneço a senha, pois é para minha segurança.',
            'Pergunto ao bot se ele é realmente oficial.',
            'Ignoro e denuncio a mensagem como spam/phishing.'
        ],
        'categoria': 'Privacidade',
        'correta': 2,
        'dificuldade': 'Fácil',
        'enunciado': "Você recebeu uma mensagem de um 'bot' pedindo sua senha para 'atualizar sua segurança'. O que você faz?",
        'explicacao': 'IAs e sistemas oficiais nunca pedem sua senha por mensagem. Isso é um golpe comum chamado phishing.',
        'id': 1
    },
    {
        'alternativas': [
            'Acredito totalmente, pois IAs têm acesso a toda a internet.',
            'Verifico a informação em fontes confiáveis e livros de história.',
            'Compartilho o texto imediatamente nas redes sociais.'
        ],
        'categoria': 'Confiabilidade',
        'correta': 1,
        'dificuldade': 'Fácil',
        'enunciado': 'Uma IA gerou um resumo sobre um fato histórico que você nunca ouviu falar. Como agir?',
        'explicacao': "IAs podem 'alucinar', ou seja, inventar fatos que parecem reais. Sempre verifique informações importantes.",
        'id': 2
    },
    {
        'alternativas': [
            'Dizer que você mesmo desenhou à mão.',
            'Não dizer nada, pois ninguém vai perceber.',
            'Indicar que a imagem foi gerada por uma IA.'
        ],
        'categoria': 'Ética',
        'correta': 2,
        'dificuldade': 'Média',
        'enunciado': 'Ao usar uma IA para criar uma imagem para um trabalho escolar, você deve:',
        'explicacao': 'A transparência é fundamental no uso da IA. Dar crédito à ferramenta é uma prática ética recomendada.',
        'id': 3
    },
    {
        'alternativas': [
            'Um tipo de computador muito rápido.',
            'Vídeos ou áudios manipulados por IA para parecerem reais.',
            'Um jogo de realidade virtual avançada.'
        ],
        'categoria': 'Segurança',
        'correta': 1,
        'dificuldade': 'Fácil',
        'enunciado': "O que é um 'Deepfake'?",
        'explicacao': 'Deepfakes usam IA para trocar rostos ou vozes em vídeos, podendo ser usados para desinformação.',
        'id': 4
    },
    {
        'alternativas': [
            'Pedir para ela fazer todo o trabalho e copiar o resultado.',
            'Ignorar a IA, pois ela não ajuda no aprendizado.',
            'Usar para explicar conceitos difíceis e tirar dúvidas.'
        ],
        'categoria': 'Educação',
        'correta': 2,
        'dificuldade': 'Média',
        'enunciado': 'Qual a melhor forma de usar a IA nos estudos?',
        'explicacao': 'A IA é uma ótima tutora para explicar temas complexos, mas copiar o resultado impede seu aprendizado.',
        'id': 5
    },
    {
        'alternativas': [
            'Eles priorizam conteúdos que aumentam seu tempo na plataforma.',
            'Eles mostram apenas o que é verdade absoluta.',
            'Eles mostram postagens em ordem puramente cronológica.'
        ],
        'categoria': 'Redes Sociais',
        'correta': 0,
        'dificuldade': 'Média',
        'enunciado': 'Como os algoritmos de IA influenciam o que você vê nas redes sociais?',
        'explicacao': "Algoritmos são treinados para manter sua atenção, o que pode criar 'bolhas' de informação.",
        'id': 6
    },
    {
        'alternativas': [
            'Os dados podem ser usados para treinar futuras versões da IA.',
            'Os dados são apagados imediatamente após o uso.',
            'Os dados são criptografados e ninguém nunca terá acesso.'
        ],
        'categoria': 'Privacidade',
        'correta': 0,
        'dificuldade': 'Difícil',
        'enunciado': 'Ao inserir dados pessoais em um chat de IA gratuito, o que pode acontecer?',
        'explicacao': 'Muitas empresas usam as conversas para treinar seus modelos. Evite compartilhar informações sensíveis.',
        'id': 7
    },
    {
        'alternativas': [
            'Que ela é muito rápida no processamento.',
            'Que ela reflete preconceitos presentes nos dados de treinamento.',
            'Que ela nunca comete erros lógicos.'
        ],
        'categoria': 'Impacto Social',
        'correta': 1,
        'dificuldade': 'Média',
        'enunciado': "O que significa dizer que uma IA possui 'viés' (bias)?",
        'explicacao': 'Se os dados usados para treinar a IA tiverem preconceitos, a IA pode reproduzir esses mesmos comportamentos.',
        'id': 8
    },
    {
        'alternativas': [
            'Desconfio, pois promessas exageradas são sinais de golpe.',
            'Clico rápido para não perder o prêmio.',
            'Respondo agradecendo e mando meus dados bancários.'
        ],
        'categoria': 'Segurança',
        'correta': 0,
        'dificuldade': 'Fácil',
        'enunciado': 'Um e-mail diz que você ganhou um prêmio em barras de ouro e pede para clicar num link gerado por IA. O que fazer?',
        'explicacao': "Golpistas usam ferramentas de IA para criar e-mails persuasivos. Desconfie sempre de ofertas 'boas demais'.",
        'id': 9
    },
    {
        'alternativas': [
            'Nenhum, a IA se desenvolve sozinha.',
            'Treinar, curar dados e definir limites éticos para a tecnologia.',
            'Apenas ligar e desligar os servidores.'
        ],
        'categoria': 'Trabalho',
        'correta': 1,
        'dificuldade': 'Difícil',
        'enunciado': 'Qual o papel dos humanos no desenvolvimento da Inteligência Artificial?',
        'explicacao': 'A supervisão humana é essencial para garantir que a IA seja segura, ética e útil para a sociedade.',
        'id': 10
    },
    {
        'id': 11,
        'enunciado': 'Uma ferramenta de IA traduziu um texto, mas você percebeu que algumas frases perderam o sentido original. O que fazer?',
        'alternativas': [
            'Utilizar a tradução sem conferir, pois a IA sempre entende o contexto.',
            'Revisar a tradução e comparar com o texto original.',
            'Apagar o texto, pois nenhuma IA consegue traduzir corretamente.'
        ],
        'correta': 1,
        'categoria': 'Tecnologia',
        'dificuldade': 'Fácil',
        'explicacao': 'A IA pode cometer erros de interpretação e perder o contexto de algumas expressões. Por isso, revisar traduções é importante.'
    },
    {
        'id': 12,
        'enunciado': 'Uma pessoa utiliza uma IA para obter um diagnóstico médico. Qual deve ser sua atitude?',
        'alternativas': [
            'Seguir o diagnóstico sem consultar ninguém.',
            'Compartilhar o diagnóstico nas redes sociais.',
            'Utilizar a resposta apenas como informação inicial e procurar um profissional de saúde.'
        ],
        'correta': 2,
        'categoria': 'Saúde',
        'dificuldade': 'Média',
        'explicacao': 'A IA pode ajudar a encontrar informações sobre saúde, mas não substitui a avaliação e o diagnóstico de um profissional.'
    },
    {
        'id': 13,
        'enunciado': 'Como a Inteligência Artificial pode ajudar pessoas com deficiência auditiva?',
        'alternativas': [
            'Gerando legendas automáticas para áudios e vídeos.',
            'Aumentando o volume de todos os sons.',
            'Impedindo o acesso a conteúdos digitais.'
        ],
        'correta': 0,
        'categoria': 'Acessibilidade',
        'dificuldade': 'Fácil',
        'explicacao': 'Ferramentas de IA podem transformar falas em legendas, facilitando o acesso à informação para pessoas com deficiência auditiva.'
    },
    {
        'id': 14,
        'enunciado': 'Qual é um dos principais desafios no desenvolvimento de carros autônomos?',
        'alternativas': [
            'Fazer o veículo consumir mais combustível.',
            'Garantir que o sistema reconheça obstáculos e tome decisões seguras no trânsito.',
            'Impedir que o veículo utilize sensores.'
        ],
        'correta': 1,
        'categoria': 'Tecnologia',
        'dificuldade': 'Média',
        'explicacao': 'Carros autônomos precisam interpretar o ambiente e reagir corretamente a situações imprevisíveis para evitar acidentes.'
    },
    {
        'id': 15,
        'enunciado': 'Por que não é recomendado confiar totalmente em ferramentas que prometem identificar se um texto foi escrito por IA?',
        'alternativas': [
            'Porque essas ferramentas nunca conseguem analisar textos.',
            'Porque todos os textos escritos por humanos são identificados como IA.',
            'Porque esses detectores podem cometer erros e apresentar resultados incorretos.'
        ],
        'correta': 2,
        'categoria': 'Confiabilidade',
        'dificuldade': 'Difícil',
        'explicacao': 'Detectores de textos gerados por IA não são totalmente precisos e podem classificar incorretamente textos escritos por humanos ou por máquinas.'
    },
    {
        'id': 16,
        'enunciado': 'Uma empresa utiliza IA para selecionar candidatos a uma vaga de emprego. Qual cuidado é necessário?',
        'alternativas': [
            'Manter a supervisão humana e avaliar possíveis erros ou discriminações do sistema.',
            'Deixar a IA tomar todas as decisões sem revisão.',
            'Selecionar apenas candidatos que utilizam ferramentas de IA.'
        ],
        'correta': 0,
        'categoria': 'Ética',
        'dificuldade': 'Média',
        'explicacao': 'Decisões importantes sobre pessoas precisam de supervisão humana para evitar injustiças e possíveis discriminações automatizadas.'
    },
    {
        'id': 17,
        'enunciado': 'O que é um prompt ao utilizar uma ferramenta de Inteligência Artificial?',
        'alternativas': [
            'Um erro que acontece durante o processamento.',
            'Uma instrução ou pergunta enviada à IA para orientar sua resposta.',
            'Um programa utilizado exclusivamente para armazenar arquivos.'
        ],
        'correta': 1,
        'categoria': 'Conceitos',
        'dificuldade': 'Fácil',
        'explicacao': 'Prompt é o comando, pergunta ou instrução fornecida pelo usuário para que a IA realize uma tarefa.'
    },
    {
        'id': 18,
        'enunciado': 'Qual é uma possível consequência ambiental do crescimento do uso da Inteligência Artificial?',
        'alternativas': [
            'A eliminação completa do consumo de energia.',
            'A redução obrigatória de todos os resíduos eletrônicos.',
            'O aumento do consumo de energia em centros de processamento de dados.'
        ],
        'correta': 2,
        'categoria': 'Meio Ambiente',
        'dificuldade': 'Difícil',
        'explicacao': 'O treinamento e a utilização de grandes sistemas de IA exigem processamento computacional, que pode aumentar o consumo de energia.'
    },
    {
        'id': 19,
        'enunciado': 'O que acontece quando uma IA recebe instruções muito vagas ou pouco detalhadas?',
        'alternativas': [
            'Ela pode gerar respostas genéricas ou diferentes do que o usuário esperava.',
            'Ela sempre identifica exatamente o que o usuário deseja.',
            'Ela deixa automaticamente de funcionar.'
        ],
        'correta': 0,
        'categoria': 'Conceitos',
        'dificuldade': 'Fácil',
        'explicacao': 'Instruções claras e específicas ajudam a IA a compreender melhor a tarefa e produzir respostas mais adequadas.'
    },
    {
        'id': 20,
        'enunciado': 'Por que é importante atualizar regularmente os sistemas que utilizam Inteligência Artificial?',
        'alternativas': [
            'Para impedir que o sistema aprenda novas informações.',
            'Para corrigir falhas, melhorar a segurança e aprimorar seu funcionamento.',
            'Para eliminar a necessidade de supervisão humana.'
        ],
        'correta': 1,
        'categoria': 'Segurança',
        'dificuldade': 'Média',
        'explicacao': 'Atualizações podem corrigir vulnerabilidades, resolver problemas e melhorar o desempenho dos sistemas de IA.'
    },
    {
        'id': 21,
        'enunciado': 'Como a Inteligência Artificial pode ajudar os estudantes na educação?',
        'alternativas': [
            'Substituindo completamente os professores.',
            'Personalizando os estudos de acordo com as dificuldades de cada aluno.',
            'Eliminando a necessidade de estudar.'
        ],
        'correta': 1,
        'categoria': 'Educação',
        'dificuldade': 'Fácil',
        'explicacao': 'A IA pode adaptar exercícios, resumos e explicações ao ritmo e às dificuldades de cada estudante, apoiando o aprendizado.'
    },
    {
        'id': 22,
        'enunciado': 'Qual é uma forma responsável de utilizar IA para fazer trabalhos escolares?',
        'alternativas': [
            'Copiar todas as respostas sem ler.',
            'Usar a IA para aprender e revisar o conteúdo.',
            'Entregar qualquer resposta gerada pela IA sem conferir.'
        ],
        'correta': 1,
        'categoria': 'Educação',
        'dificuldade': 'Fácil',
        'explicacao': 'Usar a IA como apoio para entender e revisar o tema desenvolve o aprendizado, enquanto apenas copiar prejudica a formação.'
    },
    {
        'id': 23,
        'enunciado': 'Por que devemos conferir as informações fornecidas por uma IA?',
        'alternativas': [
            'Porque a IA nunca consegue responder perguntas.',
            'Porque todas as respostas são falsas.',
            'Porque a IA pode apresentar informações incorretas.'
        ],
        'correta': 2,
        'categoria': 'Confiabilidade',
        'dificuldade': 'Fácil',
        'explicacao': 'Sistemas de IA podem cometer erros ou gerar informações imprecisas, por isso é essencial verificar os dados.'
    },
    {
        'id': 24,
        'enunciado': 'Como a IA pode ajudar os médicos na área da saúde?',
        'alternativas': [
            'Auxiliando na análise de exames e na identificação de possíveis doenças.',
            'Substituindo todos os hospitais.',
            'Realizando qualquer tratamento sem supervisão.'
        ],
        'correta': 0,
        'categoria': 'Saúde',
        'dificuldade': 'Fácil',
        'explicacao': 'A IA apoia profissionais de saúde analisando exames com rapidez para ajudar a detectar sinais de doenças mais cedo.'
    },
    {
        'id': 25,
        'enunciado': 'Qual é o principal risco de utilizar uma IA para obter um diagnóstico médico sem consultar um profissional?',
        'alternativas': [
            'A IA pode deixar o computador mais lento.',
            'A IA pode fornecer informações incorretas e prejudicar o tratamento.',
            'O paciente aprenderá muitas informações.'
        ],
        'correta': 1,
        'categoria': 'Saúde',
        'dificuldade': 'Média',
        'explicacao': 'Um diagnóstico errado ou incompleto pode atrasar o tratamento adequado ou levar a condutas prejudiciais à saúde.'
    },
    {
        'id': 26,
        'enunciado': 'Por que os dados dos pacientes precisam ser protegidos ao utilizar sistemas de IA?',
        'alternativas': [
            'Para evitar que informações pessoais e médicas sejam expostas.',
            'Para impedir que os médicos utilizem computadores.',
            'Para diminuir a quantidade de hospitais.'
        ],
        'correta': 0,
        'categoria': 'Privacidade',
        'dificuldade': 'Média',
        'explicacao': 'Dados de saúde são informações sensíveis; protegê-los garante a privacidade do paciente e evita vazamentos ou uso indevido.'
    },
    {
        'id': 27,
        'enunciado': 'Um estudante utiliza uma IA para responder uma atividade, mas percebe que uma resposta está errada. O que ele deve fazer?',
        'alternativas': [
            'Manter a resposta porque a IA sabe tudo.',
            'Apagar toda a atividade.',
            'Pesquisar em fontes confiáveis e corrigir a resposta.'
        ],
        'correta': 2,
        'categoria': 'Confiabilidade',
        'dificuldade': 'Fácil',
        'explicacao': 'Consultar livros, materiais didáticos ou fontes confiáveis permite validar o conteúdo e corrigir falhas cometidas pela IA.'
    },
    {
        'id': 28,
        'enunciado': 'Qual alternativa apresenta um benefício da IA na saúde?',
        'alternativas': [
            'Substituir a necessidade de médicos.',
            'Ajudar a analisar grandes quantidades de informações médicas.',
            'Garantir a cura de todas as doenças.'
        ],
        'correta': 1,
        'categoria': 'Saúde',
        'dificuldade': 'Média',
        'explicacao': 'A IA consegue processar grandes volumes de dados clínicos e estudos rapidamente, apoiando pesquisas e decisões médicas.'
    },
    {
        'id': 29,
        'enunciado': 'Uma IA utilizada em uma escola apresenta resultados diferentes para alunos com o mesmo desempenho. O que pode estar acontecendo?',
        'alternativas': [
            'A IA pode apresentar vieses nos dados utilizados.',
            'A IA está sempre correta.',
            'Os alunos precisam parar de estudar.'
        ],
        'correta': 0,
        'categoria': 'Ética',
        'dificuldade': 'Difícil',
        'explicacao': 'Se os dados de treinamento contêm desequilíbrios ou preconceitos, a IA pode reproduzir esses vieses e gerar avaliações injustas.'
    },
    {
        'id': 30,
        'enunciado': 'Qual é a melhor maneira de utilizar a Inteligência Artificial na educação e na saúde?',
        'alternativas': [
            'Confiar em todas as respostas sem questionar.',
            'Deixar todas as decisões nas mãos da tecnologia.',
            'Utilizar a IA como ferramenta de apoio, com supervisão e responsabilidade humana.'
        ],
        'correta': 2,
        'categoria': 'Ética',
        'dificuldade': 'Média',
        'explicacao': 'A IA traz melhores resultados quando auxilia profissionais e estudantes sob supervisão humana, garantindo decisões éticas e seguras.'
    }
]