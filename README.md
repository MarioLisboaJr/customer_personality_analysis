<div style="text-align: center">
    <h1> ANÁLISE EXPLORATÓRIA DE PERSONALIDADE DOS CLIENTES E CRIAÇÃO DE MODELO PREDITIVO PARA CAMPANHA DE MARKETING </h1>
    <h3> Modelo de Aprendizado não Supervisionado e Supervisionado </h3><br>
</div>


![](https://static.wixstatic.com/media/bc4e926ab4e3446c9117372d11e32803.jpg/v1/fill/w_1175,h_550,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Archery%20Board%20natureza.jpg)

<br>
<br>


<div style="text-align: left;">
    <a href="https://mariolisboajr-customer-personality-analysis-webappwebapp-a6snr3.streamlitapp.com/"><img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width=15%></a>        
</div> 

A análise de personalidade do cliente é uma análise detalhada que permite entender melhor seus clientes e facilita a modificação de produtos de acordo com as necessidades, comportamentos e preocupações específicas de diferentes tipos de clientes.
Considerando uma empresa de varejo, este trabalho traz um estudo sobre as características dos clientes de uma empresa e desenvolve um modelo de previsão que possibilite um melhor direcionamento em uma campanha de marketing direto. Assim, torna-se possível a escolha dos clientes com maior probabilidade de comprar a oferta, deixando de fora os não respondentes, maximizando então a rentabilidade da campanha.

<br>
<br>
<hr>

<h2> DECLARAÇÃO DO CASO </h2>

<br>

Considere uma empresa bem estabelecida que opera no setor de varejo. Atualmente eles têm cerca de centenas de milhares de clientes cadastrados e atendem quase um milhão de consumidores por ano. Vendem produtos de 6 grandes categorias: ouros, vinhos, carnes raras, frutas exóticas, peixes e produtos doces. <br>

Os clientes podem encomendar e adquirir produtos através de 3 canais de venda: lojas físicas, catálogos e site da empresa. Globalmente, a empresa teve receitas sólidas e uma linha de fundo saudável nos 3 anos anteriores, mas as perspectivas de crescimento do lucro para os próximos 3 anos não são promissoras... várias iniciativas estratégicas estão sendo consideradas para reverter esta situação. Uma delas é melhorar o desempenho das atividades de marketing, com foco especial nas campanhas diretas.

<hr>

<h2> OBJETIVO </h2>

<br>

**1) Criar grupos de clientes com características similares, traçando perfis de consumidores**

**2) Criar modelo preditivo que encontre consumidores ideais para campanha de marketing**

Desenvolvimento:

- Extrair, Tratar e Limpar Dados
- Realizar Feature Engineering
- Realizar Análise Exploratória
- Segmentar Clientes
- Criar Modelo Preditivo
- Criar Apresentação as Partes Interessadas do Negócio
- Disponibilizar Modelo para Utilização

**Desenvolvimento do Projeto**: [Aqui](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/notebook/notebook.ipynb)
    
