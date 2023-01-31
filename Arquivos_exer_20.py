%%writefile gasolina.csv
dia,venda
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

import seaborn as sns
import pandas as pd

preco_df = pd.read_csv("/content/Data_analist_project/gasolina.csv",sep=',') 

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=preco_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço Gasolina Últimos 10 dias', xlabel='Dia', ylabel='Preço');

grafico.get_figure().savefig('/content/preco_gasolina.png')  