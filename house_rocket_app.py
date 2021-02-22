import pandas as pd
import streamlit as st
import plotly.express as px

st.title('House Rocket Company')
st.markdown('Welcome to House Rocket Data Analysis')
st.header('Load data')


# read data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data

# load data
data = get_data('Datasets/kc_house_data.csv')
#st.dataframe(data.head(50))

#plot map
st.title('House Rocket Map')
is_check = st.checkbox('Display map')

# filter bedrooms
price_min= int(data['price'].min())
price_max= int(data['price'].max())
price_avg= int(data['price'].mean())

price_slider=st.slider('Price Range',
                       price_min,
                       price_max,
                       price_avg)
if is_check:
    # select rows
    houses= data[data['price']<price_slider][['id','lat','long','price']]
    st.dataframe(houses)
# draw map
    fig=px.scatter_mapbox(houses,
                      lat='lat',
                      lon='long',
                      size='price',
                      color_continuous_scale=px.colors.cyclical.IceFire,
                      size_max=15,
                      zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=300,margin={'r':0,'t':0,'l':0,'b':0})
    st.plotly_chart(fig)

bedrooms = st.sidebar.multiselect('Number of bedrooms', data['bedrooms'].unique())


