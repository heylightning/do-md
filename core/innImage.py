import base64

def extract_base64_image_from_docx(doc):
    image_parts = []
    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_parts.append(doc.part.rels[rel].target_part)
    
    base64_imagesArr = []
    for image_part in image_parts:
        image_stream = image_part.blob
        base64_image = base64.b64encode(image_stream).decode()
        base64_imagesArr.append(base64.b64decode(base64_image))
    
    return base64_imagesArr

def create_image_files(line, base64_imagesArr):
    for bytes in base64_imagesArr:
        with open(f"TBZped/image-{line}.png", "wb") as f:
            f.write(bytes)
        print(f"image-{line}.png successfully created.\n")
