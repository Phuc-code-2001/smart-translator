import streamlit as st
from components.sidebar import app_sidebar

app_sidebar.render()

st.title("Words Translation")
st.write("Công cụ này sẽ giúp bạn dịch các từ hoặc cụm từ. Ngoài ra nó cũng cho biết về các tình huống sử dụng và ví dụ.")