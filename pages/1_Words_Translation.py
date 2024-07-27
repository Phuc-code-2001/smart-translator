import streamlit as st
from components.sidebar import app_sidebar
from core.translators import translate_words

from utils.consts import APP_CONSTANTS

app_sidebar.render()

st.title("Words Translation")
st.write("""
    Công cụ này sẽ giúp bạn dịch các từ hoặc cụm từ. 
    Ngoài ra nó cũng cho biết về các tình huống sử dụng và ví dụ.
    Có thể phân tích các gốc từ và nguồn gốc và các từ liên quan.
""")

text = st.text_area("Nhập từ: ", height=200)
language = st.selectbox("Chọn ngôn ngữ đích: ", APP_CONSTANTS.languages, index=1)

if st.button("Dịch", type="primary"):
    selected_model = app_sidebar.get_selected_model()
    selected_annotation_language = app_sidebar.get_selected_annotation_language()

    stream_translated = translate_words(selected_model, text, language, selected_annotation_language, stream=True)
    st.write_stream(stream_translated)