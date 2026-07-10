import streamlit as st
import pandas as pd

st.title("Machine Learning Based Buyer Segmentation")

clients = pd.read_csv("clients.csv")
properties = pd.read_csv("properties.csv")

st.header("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Clients", len(clients))

with col2:
    st.metric("Total Properties", len(properties))

st.header("Client Type Distribution")
st.bar_chart(clients["client_type"].value_counts())

st.header("Gender Distribution")
st.bar_chart(clients["gender"].value_counts())

st.header("Buyer Distribution by Region")
st.bar_chart(clients["region"].value_counts())

st.header("Acquisition Purpose")
st.bar_chart(clients["acquisition_purpose"].value_counts())

st.header("Sample Data")
st.dataframe(clients.head(20))
