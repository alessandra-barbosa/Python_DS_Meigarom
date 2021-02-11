import pandas as pd
data=pd.read_csv('datasets/kc_house_data.csv')

#1. Quantas casas estão disponíveis para compra? 21613
print(data.shape[0])

# #2. Quantos atributos as casas possuem? 21
print(data.shape[1])
#
# #3. Quais são os atributos das casas?
print(data.columns)
# #['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors', 'waterfront', 'view',
# # 'condition', 'grade',# 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode','lat', 'long',
# # 'sqft_living15', 'sqft_lot15']

# #4. Qual a casa mais cara (casa com o maior valor de venda )? Id = 6762700020 e custa $ 7.700.000,00
print(data[['id','price']].sort_values('price',ascending=False))
#
# #5. Qual a casa com o maior número de quartos? Id=2402100895 e tem 33 quartos
print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False))
#
# #6. Qual a soma total de quartos do conjunto de dados? A soma de quartos è 72854
print(data['bedrooms'].sum())
#
# #7. Quantas casas possuem 2 banheiros? R:1930
# print(data.loc[data['bathrooms']==2])
print(data[data['bathrooms']==2].shape)
# #8.Qual o preço médio de todas as casas no conjuno de dados? R: 540.088,14
# #print(data['price'].describe())
print(data['price'].mean())
#
# #9. Qual o preço médio de casas com 2 banheiros? O preço médio de casas com 2 banheiros é de R$ 457889.72
# df2bath=data.loc[data['bathrooms']==2]
# print(df2bath['price'].mean())
print(data.loc[data['bathrooms']==2, 'price'].mean())

# #10. Qual o preço mínimo entre as casas com 3 quartos? O preço mínimo de casa com 3 quartos é R$ 82.000,00
# df3bed=data.loc[data['bedrooms']==3]
# print(df3bed[['bedrooms','price']].sort_values('price'))
print(data.loc[data['bedrooms']==3,'price'].min())
# #11.Quantas casas possuem mais de 300 metros quadrados na sala de estar? # R:21612
# print(data.loc[data['sqft_living15']>300])
data['m2_living']=data['sqft_living']*0.092
print(data[data['m2_living']>300].shape)

# #12. Quantas casas tem mais de 2 andares? São 782 casas com mais de 2 andares
# print(data.loc[data['floors']>2])
print(data[data['floors']>2].shape)
# #13. Quantas casas tem vista para o mar? 163 casas tem vista para o mar
# print(data.loc[data['waterfront']==1])
print(data[data['waterfront']==1].shape)
# #14. Das casas com vista para o mar, quantas tem 3 quartos? 64
# dfwaterfront=data.loc[data['waterfront']==1]
# print(dfwaterfront.loc[dfwaterfront['bedrooms']==3])
print(data[(data['waterfront']==1) & (data['bedrooms']==3)].shape)
# #
# 15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros? 11242
# df300living=data.loc[data['sqft_living']>300]
# print(df300living.loc[df300living['bathrooms']>2])
print(data[(data['m2_living']>300) & (data['bathrooms']>2)].shape)