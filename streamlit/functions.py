import streamlit as st
import pandas as pd
import numpy as np


def calculo_resultados(x_price, y_demand, df_elasticity, desconto, product_name):

    resultado_faturamento = []

    desconto_right = (desconto/100)
    desconto_left = 1 - desconto_right
    

    for i in df_elasticity.index:
        preco_atual_medio = x_price[df_elasticity['name'][i]].mean()
        demanda_atual = y_demand[df_elasticity['name'][i]].sum()

        reducao_preco = preco_atual_medio*desconto_left
        aumento_demanda = -desconto_right*df_elasticity['price_elasticity'][i]

        demanda_nova = aumento_demanda * demanda_atual

        faturamento_atual = preco_atual_medio * demanda_atual
        faturamento_novo = reducao_preco * demanda_nova

        faturamento_reducao = faturamento_atual*desconto_left

        perda_faturamento = faturamento_atual-faturamento_reducao

        variacao_faturamento = faturamento_novo - faturamento_atual

        variacao_percentual = ((faturamento_novo - faturamento_atual)/faturamento_atual)*100


        resultado_faturamento.append({
        'name': df_elasticity['name'][i],
        'faturamento_atual': faturamento_atual.round(2),
        'faturamento_reducao': faturamento_reducao.round(2),
        'perda_faturamento': perda_faturamento.round(2),
        'faturamento_novo': faturamento_novo.round(2),
        'variacao_faturamento': variacao_faturamento.round(2),
        'variacao_percentual': variacao_percentual.round(2)
        })

    df_resultado = pd.DataFrame(resultado_faturamento)

    return df_resultado[df_resultado['name'] == product_name ]