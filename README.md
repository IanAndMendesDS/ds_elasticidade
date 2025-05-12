# Elasticidade de preço

Esse é um projeto end-to-end de Data Science com modelo de regressão linear aplicada com o intuito de encontrar a elasticidade de preço dos produtos. No qual foi identificado a elasticidade de todos os produtos e como a mudança de preços de um produto afetam na categoria. Os resultados podem ser acessadas pelo usuário por meio do [link](https://price-elasticity.onrender.com), aplicando o desconto no produto e visualizando como isso afeta no faturamento anual da categoria.

# 1. Descrição e problema de negócio
## 1.1 Descrição
A elasticidade de preço é uma medida que indica a sensibilidade da demanda de um produto em relação às mudanças no seu preço. Ela é calculada dividindo-se a variação percentual na quantidade demandada pelo produto pela variação percentual no preço do produto.

O conceito de elasticidade de preços visa medir se, por exemplo, o aumento de preços impacta significativamente ou não na demanda do produto. Esse impacto sobre a demanda pode ser classificado como elasticidade de preços elástica, inelástica e unitária. Ainda é possível termos valores negativos representando a elasticidade de preços.

## 1.2 Problema de negócio
Foi recebido um dataset com dados de vendas de diversos E-commerce e com as seguintes tarefas:
- Descobrir qual E-commerce apresenta mais venda e quais categorias se descatam.
- Encontrar quais produtos podemos afirmar que há elasticidade de preços.
- Encontrar o faturamento anual da categoria após a aplicação da mudança no preço de um produto.

# 2. Premissas do negócio.
- Cada linha é um produto vendido.
- Para garantir uma significância estatística o p valor precisa ser menor que 0,05.
- Produtos que não apresentam significância estatística não terão sua elasticidade de preços considerada nos cálculos do faturamento anual da categoria.
- Para que a reta da regressão linear seja considerada com bom ajuste aos dados ela precisa ter um valor maior que 0,5.

# 3. Descrição dos dados
O conjunto de dados possui os seguintes atributos:

| Atributos	| Descrição |
| -- | -- |
| Date_imp_d | Data que a compra foi realizada|
| Category_name |	Nome da Categoria|
| name |	Nome do produto|
| price |	Preço do Produto|
| disc_price |	Preço do produto após o desconto aplicado na venda|
| merchant |	Identificador do E-commerce|
| Disc_percentage |	Percentual de desconto|
| isSale |	Indicador se foi venda ou não|
| Imp_count |Contagem de vendas no período|
| brand |	Marca|
| p_description | Descrição do produto|
| dateAdded |	Data que o produto foi adicionado ao estoque|
| dateSeen |	Data que o produto saiu do estoque|
| dateUpdated |	Data de atualização da transação|
| manufacturer |	Criador do produto|
| Day_n |	Dia da semana por escrito|
| month |	Mês em número|
| month_n |	Mês em escrito|
| day |	Dia em número|
| Week_Number |	Número da semana|

# 3. Estratégia de solução
Para a resolução do problema foi utilizado a metodologia CRISP-DM

![CRISP-DS](https://github.com/user-attachments/assets/08db5699-27b9-483b-8b10-d71949ca8415)


## 3.1 Fases do CRISP-DM

1. Definição do Problema de Negócio: Identificar stakeholders e objetivos.
2. Compreensão do Negócio: Alinhar expectativas e prototipar soluções.
3. Coleta de Dados: Agregar dados.
4. Limpeza de Dados: Tratar valores ausentes, outliers e inconsistências.
5. Análise Exploratória: Descobrir padrões e criar hipóteses.
6. Modelagem dos Dados: Aplicar transformações estatísticas e feature engineering.
7. Treinamento de Algoritmos: Aplicar regresão linear.
8. Bussiness Performance: A partir dos produtos encontrados, aplicar desconto para observar como a demanda irá reagir.
9. Deploy da Solução: Publicação do modelo em um ambiente de produção em nuvem (Streamlit).

## 3.2 Ferramentas utilizadas
- Python, Pandas, Matplotlib e Seaborn.
- VSCode.
- Linear Regresion on Statsmodel.
- Streamlit Python framework web.
- Render.
- Git e Github.
  
# 4 Trabalhos Futuros
- Realizar uma EDA mais aprofundada na categoria de Laptops e Computadores da Best Buy.
- Através dessa EDA visar explicar quais são os melhores produtos e procurar indícios que expliquem sua elasticidade de preços.
- Utilizar outras formas de calcular a elasticidade de preços.
- Otimizar o web app de forma de fique mais funcional para seus usuários.

