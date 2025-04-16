import streamlit as st
import pandas    as pd
from functions import calculo_resultados


# ----- Dataset Imports ------
df_crossprice = pd.read_csv('datasets/crossprice.csv')
df_elasticity = pd.read_csv('datasets/df_elasticity.csv')
x_price = pd.read_csv('datasets/x_price.csv')
y_demand = pd.read_csv('datasets/y_demand.csv')

st.title('Elasticidade de preço')

product_name = st.selectbox('Escolha a(s) loja(s):',x_price.columns.drop('week_number'))


x = df_elasticity.loc[df_elasticity['name'] == product_name]

if x.empty:
    st.write('Infelizmente esse produto não apresenta um valor de p-valor < 0.05 para gerar significância estatística')

else:
    
    discount = st.slider(min_value=0, max_value=30, step=1, label='Desconto', value=0)
    resultado = calculo_resultados(x_price, y_demand, df_elasticity, discount, product_name)



    st.subheader('Descrição', anchor=False)
    st.write(
        f'''
        - Faturamento atual: $ {resultado['faturamento_atual'].iloc[0]}.
        - Faturamento com redução de {discount}%: $ {resultado['faturamento_reducao'].iloc[0]}.
        - Diferença: $ {resultado['perda_faturamento'].iloc[0]}.
        '''
    )
    st.subheader('Descrição com variação da demanda', anchor=False)
    st.write(
        f'''
        - Faturamento atual: $ {resultado['faturamento_atual'].iloc[0]}.
        - Faturamento com aumento da demanda: $ {resultado['faturamento_novo'].iloc[0]}
        - Variação no faturamento: $ {resultado['variacao_faturamento'].iloc[0]} 
        - Variação percentual {resultado['variacao_percentual'].iloc[0]}%.
        '''
    )
