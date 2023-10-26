# **Integração Prática: Consumindo APIs com Power BI**

O mundo dos dados está repleto de fontes ricas e diversificadas que podem fornecer insights valiosos para os negócios. Em um cenário de globalização, onde as transações financeiras cruzam fronteiras e moedas, estar atualizado sobre as variações cambiais é mais do que uma necessidade – é uma estratégia.

Imagine por um momento que você é o responsável por uma grande empresa de importações. Diariamente, você lida com múltiplas transações em diversas moedas, e cada pequena flutuação no valor de cotação pode representar impactos significativos nos seus lucros ou despesas. Ter em mãos um dashboard atualizado com as cotações em tempo real não é apenas conveniente, mas crucial para decisões informadas e ágeis.

*Então, como fazer isso?*

A solução está em combinar a eficiência do Power BI com a precisão dos dados fornecidos diretamente pela fonte mais confiável em termos de cotação de moedas no Brasil: a API do Banco Central.

Neste tutorial, você será guiado passo a passo sobre como realizar essa integração. Usaremos como exemplo a seguinte consulta à API do Banco Central:

```
https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda='USD',dataInicialCotacao='10-24-2023',dataFinalCotacao='10-24-2023')?$select=cotacaoCompra
```
Acompanhe e descubra como importar dados de APIs para utilizar em suas análises!

---

## Entendendo os Dados Básicos da Empresa

Antes de nos aprofundarmos na integração com a API do Banco Central, é crucial entender os dados com os quais estaremos trabalhando. Uma empresa de importações possui uma infinidade de informações circulando diariamente. Desde a movimentação de produtos até os custos associados a cada operação, é essencial manter um registro detalhado para uma gestão eficaz.

### Estrutura Básica dos Dados

Para nossa análise, consideremos uma tabela que contém os seguintes campos:

1. **Cód de Movimentação**: Um identificador único para cada transação.
2. **Data**: A data em que a movimentação ocorreu.
3. **Tipo**: Define se a movimentação foi uma compra ou venda.
4. **Classificação**: Categoria do produto importado (ex: eletrônicos, vestuário, alimentos).
5. **Documento**: Número do documento associado à movimentação, como uma nota fiscal.
6. **Centro de Custos**: Área da empresa responsável pela transação (ex: setor de compras, vendas).
7. **Local**: País ou região de origem ou destino da mercadoria.
8. **Valor**: Montante financeiro da transação.
9. **Moeda**: Moeda em que a transação foi realizada (ex: USD, EUR).

Estes são os campos básicos, mas é possível expandir conforme a necessidade. Por exemplo, podemos adicionar "Descrição do Produto", "Fornecedor", etc.

### Simulando Dados com Python**

No mundo da análise de dados, nem sempre temos acesso direto a dados reais para trabalhar, especialmente em estágios iniciais de um projeto ou quando estamos criando protótipos. É aqui que a simulação de dados entra em cena. Simular dados nos permite criar cenários hipotéticos, testar funcionalidades e verificar a viabilidade de integrações, como a que faremos com a API do Banco Central.

O Python, sendo uma das linguagens de programação mais versáteis e amplamente utilizadas no mundo da ciência e análise de dados, oferece uma vasta gama de ferramentas e bibliotecas para manipulação, análise e visualização de dados. Além de sua flexibilidade, também se destaca pela facilidade com que podemos criar conjuntos de dados aleatórios, mas realistas, como faremos a seguir.

```python
import pandas as pd
import random
from datetime import datetime, timedelta

# Gerando dados aleatórios
num_rows = 1000

cod_movimentacao = range(1, num_rows+1)
data = [(datetime.today() - timedelta(days=random.randint(0,365))).date() for _ in range(num_rows)]
tipo = random.choices(["Compra", "Venda"], k=num_rows)
classificacao = random.choices(["Eletrônicos", "Vestuário", "Alimentos", "Móveis"], k=num_rows)
documento = [f"NF-{random.randint(1000,9999)}" for _ in range(num_rows)]
centro_custos = random.choices(["Setor de Compras", "Setor de Vendas", "Logística"], k=num_rows)
local = random.choices(["Brasil", "EUA", "China", "Alemanha", "Japão"], k=num_rows)
valor = [random.uniform(50, 5000) for _ in range(num_rows)]
moeda = random.choices(["USD", "EUR", "JPY", "CNY"], k=num_rows)

# Criando DataFrame
df = pd.DataFrame({
    "Cód de Movimentação": cod_movimentacao,
    "Data": data,
    "Tipo": tipo,
    "Classificação": classificacao,
    "Documento": documento,
    "Centro de Custos": centro_custos,
    "Local": local,
    "Valor": valor,
    "Moeda": moeda
})

# Salvando
df.to_excel("dados_importacao.xlsx", index=False)
```

