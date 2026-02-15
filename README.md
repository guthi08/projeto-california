# 🏠 California Housing Prices Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.3-orange)
![Status](https://img.shields.io/badge/Status-Deploy%20✅-brightgreen)

Um projeto completo de Ciência de Dados (End-to-End), desde a análise exploratória até o deploy de um modelo de Machine Learning para prever preços de imóveis na Califórnia.

Este projeto foi desenvolvido seguindo os passos do livro **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"** (Aurélien Géron).

## 🔗 Demonstração Online
Acesse o aplicativo rodando em tempo real:
👉 **[CLIQUE AQUI PARA ACESSAR O APP](em breve)** 👈

---

## 🧠 Sobre o Projeto

O objetivo é utilizar dados do Censo da Califórnia (1990) para criar um modelo capaz de prever o valor mediano de uma casa em um determinado distrito (quarteirão), com base em características como localização, idade do imóvel, renda média dos moradores, etc.

### 🛠 Pipeline de Desenvolvimento
1.  **Coleta de Dados:** Utilização do dataset `California Housing` (StatLib repository).
2.  **Análise Exploratória (EDA):** Identificação de correlações, distribuição geográfica e limpeza de dados.
3.  **Engenharia de Features:** Criação de novas variáveis relevantes, como `bedrooms_per_room` e `population_per_household`.
4.  **Pré-processamento:** Tratamento de valores nulos (Imputation) e escalonamento (StandardScaler).
5.  **Modelagem:** Teste de vários algoritmos (Linear Regression, Decision Tree) e seleção do **Random Forest Regressor** como o melhor modelo.
6.  **Deploy:** Criação de uma interface web com **Streamlit** e hospedagem na nuvem.

---

## 📊 Resultados do Modelo

O modelo final (Random Forest) obteve os seguintes resultados no conjunto de teste:

-   **RMSE (Root Mean Squared Error):** ~$48,000
-   **Desempenho:** Superou os modelos lineares simples.

> **Nota:** Os dados são de 1990. Os valores monetários estão desatualizados para o mercado atual e servem apenas para fins educacionais de Machine Learning.
