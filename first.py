import streamlit as st
st.title('priyank patel')
st.title('ATS Branch')
import pandas as pb
dataset=pb.read_excel("Bill Register.xlsx")
st.dataframe(dataset)