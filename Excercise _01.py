#carregue o conjunto de dados chamado kc_house _data.csv
#funcao_read_csv()
#biblioteca_pandas
import pandas as pd

data=pd.read_csv('datasets/kc_house_data.csv')

#mostre as primeiras 5 linhas do conjunto de dados
#print(data.head())
#mostre o numero de linhas e colunas do conjunto de dados
#print(data.shape)
#mostre o nome das colunas
#print(data.columns)
#mostre os dados ordenados da coluna price
#print(data[['id','price']].sort_values('price'))
#mostre os dados ordenados da coluna price do maior pro menor
#print(data[['id','price']].sort_values('price',ascending=False))

#Exercicio
print(data.head())
#1. Quantas casas estão disponíveis para compra? 21613
print(data.shape)

#2. Quantos atributos as casas possuem? 21
#print(data.shape)

#3. Quais são os atributos das casas?
print(data.columns)
#['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors', 'waterfront', 'view',
# 'condition', 'grade',# 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode','lat', 'long',
# 'sqft_living15', 'sqft_lot15']

#4. Qual a casa mais cara ( casa com o maior valor de venda )? Id = 6762700020

print(data[['id','price']].sort_values('price',ascending=False))

#5. Qual a casa com o maior número de quartos? Id=2402100895
print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False))

#6. Qual a soma total de quartos do conjunto de dados? A soma de quartos è 72854
print(data['bedrooms'].sum())

#7. Quantas casas possuem 2 banheiros? R:1930
print(data[['id','bathrooms']].query('bathrooms==2'))

#8.Qual o preço médio de todas as casas no conjuno de dados? R: 540.088,14
#print(data['price'].describe())
print(data['price'].mean())

#9. Qual o preço médio de casas com 2 banheiros? O preço médio de casas com 2 banheiros é de R$ 457889.72
df2bath = data.query('bathrooms==2')
print(df2bath['price'].mean())

#10. Qual o preço mínimo entre as casas com 3 quartos? O preço mínimo de casa com 3 quartos é R$ 82.000,00
df3bed=data.query('bedrooms==3')
print(df3bed[['bedrooms','price']].sort_values('price'))

#11.Quantas casas possuem mais de 300 metros quadrados na sala de estar? # R:21612
df300=data[['sqft_living','bathrooms']].query('sqft_living>300')
print(df300)

#12. Quantas casas tem mais de 2 andares? São 782 casas com mais de 2 andares
df2floors=data[['floors','price']].query('floors>2')
print(df2floors)

#13. Quantas casas tem vista para o mar? 163 casas tem vista para o mar
dfwaterfront=data[['bedrooms','waterfront']].query('waterfront==1')
print(dfwaterfront)

#14. Das casas com vista para o mar, quantas tem 3 quartos? 64
print(dfwaterfront.query('bedrooms==3'))

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros? 11242
print(df300.query('bathrooms>2'))

#9. Qual o preço médio de casas com 2 banheiros? O preço médio de casas com 2 banheiros é de R$ 457889.72
df2bath = data.loc[data['bathrooms']==2]
print(df2bath['price'].mean())