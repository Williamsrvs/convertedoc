import streamlit as st
import pandas as pd
import openpyxl
from PIL import Image

# Carregar a logo no menu lateral com tamanho de 150x150 pixels
image = Image.open('LOGO.png')
image = image.resize((150, 150))  # Ajuste conforme necessário
st.sidebar.image(image)


# Dados Contato
st.sidebar.markdown("Soluções inteligentes é com a Date Analytics")
st.sidebar.markdown("Este projeto totalmente desenvolvido em Python, tem sua finaliade em organizar, ajustar ou converter aquelas planilhas antes bagunçadas e desorganizadas com linhas e colunas em branco.")
st.sidebar.markdown("Village das Fontes Nº 770 - Benedito Bentes")
st.sidebar.markdown("Email: dateanalytics@outlook.com")
st.sidebar.markdown("Acesse agora mesmo nosso portifólio e saiba mais [http://wrportifolio.streamlit.app](http://wrportifolio.streamlit.app)")

st.title("Resolva o problema da sua planilha Excel com um simples comando.")
st.markdown("Esta página consegue ajustar sua planilha que possuí linhas vazias e colunas e organiza tudo pra você.")

# Carregar a planilha Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type="xlsx")

if uploaded_file is not None:
    # Ler a planilha Excel usando o openpyxl como engine
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Remover linhas e colunas vazias
    df.dropna(how='all', inplace=True)  # Remove linhas completamente vazias
    df.dropna(axis=1, how='all', inplace=True)  # Remove colunas completamente vazias

    # Exibir o DataFrame
    st.dataframe(df)
