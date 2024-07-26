import streamlit as st
from components.sidebar import app_sidebar
from core.translators import translate_text

from utils.consts import APP_CONSTANTS

st.set_page_config(page_title="Smart Translator", page_icon="🌍")
app_sidebar.render()

st.title("Smart Translator")
st.write("Công cụ này giúp bạn tự động dịch văn bản sang ngôn ngữ đích. Có kèm theo chú thích từ khóa hoặc từ chuyên ngành.")

textbox = st.text_area("Enter a text: ", height=250, label_visibility="hidden")
selected_language = st.selectbox("Select language to translate to: ", APP_CONSTANTS.languages, index=1)
if st.button("Translate", type="primary"):
    selected_model = app_sidebar.get_selected_model()
    selected_annotation_language = app_sidebar.get_selected_annotation_language()

    stream_translated = translate_text(selected_model, textbox, selected_language, selected_annotation_language, stream=True)
    st.write_stream(stream_translated)