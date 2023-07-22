import streamlit as st
from core import utilities
from PIL import Image

def config():
    st.set_page_config(
        page_title="DoMD - A simple app to help you write Markdown documents.",
        page_icon="static\icon.png",
        layout="centered",
        menu_items={
            'Report a bug': "https://www.github.com/heylightning/do-md/issues/new",
        }
    )
    
    sidebarConfig()
    heroSec()

def sidebarConfig():
    st.sidebar.title("DoMD")
    st.sidebar.caption("A simple app to help you write Markdown documents. Know more about this project [here](https://www.github.com/heylightning/do-md#readme).")
    st.sidebar.divider()
    st.sidebar.markdown('''
    ## `How to use?`
    1. Upload a .docx file.
    2. Preview the Markdown.
    3. Download the Markdown.
''')
    st.sidebar.markdown("Made with ❤️ by [heylightning - Pratham](https://www.github.com/heylightning).")
    st.sidebar.caption("Note: This is a beta version.")

def heroSec():
    image = Image.open('static\icon.png')
    st.image(image, width=50)
    st.header('DoMD')
    st.caption('This is a simple app to help you write Markdown documents.')
    st.divider() 
    uploadDocs()

def previewMD():
    st.markdown('### Preview for your `markdown` file:')
    st.divider()
    st.download_button(label="Download Markdown", data=downloadMD(), file_name="preview.md", mime="text/markdown")
    st.markdown(downloadMD())

def downloadMD():
    return '## This is a sample markdown file.'

def uploadDocs():
    uploaded_file = st.file_uploader("Choose a  .docx file")
    if uploaded_file is not None:
        previewMD()

def main():
    config()