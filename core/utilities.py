from docx import Document
import streamlit as st
from core.pre_utilities import *
from core.innImage import extract_base64_image_from_docx, create_image_files
from core.marking import tableMarker, imageMarker


def config(document):
    block_xmlArr = []
    for block in document.element.body:
        block_xmlArr.append(block.xml)

    Markdown = ""

    for iteration in range(1, len(block_xmlArr) + 1):
        if titleExtractor(block_xmlArr[iteration - 1]) != None:
            Markdown = Markdown + "\n" + "# " + \
                titleExtractor(block_xmlArr[iteration - 1])

        elif subtitleExtractor(block_xmlArr[iteration - 1]) != None:
            Markdown = Markdown + "\n" + "### " + \
                subtitleExtractor(block_xmlArr[iteration - 1])

        elif headExtractor(block_xmlArr[iteration - 1]) != None:
            Markdown = Markdown + "\n" + "## " + \
                headExtractor(block_xmlArr[iteration - 1])

        elif listExtractor(block_xmlArr[iteration - 1]) != None:
            Markdown = Markdown + "\n" + "* " + \
                listExtractor(block_xmlArr[iteration - 1])

        elif tableExtractor(block_xmlArr[iteration - 1]) != None:
            Arr, Col = tableExtractor(block_xmlArr[iteration - 1])
            Markdown = Markdown + "\n\n" + tableMarker(Arr, Col)

        elif paraNimageExtractor(block_xmlArr[iteration - 1]) != None:
            if paraNimageExtractor(block_xmlArr[iteration - 1]) == "Image.":
                create_image_files(
                    iteration, extract_base64_image_from_docx(document))
                if (imageMarker(iteration) == True):
                    Markdown = Markdown + "\n\n" + \
                        f"![Image](image-{iteration}.png)" + "\n"

            else:
                if (paraNimageExtractor(block_xmlArr[iteration - 1]) == 'white-line.'):
                    Markdown = Markdown + "\n"
                elif (paraNimageExtractor(block_xmlArr[iteration - 1]) == 'section-break.'):
                    pass
                else:
                    Markdown = Markdown + "\n" + \
                        paraNimageExtractor(block_xmlArr[iteration - 1])

    return Markdown


def renderer():
    try:
        uploaded_file = st.file_uploader("Choose a .docx file")
        if uploaded_file is not None:
            document = Document(uploaded_file)
            return config(document)
    except Exception as Error:
        print(Error)
