import streamlit as st
import pandas as pd 
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

#Cabeçalho do aplicativo
st.header('Análise de Preço de Veículos')

hist_button = st.sidebar.button('Histograma de Preço')

if hist_button:
    #escrever uma mensagem
    st.write('Criando um histograma de preço dos veículos')
    
    # criar o histograma
    fig = px.histogram(car_data, x='price', title='Distribuição do Preço dos Veículos',  template='plotly_white')
    
    #exibir um grafico plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    
#Botão grafico de dispersão
scatter_button = st.sidebar.button('Gráfico de Dispersão')

if scatter_button:
    #escrever uma mensagem
    st.write('Criando um gráfico de dispersão dos veículos')
    
    # criar o gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='price', title='Relação entre Quilometragem e Preço', template='plotly_white')
    
    #exibir um grafico plotly interativo
    st.plotly_chart(fig, use_container_width=True)