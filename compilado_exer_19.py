# gerando arquivo csv

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

# importando as bibliotecas, carregando os dados do arquivo csv e criando data frame

import seaborn as sns
import pandas as pd

preco_df = pd.read_csv("/content/Data_analist_project/gasolina.csv",sep=',') 

# vizualizando head dataframe 

preco_df

# gerando grafico de linhas 

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=preco_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Variação Preço Gasolina', xlabel='Dia', ylabel='Preço');

# salvando grafico em png

grafico.get_figure().savefig('/content/preco_gasolina.png')