from docx import Document
import streamlit as st
from core.pre_utilities import *
from core.innImage import extract_base64_image_from_docx, create_image_files
from core.marking import tableMarker, imageMarker

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
            Arr, Col = tableExtractor(block_xmlArr[iteration - 1])
            print(f"\n{tableMarker(Arr, Col)}\n") # Only for Data Visualization.
            lineDict[f"Line {iteration}"] = tableMarker(Arr, Col)
        elif paraNimageExtractor(block_xmlArr[iteration - 1]) != None:
            if paraNimageExtractor(block_xmlArr[iteration - 1]) == "Image.":
                create_image_files(iteration, extract_base64_image_from_docx(document))
                if (imageMarker(iteration) == True):
                    lineDict[f"Line {iteration}"] = f"![Image](image-{iteration}.png)"
            else:
                lineDict[f"Line {iteration}"] = paraNimageExtractor(block_xmlArr[iteration - 1])
    
    markdown = ""
    for content in lineDict:
        markdown = markdown + str(f"{content} : {lineDict[content]} \n\n")

    return markdown

def renderer():
    uploaded_file = st.file_uploader("Choose a .docx file")
    if uploaded_file is not None:
        document = Document(uploaded_file)
        return config(document)
    