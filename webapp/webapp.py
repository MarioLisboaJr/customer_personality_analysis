#importar bibliotecas
import pandas as pd
import streamlit as st
import joblib
import time


#configuração padrão da página
st.set_page_config(page_title='Customer Segmentation', layout='centered')


#descrição
st.markdown('<div style="text-align: center"><h1> ANÁLISE EXPLORATÓRIA DE DADOS </div>',unsafe_allow_html=True)
st.markdown('<div style="text-align: center"><h3> (Segmentação de Clientes e Criação de Modelo Preditivo) </div>',unsafe_allow_html=True)

st.caption('<div style="text-align: left"><h2> ANÁLISE DE PERSONALIDADE DO CLIENTE </div>',unsafe_allow_html=True)
st.write('<div style="text-align: justify"> A Análise de Personalidade do Cliente é uma análise detalhada dos clientes ideais de uma empresa. Ajuda uma empresa a entender melhor seus clientes e facilita a modificação de produtos de acordo com as necessidades, comportamentos e preocupações específicas de diferentes tipos de clientes. </div>',unsafe_allow_html=True)

st.caption('<div style="text-align: left"><h2> DECLARAÇÃO DO CASO </div>',unsafe_allow_html=True)
st.write('<div style="text-align: justify"> Considere uma empresa bem estabelecida que opera no setor de varejo. Atualmente eles têm cerca de centenas de milhares de clientes cadastrados e atendem quase um milhão de consumidores por ano. Vendem produtos de 6 grandes categorias: ouros, vinhos, carnes raras, frutas exóticas, peixes e produtos doces.<p><p> Os clientes podem encomendar e adquirir produtos através de 3 canais de venda: lojas físicas, catálogos e site da empresa. Globalmente, a empresa teve receitas sólidas e uma linha de fundo saudável nos 3 anos anteriores, mas as perspectivas de crescimento do lucro para os próximos 3 anos não são promissoras... várias iniciativas estratégicas estão sendo consideradas para reverter esta situação. Uma delas é melhorar a desempenho das atividades de marketing, com foco especial nas campanhas de marketing.<p><p> Percebendo a importância de se ter uma abordagem mais quantitativa na tomada de decisões, a empresa contratou um pequeno grupo de cientistas de dados com um objetivo claro em mente: construir um modelo preditivo que apoiará as iniciativas de marketing direto. </div>',unsafe_allow_html=True)

st.caption('<div style="text-align: left"><h2> OBJETIVO </div>',unsafe_allow_html=True)
st.write('<div style="text-align: justify"> O objetivo é construir um modelo preditivo que produza o maior lucro para a próxima campanha de marketing direto. A nova campanha, sexta, visa vender um novo gadget para os clientes. Para construir o modelo, uma campanha piloto envolvendo 2.240 clientes foi realizada. Os clientes foram selecionados aleatoriamente e contatados por telefone sobre a aquisição do gadget. Durante os meses seguintes, os clientes que compraram a oferta foram devidamente rotulados.<p><p> O objetivo da equipe é desenvolver um modelo que preveja o comportamento do cliente e aplicá-lo ao restante da base de clientes. Felizmente, o modelo permitirá que a empresa escolha os clientes com maior probabilidade de comprar a oferta deixando de fora os não respondentes, tornando a próxima campanha altamente rentável. Além de maximizar o lucro da campanha, tem-se o interesse também do entendimento das características dos clientes da empresa. </div>',unsafe_allow_html=True)

st.caption('<div style="text-align: left"><h2> RESULTADOS E CÓDIGOS DESTA ANÁLISE EM PYTHON: </div>',unsafe_allow_html=True)
st.markdown('##### [Jupyter Notebook](https://github.com/MarioLisboaJr/customer_personality_analysis/blob/main/notebook/notebook.ipynb)' ,unsafe_allow_html=True)


#barra lateral
#parâmetros do modelo
x = {
    'Número de dias desde a última compra:': 5,
    'Tempo como cliente da empresa:': 10,
    'Valor gasto em carnes nos últimos dois anos:': 1,
    'Número de compras realizadas nas lojas físicas:': 2,
    'Número de visitas no site da empresa no último mês:': 6,
    'Total de campanhas de marketing que o cliente já participou:': 1,
    'Grau de escolaridade:': 1    
    }

