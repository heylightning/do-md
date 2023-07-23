from docx import Document
import streamlit as st
from core.pre_utilities import *

def config(document):
    return 'in progress'

def renderer():
    uploaded_file = st.file_uploader("Choose a .docx file")
    if uploaded_file is not None:
        document = Document(uploaded_file)
        return config(document)