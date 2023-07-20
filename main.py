from docx import Document

def read_docx(path):
    doc = Document(path)
    content = []
    for paragraph in doc.paragraphs:
        # return identify_heading(paragraph)
        print(paragraph.style)
    return "\n".join(content)

def identify_heading(paragraph):
    heading_styles = ["Heading 1", "Heading 2", "Heading 3", "Heading 4", "Heading 5", "Heading 6"]

    for style in heading_styles:
        if paragraph.style.name.startswith(style):
            # return True
            return paragraph.style
    return False

def convert_to_markdown(docx_content):
    paragraphs = docx_content.split("\n")

    markdown_content = "\n\n".join(paragraphs)

    return markdown_content

def save_to_file(markdown_content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def main():
    content = read_docx("./static/test.docx")
    print(content)
if __name__ == "__main__": 
    main()