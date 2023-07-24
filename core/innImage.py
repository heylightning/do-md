# prototype/nextMove.txt

import base64
from docx import Document

def extract_base64_image_from_docx(docx_file):
    doc = Document(docx_file)
    
    image_parts = []
    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_parts.append(doc.part.rels[rel].target_part)
    
    base64_images = []
    for image_part in image_parts:
        image_stream = image_part.blob
        base64_image = base64.b64encode(image_stream).decode()
        base64_images.append(base64_image)
    
    return base64_images

docx_file = "..test.docx" 
base64_images_data = extract_base64_image_from_docx(docx_file)
print(len(base64_images_data))

base64_encoded_image = base64.b64decode(base64_images_data[0])

with open("text.png", "wb") as f:
    f.write(base64_encoded_image)
