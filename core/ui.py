import streamlit as st
from core import utilities
from PIL import Image
from core.zipping import create_zip_from_folder


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
    st.sidebar.caption(
        "A simple app to help you write Markdown documents. Know more about this project [here](https://www.github.com/heylightning/do-md#readme).")
    st.sidebar.divider()
    st.sidebar.markdown('''
    ## `How to use?`
    1. Upload a .docx file.
    2. Preview the Markdown.
    3. Download the Markdown.
''')
    st.sidebar.markdown(
        "Made with ❤️ by [heylightning - Pratham](https://www.github.com/heylightning).")
    st.sidebar.caption("Note: This is a beta version.")


def heroSec():
    image = Image.open('static\icon.png')
    st.image(image, width=50)
    st.header('DoMD')
    st.caption('This is a simple app to help you write Markdown documents.')
    st.divider()
    content = utilities.renderer()
    if content is not None:
        previewMD(content)
        configMarkdown(content)


def previewMD(content):
    st.markdown('### Preview for your `markdown` file:')
    st.divider()
    st.markdown(content)


def configMarkdown(content):
    with open(f"TBZped/markdown.md", "w") as f:
        f.write(content)

    print("\nMarkdown file successfully created.\n")
    create_zip_from_folder("TBZped", "mdZip.zip")


def main():
    config()