Este código cria uma planilha "dados_importacao.xlsx" contendo mil linhas de dados fictícios, que servirão como base para nossa análise no Power BI.

---

## Do Excel à Atualização em Tempo Real

Com uma compreensão clara dos dados da empresa, podemos agora prosseguir para o próximo capítulo, onde começaremos a integração com a API do Banco Central para atualização das cotações em tempo real.

### Transformando e Integrando Dados no Power BI

A primeira etapa deste processo começa com a importação de nossos dados no Power BI. A ferramenta da Microsoft é reconhecida por sua capacidade de se conectar a diversas fontes de dados, e com o Excel, essa integração é quase instantânea.

*Para começar:*

1. **Abra o Power BI Desktop**.
2. No menu inicial, clique em "Obter dados".
3. Escolha a opção "Excel" e localize o arquivo "dados_importacao.xlsx" que geramos anteriormente.
4. Selecione a planilha ou as tabelas que deseja importar e clique em "Transformar Dados".

Ao clicar em "Transformar Dados", você será direcionado ao Editor de Consultas do Power BI, um espaço poderoso onde a mágica da transformação e modelagem de dados acontece.

---

## Enriquecendo os Dados com a API do Banco Central

Com os dados da empresa devidamente carregados no Editor de Consultas do Power BI, o nosso foco agora se volta para uma questão central: como obter, de forma dinâmica e precisa, as cotações atuais das moedas para cada transação registrada? A resposta está na integração com a API do Banco Central.

### **Entendendo a API**

A API do Banco Central é uma poderosa ferramenta que nos permite acessar informações atualizadas sobre a cotação das moedas. O link que nos foi fornecido anteriormente:

[https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda='USD',dataInicialCotacao='10-05-2023',dataFinalCotacao='10-05-2023')?%24select=cotacaoCompra](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda='USD',dataInicialCotacao='10-05-2023',dataFinalCotacao='10-05-2023')?%24select=cotacaoCompra)

contém alguns parâmetros essenciais que devem ser entendidos:

- **codigoMoeda**: Refere-se ao código da moeda que queremos consultar. No caso acima, 'USD' refere-se ao dólar americano.
- **dataInicialCotacao e dataFinalCotacao**: Delimitam o período de busca das cotações. No exemplo, estamos buscando a cotação do dólar para o dia 10-05-2023.

Para uma integração eficaz com o Power BI, precisamos que esses parâmetros sejam dinâmicos, ou seja, que se adaptem automaticamente às diferentes moedas e datas em nossos registros.

### Configurando a Coluna de Data para a API

Para uma integração eficaz com a API do Banco Central, é fundamental que as datas em nosso dataset estejam alinhadas ao formato que a API reconhece, que é (dd-MM-yyyy). Dada a variedade de formatos de data que podemos encontrar em datasets, muitas vezes se faz necessário ajustar ou criar uma nova coluna que atenda a esse padrão.

*Siga os passos abaixo para criar essa coluna no formato adequado:*

1. No Editor de Consultas do Power BI, selecione a coluna que contém as datas.
2. Acesse a aba "Adicionar Coluna" na parte superior.
3. Dentro das opções disponíveis, opte por "Coluna de Exemplos". Este recurso permite que você forneça um ou dois exemplos e o Power BI tentará replicar esse padrão para as demais entradas da coluna.
4. Forneça um exemplo no formato desejado (dd-MM-yyyy) e observe o Power BI aplicar esse formato a todas as demais datas.
5. Após a criação, renomeie esta nova coluna para algo descritivo como "DataFormatada_API" para fácil identificação posterior.

Com a nova coluna de datas formatada conforme a API exige, estamos um passo mais perto de realizar uma integração bem-sucedida e dinâmica com as cotações de moeda atualizadas.

### **Integrando API em uma nova coluna**

Com nossa estrutura de dados preparada e devidamente formatada, o próximo passo lógico é integrar a API do Banco Central para capturar as cotações atualizadas em tempo real. Usaremos o Editor Avançado, ele torna essa tarefa acessível e dinâmica.

#### **Estrutura Básica para Acesso a APIs**:

A estrutura padrão para criação de uma nova coluna e acesso a APIs no Power BI é ilustrada abaixo:

```m
let
...
PreviousStep = ... ,    
Step = Table.AddColumn(PreviousStep, "NewColumnName", each Json.Document(Web.Contents("https://api.example.com/data?param=" & [id] & "&key=[apiKey]"))),
in Step
```

*Neste modelo:*

- **let e in**: Delimitam o início e o fim de uma série de etapas de transformação.
- **PreviousStep**: Representa a etapa anterior na sequência de transformações.
- **Table.AddColumn**: Função responsável por criar uma nova coluna no conjunto de dados.
- **Json.Document & Web.Contents**: Estas funções trabalham em conjunto para fazer um chamado à API e interpretar a resposta, que geralmente está em formato JSON.

