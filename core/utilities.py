from docx import Document
import streamlit as st

def config(document):
    return 'in progress'

def headExtractor():
    pass

def paraExtractor():
    pass

def listExtractor():
    pass

def tableExtractor():
    pass

def imageExtractor():
    pass

def linkExtractor():
    pass

def renderer():
    uploaded_file = st.file_uploader("Choose a  .docx file")
    if uploaded_file is not None:
        document = Document(uploaded_file)
        return config(document)