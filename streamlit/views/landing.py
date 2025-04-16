import streamlit as st

st.title('Elasticidade de preço')


# -- Sobre o projeto ----
st.write(
    '''Essa aplicação foi desenvolvida para um e-commerce para prever e entender a elasticidade de preço na sua base de 
    produtos eletrônicos.'''
)

# --- Objetivo ----
st.write('\n')
st.subheader('Objetivo', anchor=False)
st.write(
    '''
    - A elasticidade de preço é uma medida que indica a sensibilidade da demanda de um produto em relação às mudanças no seu preço.
    - Com base nessa aplicação, é possível tomar decisões estratégicas e maximizar o faturamento da empresa.
    '''
)

# ---- Premissas de Negócio ----- #
st.write('\n')
st.subheader('Critérios elegibilidade', anchor=False)
st.write(
    '''
    - A probabilidade de obter os resultados observados caso a hipótese nula seja verdadeira (p-valor) tem que ser < 0.05
    '''
)