**Modelo Preditivo no Streamlit**: [Aqui](https://mariolisboajr-customer-personality-analysis-webappwebapp-a6snr3.streamlitapp.com/)

**Apresentação de Negócio**: [Aqui](https://github.com/MarioLisboaJr/customer_personality_analysis/tree/main/apresentacao)
    
<hr>

<h2> INFORMAÇÃO SOBRE OS DADOS </h2>

A base de dados possui informações sobre 29 características de 2.240 clientes de uma empresa de varejo.

**Conteúdo do DataSet:**

**ID**: Identificador exclusivo <br/>
**Year_Birth**: Ano de nascimento<br/>
**Education**: Nível de escolaridade <br/>
**Marital_Status**: Estado civil <br/>
**Income**: Renda familiar anual <br/>
**Kidhome**: Número de crianças em casa <br/>
**Teenhome**: Número de adolescentes na casa <br/>
**Dt_Customer**: Data do cadastro do cliente na empresa <br/>
**Recency**: Número de dias desde a última compra do cliente <br/>
**Complain**: 1 se o cliente reclamou nos últimos 2 anos, 0 caso contrário <br/>
**MntWines**: Valor gasto em vinho nos últimos 2 anos <br/>
**MntFruits**: Valor gasto em frutas nos últimos 2 anos <br/>
**MntMeatProducts**: Valor gasto em carne nos últimos 2 anos <br/>
**MntFishProducts**: Valor gasto em pescado nos últimos 2 anos <br/>
**MntSweetProducts**: Valor gasto em doces nos últimos 2 anos <br/>
**MntGoldProds**: Valor gasto em ouro nos últimos 2 anos <br/>
**NumDealsPurchases**: Número de compras feitas com desconto <br/>
**AcceptedCmp1**: 1 se o cliente aceitou a oferta na 1ª campanha, 0 caso contrário <br/>
**AcceptedCmp2**: 1 se o cliente aceitou a oferta na 2ª campanha, 0 caso contrário <br/>
**AcceptedCmp3**: 1 se o cliente aceitou a oferta na 3ª campanha, 0 caso contrário <br/>
**AcceptedCmp4**: 1 se o cliente aceitou a oferta na 4ª campanha, 0 caso contrário <br/>
**AcceptedCmp5**: 1 se o cliente aceitou a oferta na 5ª campanha, 0 caso contrário <br/>
**Response**: 1 se o cliente aceitou a oferta na última campanha, 0 caso contrário <br/>
**NumWebPurchases**: Número de compras realizadas através do site da empresa <br/>
**NumCatalogPurchases**: Número de compras feitas usando um catálogo <br/>
**NumStorePurchases**: Número de compras feitas diretamente nas lojas <br/>
**NumWebVisitsMonth**: Número de visitas ao site da empresa no último mês <br/>

<hr>

<h2> ANÁLISE EXPLORATÓRIA </h2>

**Características dos Clientes**:

- 50% têm graduação completa, 38% possuem algum tipo de pós-graduação e apenas 11% possuem no máximo o ensino médio
- 65% possuem algum relacionamento contra 35% vivendo sozinho
- 80% possuem no máximo um dependente
- Tem em sua maioria entre 30 e 65 anos
- Possuem renda anual média de 25.000 a 75.000UM

**Principais insights obtidos dos dados**:

- **O site não parece ser um bom cartão de visita**: <br>
Um maior número de visitas ao site não resulta em mais compras pela internet e influencia negativamente nas compras dos outros canais de venda.
<br> 
 
- **Empresa não é muito atrativa para famílias maiores**:<br>
80% dos clientes possuem no máximo um dependente, sendo destes, mais de 60% sem nenhum. Além disto, temos que pessoas com mais dependentes tendem a gastar menos, o que vai de contra ao esperado.
<br>

- **Ainda existe uma boa margem para novas campanhas de marketing**:<br>
Cerca de 70% dos entrevistados só aceitaram uma oferta e ainda existe 79% de clientes que não participaram de nenhuma campanha. Temos também que os mais interessados na nova campanha participaram ativamente em mais das anteriores, indicando uma possível satisfação com o resultado.

<hr>

<h2> SEGMENTAÇÃO DE CLIENTES </h2>

Foi utilizado o algoritmo K-Means para criar três classes de clientes:
<br>
![](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/outputs/output_61_0.png?raw=true)
![](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/outputs/output_77_0.png?raw=true)
<br>

Características dos grupos de clientes:

**Cluster 0**: <br>
Os clientes que pertencem a este grupo possuem uma **renda anual acima da média** e por isso acabam **gastando mais no geral**, em todas as categorias de produtos. Possuem uma maior preferência por **compras através dos catálogos e lojas físicas**, sendo neste, o canal que mais compras realizou. **Descontos não parece ser um chamativo muito grande** para eles, visto que sua utilização ficou bem abaixo da média. Outra característica forte deste grupo é que eles **visitam bem pouco o site da empresa**.<br>
**Possuem menos dependentes** e, de todas as campanhas de marketing já realizadas, este grupo foi o que **mais interesse teve nas ofertas**.

**Cluster 1**: <br>
O maior grupo, se caracteriza pelos clientes com **renda abaixo da média**, e, com consequência, **acabam por consumir menos**, tanto em valor gasto quanto em quantidade de compras, para todos os produtos e em todos os canais de venda. Mesmo com uma renda média menor, **não se destacam pelo número de descontos utilizados**. Já para o **número de reclamações, estão acima da média**, apesar de a empresa ter este índice baixíssimo. Neste grupo temos a **menor adesão geral às campanhas de marketing**.

**Cluster 2**: <br>
Estes clientes são os **intermediários**, representam aqui nosso menor grupo. Sua **renda anual se aproxima bastante de uma renda média** de todos os clientes. Fato que chama atenção é que este grupo é o que **mais realiza compras no site**, e são também os que **mais utilizam descontos**.

<hr>

<h2> MODELO PREDITIVO </h2>

Para criação do modelo foi testado cinco algoritmos diferentes:

- Random Forest
- Suport Vector Machine
- Logistic Regression
- K Neighbor Nearest
- Gradient Booster

Após o teste inicial o modelo **Logistic Regression** foi escolhido por algumas razões:

Como neste nosso problema precisamos encontrar a maioria dos clientes em potencial da nossa nova campanha, temos então um **alto custo associado ao Falsos Negativos**, pois, caso tenhamos um cliente em potencial não detectado pelo modelo, diminuímos a taxa de sucesso da nossa campanha e consequentemente diminuiremos o seu retorno. Para melhor avaliar esta situação utilizamos da **métrica de Recall**.

Analisando principalmente este indicador, percebemos que Logistic Regression e K Nearest Neighbor se destacam com Recall de 81%. Como Logistic Regression aparece ligeiramente melhor, com Acuracidade de 82% contra 77%, optamos pela escolha deste modelo.

<hr>

<h2> RESULTADOS DO MODELO </h2>

<br>

![](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/outputs/output_94_0.png?raw=true)

<br>
Relatório de Classificação:

               precision    recall  f1-score   support

           0       0.95      0.82      0.88       279
           1       0.46      0.79      0.58        53

    accuracy                           0.82       332

<br>

O modelo de Regressão Logística final leva em consideração sete características para prever os clientes potenciais a aderirem a próxima campanha. <br>

São elas: <br>

1) Número de dias desde a última compra; <br>
2) Valor gasto em carnes nos últimos dois anos; <br>
3) Total de campanhas de marketing que o cliente já participou; <br>
4) Anos como cliente da empresa; <br>
5) Número de compras realizadas nas lojas físicas; <br>
6) Número de visitas no site da empresa no último mês; <br>
7) Grau de escolaridade: Menor ou igual ao ensino médio completo, graduação ou pós-graduação.

