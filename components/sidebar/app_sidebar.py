import streamlit as st
from core.llms import list_model_name
from utils.consts import APP_CONSTANTS

global_vars = dict()

def render():
    sidebar = st.sidebar
    sidebar.title("Smart Translator")
    selected_model = sidebar.selectbox("Select a model:", list_model_name[::-1], index=0)
    global_vars.update({"selected_model": selected_model})

    selected_annotation_language = sidebar.selectbox("Select annotation language:", APP_CONSTANTS.languages, index=1)
    global_vars.update({"selected_annotation_language": selected_annotation_language})

def get_selected_model():
    return global_vars["selected_model"]

def get_selected_annotation_language():
    return global_vars["selected_annotation_language"]