#### Adaptando para Nossas Necessidades:

Para nosso contexto específico, a URL da API do Banco Central é ligeiramente diferente, e os parâmetros são dinamicamente inseridos a partir das colunas de nossa tabela:

```m
https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda='" & [Moeda] & "',dataInicialCotacao='" & [DataFormatada_API] & "',dataFinalCotacao='" & [DataFormatada_API] & "')?$select=cotacaoCompra
```

*Nos detalhes deste link:*

'" & [Moeda] & "': Aqui, fazemos uma referência direta à coluna "Moeda" de nossa tabela.
'" & [DataFormatada_API] & "': Esta parte se refere à coluna "DataFormatada_API", garantindo que as datas estejam no formato adequado.

Assim, para adaptar o código ao nosso contexto, atualize no editor para:

```
let
...
#"Get Cotação" = Table.AddColumn(#"Coluna Personalizada Adicionada", "Cotação", each Json.Document(Web.Contents("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda='" & [Moeda] & "',dataInicialCotacao='" & [DataFormatada_API] & "',dataFinalCotacao='" & [DataFormatada_API] & "')?$select=cotacaoCompra")))
in
    #"Get Cotação"
```

Ao aplicar essa estrutura, conseguimos extrair, de forma dinâmica e em tempo real, as cotações das moedas conforme a necessidade de cada linha do nosso conjunto de dados. Isso garante uma análise atualizada e precisa, fundamentada em dados confiáveis, otimizando assim as tomadas de decisão.


### Decifrando Estruturas de Dados Complexas

Quando mergulhamos nas possibilidades avançadas do Power BI, especialmente ao lidar com dados obtidos diretamente de APIs, é comum encontrarmos colunas que aparentemente são simples, mas na realidade, ocultam estruturas de dados mais intrincadas. É aqui que entra o conceito de "Record" ou "List" em algumas dessas colunas. Estes termos indicam que a coluna contém informações aninhadas ou listas de valores, que, para serem efetivamente aproveitadas, precisam ser expandidas.

#### Por que é essencial expandir essas colunas?
1. **Acesso Integral aos Dados**: Ao nos depararmos com colunas marcadas como "Record" ou "List", isso indica que há dados subjacentes que não estão imediatamente visíveis. Expandir essas colunas nos permite ter uma visão completa desses dados.

2. **Clareza e Organização**: Muitas vezes, ao expandir essas colunas, os dados subjacentes são automaticamente organizados em novas colunas com nomes claros e descritivos, facilitando sua interpretação.

3. **Maximização da Análise**: Com todos os dados disponíveis de forma estruturada, podemos realizar análises mais profundas, criar visualizações mais detalhadas e tomar decisões mais informadas.

#### Como proceder com a expansão no Power Query do Power BI?
1. **Navegue até o Editor do Power Query**: A partir do Power BI Desktop, selecione "Editar Consultas".

2. **Identifique a Coluna Relevante**: No ambiente do editor, procure a coluna que apresenta valores como "Record" ou "List". Ao lado do nome da coluna, você perceberá um pequeno ícone, que pode ser uma seta ou uma tabela.

3. **Proceda com a Expansão**: 
    - Para colunas indicadas como "Record": Clique no ícone de seta. Uma janela se abrirá, mostrando todos os campos disponíveis contidos no "Record". Escolha os campos desejados e confirme. O Power Query criará colunas adicionais conforme os campos selecionados.
    -Para "List": Clique no ícone correspondente e opte por "Expandir para Novas Linhas". Isso transformará a lista em uma nova tabela, com cada item representado em uma linha separada.

4. **Conclua e Atualize**: Após realizar as expansões necessárias, selecione "Fechar e Aplicar" no Power Query. Você será redirecionado para o ambiente principal do Power BI, e seu modelo de dados será atualizado com as novas colunas.

O processo de expansão de colunas no Power BI não é apenas uma técnica. É um passo fundamental para garantir que todos os dados obtidos, especialmente de APIs, sejam completamente acessíveis e prontos para análise. Esta prática garante que você tenha uma visão completa e clara dos seus dados, maximizando o potencial de suas análises e insights.


## **Conclusão**

Ao longo deste material, destacamos a integração harmoniosa entre o Excel, Power BI e APIs, mostrando o potencial dessa combinação. Neste ponto você já deve observar perfeitamente esta integração.

Embora o propósito deste artigo não seja construir um painel completo, acredito que a exploração sobre a integração do Power BI com a API do Banco Central tenha sido elucidativa. O objetivo foi simplificar o processo, demonstrando que, com as ferramentas adequadas, é possível incorporar informações externas às nossas análises. O domínio de dados é dinâmico, e manter-se atualizado é fundamental para o sucesso em qualquer empreendimento. Espero ter ajudado. Até breve!