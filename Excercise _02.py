# ====================================================================
# #Aula 002
# ======================================================================
import pandas as pd
data=pd.read_csv('Datasets/kc_house_data.csv')
data['date']=pd.to_datetime(data['date'])
# print(data.head(10))
# data['sqft_living']=data['sqft_living'].astype(float)
# data['bedrooms']=data['bedrooms'].astype(float)
# print(data.dtypes)
# data['nome']='Alessandra'
# print(data.columns)
# data=data.drop('nome', axis= 1)

    ### A - Qual data do imovel mais antiga do portfolio?
#print(data[['id','date']].sort_values('date', ascending=True))

    ### B - Quantos imoveis possuem 0 numero maximo de andares?
#print(data[['id','floors']].sort_values('floors', ascending=False))
#print(data['floors'].unique())
#print(data[data['floors']==3.5].shape)

    ### C - Criar uma classificacao para os imoveis, separando baixo padrao e alto padrao.
data['level']='standard'
# print(data.columns)
# print(data.dtypes)
data.loc[data['price']>540000,'level']='high-level'
data.loc[data['price']<540000,'level']='low-level'
#print(data[['id','price','level']].head())

    ### D - Relatorio ordenado pelo preço
# report=data[['id','price','date','bedrooms','sqft_lot','level']].sort_values('price',ascending=False)
# #print(report)
# report.to_csv('datasets/report_aula02.csv',index=False)

    ### E - Mapa indicando onde as casas estao localizadas

#import plotly.express as px
# data_mapa=data[['id','lat','long','price']]
# mapa = px.scatter_mapbox(data_mapa,lat='lat',lon='long',hover_name= 'id',hover_data=['price'],color_discrete_sequence=['fuchsia'],zoom=3,height=300)
# mapa.update_layout(mapbox_style='open-street-map')
# mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()

# 1. 1. Crie um anova coluna chamada: "house_age"
# - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house'
# - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house'
#data['date'] = pd.to_datetime(data['date'],format='%Y/%m/%d',errors='coerce')
data['house_age'] = 'age'
data.loc[data['date'] > pd.to_datetime('2014-01-01',format='%Y/%m/%d',errors='coerce'), 'house_age'] = 'new_house'
data.loc[data['date'] < pd.to_datetime('2014-01-01',format='%Y/%m/%d',errors='coerce'), 'house_age'] = 'old_house'
#print(data.dtypes)
#print(data[['date', 'house_age']].head(15))

# 2. Crie uma nova coluna chamada: "dormitory_type"
# - Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
# - Se o valor da coluna "bedrooms" for igual à 2 => 'apartament'
# - Se o valor da coluna "bedrooms" for maior que 2 => 'house'
data['dormitory_type'] = 'null'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] ==2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] >2, 'dormitory_type'] = 'house'
#print(data[['house_age','date', 'bedrooms','dormitory_type']].head(10))

# 3. Crie uma nova coluna chamada: "condition_type"
# - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
# - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
# - Se o valor da coluna "condition" for igual à 5 => 'good'
data['condition_type'] = 'null'
data.loc[data['condition'] <=2, 'condition_type'] = 'bad'
data.loc[(data['condition'] ==3) | (data['condition']==4), 'condition_type'] = 'regular'
data.loc[data['condition'] ==5, 'condition_type'] = 'good'
#print(data[['condition','condition_type']].head(20))

# # 4. Modifique o TIPO da coluna "condition" para STRING
data['condition']=data['condition'].astype(str)
#print(data.dtypes)
# # 5. Delete as colunas "sqft_living15" e "sqft_lot15"
data=data.drop('sqft_living15', axis=1)
data=data.drop('sqft_lot15', axis=1)
#print(data.columns)

# # 6. Modifique o TIPO da coluna "yr_build" para DATE
data['yr_built']=pd.to_datetime(data['yr_built'],format='%Y',errors='coerce')
## # 7. Modifique o TIPO da coluna "yr_renovated" para DATE
data['yr_renovated']=pd.to_datetime(data['yr_renovated'],format='%Y',errors='coerce')
print(data.dtypes)
#
# # 8. Qual a data mais antiga de construção de um imóvel?
# # R: 1900
print(data[['id','yr_built']].min())
#
# # 9. Qual a data mais antiga de renovação de um imóvel?
# # R: 1934
print(data[['id','yr_renovated']].min())

# # 10. Quantos imóveis tem 2 andares?
# # R: 8241
print(data[data['floors']==2].shape)
#
# # 11. Quantos imóveis estão com a condição igual a “regular” ?
# # R: 19.710 imóveis com condição regular.
print(data[data['condition_type']=='regular'].shape)
#
# # 12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?
# # R: 2 imóveis "bad" com "vista para água"
print(data[(data['condition_type']=='bad') & (data['waterfront']==1)].shape)

# # 13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?
# # R: 1701
print(data[(data['condition_type']=='good') & (data['house_age']=='new_house')].shape)

# # 14. Qual o valor do imóvel mais caro do tipo “studio” ?
# # R: 1.247.000,00
print(data[['dormitory_type','price']].loc[data['dormitory_type']=='studio'].sort_values('price',ascending=False))
#
# # 15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?
# # R: 0 imóveis
print(data[(data['dormitory_type']=='apartment') & (data['yr_renovated']=='2015')].shape)
# # 16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?
# # R: 33 quartos
print(data[['dormitory_type','bedrooms']].loc[data['dormitory_type']=='house'].sort_values('bedrooms', ascending=False))
# # 17. Quantos imóveis “new_house” foram reformados no ano de 2014?
# R: 91 imóveis
print(data[(data['house_age']=='new_house') & (data['yr_renovated']=='2014')].shape)

# 18. Selecione as colunas 'id', 'date', 'price', 'floor,zipcode':
#direto pelos nomes das colunas?
#pelos indices
#pelos indices das linhas e os nomes das colunas
#indices booleanos
print (data[['id', 'date', 'price', 'floors','zipcode']])
print (data.iloc[:,[0,1,2,7,16]])
print (data.loc[:,['id', 'date', 'price', 'floors','zipcode']])
print (data.loc[:,['id', 'date', 'price', 'floors','zipcode']])
print(data.columns)
coluna=[True,True,True,False,False,False,False,
        True,False,False,False,False,False,False,False,
        False,True,False,False,False,False,False,False,]
print(data.loc[:,coluna])
# 19. Salve um arquivo .csv somente com as colunas do item 10 ate o 17
report=data[['id', 'date', 'price', 'floors','zipcode','dormitory_type','condition_type','yr_renovated', 'yr_built']].sort_values('price',ascending=False)
print(report)
report.to_csv('datasets/report_aula02.csv',index=False)

# 20. Modifique a cor dos pontos domapa para verde-escuro
import plotly.express as px
data_mapa=data[['id','lat','long','price']]
mapa = px.scatter_mapbox(data_mapa,lat='lat',lon='long',hover_name= 'id',hover_data=['price'],color_discrete_sequence=['darkgreen'],zoom=10,height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
#mapa.show()

print(data[["bathrooms","price"]].groupby("bathrooms").mean())
import this
0