#ajustar campos no streamlit
st.sidebar.caption('# Insira as informações sobre os cliente abaixo e descubra se vale a pena direcionar a campanha para ele ou não:')

for item in x:
    
    if item == 'Tempo como cliente da empresa:':
        valor = st.sidebar.number_input(label=f'{item}', value=10 ,step=1, min_value=0, help='Informação em Anos')
    
    elif item == 'Grau de escolaridade:':
        valor = st.sidebar.selectbox(label=f'{item}', options=('Ensino Médio', 'Ensino Superior', 'Pós-Graduação'))
        if valor == 'Ensino Médio':
            valor = 1
        elif valor == 'Ensino Superior':
            valor = 2
        else:
            valor = 3
    
    elif item == 'Total de campanhas de marketing que o cliente já participou:':
        valor = st.sidebar.slider(label=f'{item}' ,min_value=0, value=1, max_value=5, step=1)
    
    else:
        valor = st.sidebar.number_input(label=f'{item}',value=x[item], step=10, min_value=0)
    
    #receber valores do input    
    x[item] = valor

#tratar dados do input e padronizar com os dados do treino    
data = {
    'Recency': [49.012635, 28.948352], 
    'Enrollment_Time': [8.971570, 0.685618],
    'MntMeatProducts': [166.995939, 224.283273],
    'NumStorePurchases': [5.800993, 3.250785],
    'NumWebVisitsMonth': [5.319043, 2.425359],
    'AcceptedAnyCmp': [0.298285, 0.679209], 
    'Education': [2.267148, 0.652084]    
}
df = pd.DataFrame(data, index=['mean', 'std'])
mean = df[df.index=='mean']
std = df[df.index=='std']

#padronizar input
valores_x = pd.DataFrame(x, index=[0])
valores_x = (valores_x.values - mean.values)/std.values

#criar botao para rodar modelo
st.sidebar.markdown("<br>", unsafe_allow_html=True)
botao = st.sidebar.button('Classificar Cliente')
if botao:
    
    #importar modelo treinado
    modelo = joblib.load('webapp/modelo_classificacao.joblib')
    
    #fazer previsão
    classificar = modelo.predict(valores_x)
    
    prob_predict = modelo.predict_proba(valores_x)
    class_0 = prob_predict[0][0]
    class_1 = prob_predict[0][1]
    
    #aguardar conclusão da previsão
    with st.sidebar:
        with st.spinner('Aguarde um momento...'):
            time.sleep(1)
    
    #exibir resultado
    if classificar[0] == 1:
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        st.sidebar.success(
        '### Cliente em potencial. Oferecer 6ª campanha!\n###### *{:.2%} de chance do cliente aceitar a oferta.'.format(class_1)
                  )
    else:
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        st.sidebar.error(
        '### Cliente não possui perfil para 6ª campanha!\n###### *{:.2%} de chance do cliente não aceitar a oferta.'.format(class_0)
                )
        
st.sidebar.markdown("<br>", unsafe_allow_html=True)
        
#video
st.caption('<div style="text-align: left"><h2> APRESENTAÇÃO DOS RESULTADOS: </div>',unsafe_allow_html=True)

video_file = open(r'apresentacao/apresentacao.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


#rodape
github = f"<a href='https://github.com/MarioLisboaJr'><img src='https://cdn-icons-png.flaticon.com/512/733/733553.png' height='40' width='40'></a>"
linkedin = f"<a href='https://www.linkedin.com/in/mario-lisboa/'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' height='40' width='40'></a>"
portfolio = f"<a href='https://lisboamario.wixsite.com/website'><img src='https://img.icons8.com/clouds/344/external-link.png' height='50' width='50'></a>"

st.markdown(f"<div style='text-align: center'><br><br><br>{github}&ensp;{linkedin}&ensp;{portfolio}<p>{'Mário Lisbôa'}</div>",
            unsafe_allow_html=True)
