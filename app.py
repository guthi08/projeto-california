import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# --- 1. DEFINIÇÃO DA CLASSE (Obrigatório estar aqui no topo!) ---
# Essa classe precisa existir antes do joblib carregar o modelo.
# Ela ensina ao Python o que é "CombinedAttributesAdder".

# Índices das colunas (baseado no dataset da Califórnia)
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    
    def fit(self, X, y=None):
        return self  # nada a fazer no fit
    
    def transform(self, X):
        # Evita erro se X for DataFrame, convertendo para numpy array
        if isinstance(X, pd.DataFrame):
            X = X.values
            
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


import __main__
setattr(__main__, "CombinedAttributesAdder", CombinedAttributesAdder)

# --- 2. CARREGAR O MODELO ---
# O arquivo .pkl deve estar na mesma pasta que este arquivo .py
pipeline = joblib.load('modelo_california.pkl')

# --- 3. A INTERFACE DO SITE (Streamlit) ---
st.title('Previsão de Preços de Casas - Califórnia 🏠')

st.write("""
### Descubra o valor estimado do seu imóvel
Preencha os dados abaixo para simular o preço baseado no Censo de 1990.
""")

# Criando colunas para ficar mais organizado visualmente
col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input('Longitude', value=-122.23)
    latitude = st.number_input('Latitude', value=37.88)
    housing_median_age = st.number_input('Idade da Casa (Anos)', value=41.0, min_value=1.0)
    total_rooms = st.number_input('Total de Quartos', value=880.0, min_value=1.0)
    total_bedrooms = st.number_input('Total de Dormitórios', value=129.0, min_value=1.0)

with col2:
    population = st.number_input('População no Bairro', value=322.0, min_value=1.0)
    households = st.number_input('Ocupantes (Famílias)', value=126.0, min_value=1.0)
    median_income = st.number_input('Renda Média (Dezenas de Milhar)', value=8.3)
    ocean_proximity = st.selectbox('Proximidade do Oceano', 
                                  ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

# Botão de Ação
if st.button('Calcular Preço 💰'):
    # Montar o DataFrame com os nomes EXATOS que o modelo espera
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
    
    try:
        # Fazer a previsão
        preco = pipeline.predict(dados_input)
        
        # Mostrar resultado formatado
        st.success(f'O preço estimado é: $ {preco[0]:,.2f}')
        st.balloons() # Efeito visual de festa
        
    except Exception as e:
        st.error(f"Erro na previsão: {e}")
