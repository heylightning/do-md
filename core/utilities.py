from docx import Document
import streamlit as st
from core.pre_utilities import *

def config(document):
    block_xmlArr = []
    lineDict = {}
    for block in document.element.body:
        block_xmlArr.append(block.xml)

    for iteration in range(1, len(block_xmlArr) + 1):
        if titleExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = titleExtractor(block_xmlArr[iteration - 1])
        elif subtitleExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = subtitleExtractor(block_xmlArr[iteration - 1])
        elif headExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = headExtractor(block_xmlArr[iteration - 1])
        elif listExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = listExtractor(block_xmlArr[iteration - 1])
        elif tableExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = tableExtractor(block_xmlArr[iteration - 1])
        elif paraNimageExtractor(block_xmlArr[iteration - 1]) != None:
            lineDict[f"Line {iteration}"] = paraNimageExtractor(block_xmlArr[iteration - 1])
    
    temp = ""
    for content in lineDict:
        temp = temp + str(f"{content} : {lineDict[content]} \n\n")

    return temp

def renderer():
    uploaded_file = st.file_uploader("Choose a .docx file")
    if uploaded_file is not None:
        document = Document(uploaded_file)
        return config(document)
    