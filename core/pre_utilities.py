from core.innText import textExtractor
from core.innTable import xmlConfig
import xml.etree.ElementTree as ET

def titleExtractor(block_xml):
    if(block_xml.find('w:pStyle w:val="Title"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a title. text={textExtractor(block_xml)}"
    return None

def subtitleExtractor(block_xml):
    if(block_xml.find('w:pStyle w:val="Subtitle"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a subtitle. text={textExtractor(block_xml)}"
    return None

def headExtractor(block_xml):
    if(block_xml.find('w:pStyle w:val="Heading1"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading1. text={textExtractor(block_xml)}"
    elif(block_xml.find('w:pStyle w:val="Heading2"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading2. text={textExtractor(block_xml)}"
    elif(block_xml.find('w:pStyle w:val="Heading3"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading3. text={textExtractor(block_xml)}"
    elif(block_xml.find('w:pStyle w:val="Heading4"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading4. text={textExtractor(block_xml)}"
    elif(block_xml.find('w:pStyle w:val="Heading5"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading5. text={textExtractor(block_xml)}"
    elif(block_xml.find('w:pStyle w:val="Heading6"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a heading6. text={textExtractor(block_xml)}"
    return None

def paraNimageExtractor(block_xml):
    if(block_xml.find('<w:pStyle ') == -1 and block_xml.find('<w:tblStyle ') == -1):
        if imageExtractor(block_xml) is not None:
            return imageExtractor(block_xml)
        else:
            if(block_xml.find('<w:t') != -1):
                return f'Is a paragraph. text={textExtractor(block_xml)}'
            else:
                if(block_xml.startswith('<w:sectPr ') == True):
                    return 'Is a section break.'
                else:
                    return 'Is a white line.'

def listExtractor(block_xml):
    if(block_xml.find('w:pStyle w:val="ListParagraph"') != -1):
        if(block_xml.find('<w:t') != -1):
            return f"Is a list. {textExtractor(block_xml)}"
    return None

def tableExtractor(block_xml):
    if(block_xml.find('<w:tblStyle w:val="TableGrid"/>') != -1):
        dataArr, noCol = xmlConfig(ET.fromstring(block_xml))
        return dataArr, noCol
    return None

def imageExtractor(block_xml):
    if(block_xml.find('<w:drawing>') != -1):
        return "Image."
    return None