**O resultado obtido foi:**

- Identificação de 42 dos 53 clientes (79%) que aceitaram a oferta do projeto piloto. Relembrando que a identificação destes clientes é o fator crucial para o sucesso da campanha; <br>


- Um direcionamento da campanha para 50 clientes não interessados dentro dos 279 conhecidos, representando um erro de 18%. A oferta a clientes não interessados impacta em um maior custo para a divulgação da campanha; <br>


- Modelo final atingiu uma precisão geral de 82% de acuracidade.

**Perfil de cliente para a próxima campanha de marketing**:

- Não são casados
- Possuem maior escolaridade
- Têm preferência por vinhos e carnes
- Visitam mais o site
- Compram mais por catálogos
- Não frequentem muito as lojas físicas
- São fregueses a mais tempo
- Participam de mais campanhas
- Compram com mais frequência

Lembrando que, para um maior sucesso da campanha o entendimento dos produtos ofertados é crucial, bem como o entendimento de sua sazonalidade, se existir, e dos meios de divulgação a serem utilizados. Necessitando assim de uma análise também destes dados aqui não contidos. 

Quanto à maximização dos lucros, tem de se levar em conta os custos fixos e variáveis da campanha. Com isso, depois de classificar todos os clientes da empresa com o modelo obtido, conseguiremos descobrir qual o ponto de equilíbrio desta oferta, tornando possível a análise da sua viabilidade antes da execução. Caso não visualizem um cenário satisfatório, tentar buscar minimizar os custos ou tentar angariar mais clientes, deixando o produto mais atrativo, para assim tornar a campanha mais lucrativa.

<hr>

<h2> APRESENTAÇÃO AS PARTES INTERESSADAS </h2>

<br>

![](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/apresentacao/apresentacao.gif?raw=true)
<br>

**Apresentação de Negócio**: [Aqui](https://github.com/MarioLisboaJr/customer_personality_analysis/tree/main/apresentacao)

<hr>

<br>

**Desenvolvimento do Projeto**: [Aqui](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/notebook/notebook.ipynb)

**Desenvolvimento do Web App no Streamlit**: [Aqui](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/webapp/webapp.py)

<div style="text-align: left;">
    <a href="https://mariolisboajr-customer-personality-analysis-webappwebapp-a6snr3.streamlitapp.com/"><img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width=15%></a>        
</div> 

<br>

<hr>

<h2> AUTOR </h2>

Mário Lisbôa <br>
Pós-Graduando em Data Science e Analytics - USP [🔗](https://mbauspesalq.com/cursos/mba-em-data-science-e-analytics) <br>

<div style="text-align: left;">
        <br>
        <br>
        <a href="https://www.linkedin.com/in/mario-lisboa/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width=15%>
    </a> 
</div>      
