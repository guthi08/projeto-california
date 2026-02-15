import streamlit as st
import joblib
import pandas as pd

# Carregar o modelo
pipeline = joblib.load('modelo_california.pkl')

st.title('Previsão de Preços de Casas - Califórnia 🏠')

# Criando os campos para o usuário digitar
# Importante: A ordem e os nomes devem bater com o que o modelo espera
longitude = st.number_input('Longitude', value=-122.23)
latitude = st.number_input('Latitude', value=37.88)
housing_median_age = st.number_input('Idade da Casa', value=41.0)
total_rooms = st.number_input('Total de Quartos', value=880.0)
total_bedrooms = st.number_input('Total de Dormitórios', value=129.0)
population = st.number_input('População', value=322.0)
households = st.number_input('Ocupantes', value=126.0)
median_income = st.number_input('Renda Média (em dezenas de milhar)', value=8.3)
ocean_proximity = st.selectbox('Proximidade do Oceano', 
                              ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

# Botão para prever
if st.button('Calcular Preço'):
    # Criar um DataFrame com os dados (igual ao que usamos no treino)
    dados_input = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    })
    
    # Fazer a previsão
    preco = pipeline.predict(dados_input)
    
    st.success(f'O preço estimado é: ${preco[0]:,.2f}')
