import streamlit as st
import pandas as pd
import plotly.express as px

#Título do aplicativo na aba do navegador
st.set_page_config(page_title='Análise de Preço de Veículos', page_icon=':car:', layout='wide')

car_data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Análise de Preço de Veículos')

hist_button = st.sidebar.button('Histograma de Preço')

if hist_button:
    # escrever uma mensagem
    st.write('Criando um histograma de preço dos veículos')

    # criar o histograma
    fig = px.histogram(
        car_data,
        x='price',
        color_discrete_sequence=['#2E86C1'],
        title='Distribuição do Preço dos Veículos'
    )
    
      
    fig.update_layout(
        xaxis_title='Preço',
        yaxis_title='Quantidade de Veículos',
        font=dict(color='#222222'),
        xaxis=dict(tickfont=dict(color='#222222'), title_font=dict(color='#222222')),
        yaxis=dict(tickfont=dict(color='#222222'), title_font=dict(color='#222222'))
    )


    # exibir um gráfico plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# Botão gráfico de dispersão
scatter_button = st.sidebar.button('Gráfico de Dispersão')

if scatter_button:
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão dos veículos')

    # criar o gráfico de dispersão
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        opacity=0.3,
        color_discrete_sequence=['#2E86C1'],
        title='Relação entre Milhagem e Preço'
    )
    
    fig.update_layout(
        xaxis_title='Milhagem',
        yaxis_title='Preço'
    )
    
    # cor do texto dos eixos
    fig.update_layout(
        font=dict(color='#222222'),
        xaxis=dict(tickfont=dict(color='#222222'), title_font=dict(color='#222222')),
        yaxis=dict(tickfont=dict(color='#222222'), title_font=dict(color='#222222')),
    )

    # exibir um gráfico plotly interativo
    st.plotly_chart(fig, use_container_width=True)