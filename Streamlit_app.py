import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')
@st.cache(allow_output_mutation=True)

def get_data(path):
    data=pd.read_csv(path)
    return data

path='Datasets/kc_house_data.csv'
data=get_data(path)

#add new features
data['price_m2']=data['price']/data['sqft_lot']

#===============================
#Data Overview
#===============================

f_attributes=st.sidebar.multiselect('Enter columns',data.columns)
f_zipcode=st.sidebar.multiselect('Enter Zip Code',data['zipcode'].unique())

st.title('Data overview')

if (f_zipcode !=[])&(f_attributes !=[]):
    data=data.loc[data['zipcode'].isin(f_zipcode),f_attributes]
elif (f_zipcode ==[])&(f_attributes !=[]):
    data=data.loc[:,f_attributes]
elif (f_zipcode != []) & (f_attributes == []):
    data = data.loc[data['zipcode'].isin(f_zipcode), :]
else:
    data=data.copy()

#Average metrics
df1=data[['id','zipcode']].groupby('zipcode').count().reset_index()
df2=data[['price','zipcode']].groupby('zipcode').mean().reset_index()
df3=data[['sqft_living','zipcode']].groupby('zipcode').mean().reset_index()
df4=data[['price_m2','zipcode']].groupby('zipcode').mean().reset_index()

# merge
m1=pd.merge(df1,df2,on='zipcode',how='inner')
m2=pd.merge(m1,df3,on='zipcode',how='inner')
df=pd.merge(m2,df4,on='zipcode',how='inner')

df.columns=['ZIPCODE','TOTAL HOUSES','PRICE','SQRT LIVING','PRICE/M2']
st.dataframe(df,height=600)

#Statistic Descriptive
num_attributes = data.select_dtypes(include=['int64','float64'])
media = pd.DataFrame(num_attributes.apply(np.mean))
mediana = pd.DataFrame(num_attributes.apply(np.median))
std = pd.DataFrame(num_attributes.apply(np.std))

max_= pd.DataFrame(num_attributes.apply(np.max))
min_= pd.DataFrame(num_attributes.apply(np.min))

df1=pd.concat([max_,min_,media,mediana,std],axis=1).reset_index()
df1.columns=['attributes','max','min','mean','median','std']

st.dataframe(df1,height=600)

#




