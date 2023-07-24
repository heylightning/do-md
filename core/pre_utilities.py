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
        return "Is a table."
    return None

def imageExtractor(block_xml):
    if(block_xml.find('<w:drawing>') != -1):
        return "Is an image."
    return None

def textExtractor(block_xml):
    root = ET.fromstring(block_xml)
    text_values = [t.text for t in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')]

    final_values = [txt.strip() for txt in text_values]
    result_string = " ".join(final_values)
    if innerTxtExtractorStyleConfig(block_xml) is not None:
        innerTxtConfigData = innerTxtExtractorStyleConfig(block_xml)
        return lvl2Config(lvl1Config(result_string, innerTxtConfigData))
    return result_string

# TODO: Should be encountered second.

def tableDataConfig():
    pass

# TODO: Should be encountered third.

def imageBase64DataConfig():
    pass

def boldPartExtractor(block_xml):
    bold_text = ""
    root = ET.fromstring(block_xml)

    for r in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
        if any(bold_element is not None for bold_element in r.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}b')):
            text = r.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            if text is not None and text.text:
                bold_text += text.text
        
    return bold_text

def italicsPartExtractor(block_xml):
    italic_text = ""
    root = ET.fromstring(block_xml)

    for r in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
        if any(italic_element is not None for italic_element in r.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}i')):
            text = r.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            if text is not None and text.text:
                italic_text += text.text

    return italic_text

def innerTxtExtractorStyleConfig(block_xml):
    innerTxtDICT = {}
    if boldPartExtractor(block_xml) is not None:
        innerTxtDICT['bold'] = boldPartExtractor(block_xml)
    if italicsPartExtractor(block_xml) is not None:
        innerTxtDICT['italics'] = italicsPartExtractor(block_xml)

    if innerTxtDICT['bold'] != '' or innerTxtDICT['italics'] != '':
        return innerTxtDICT
    return None

def lvl1Config(result_string, innerTxt):
    innOBJArr = []
    if innerTxt['bold'] != '':
        startIndex = result_string.find(innerTxt['bold'])
        endIndex = startIndex + (len(innerTxt['bold']) - 1)
        boldOBJ = {}
        boldOBJ['startIndex'] = startIndex
        boldOBJ['endIndex'] = endIndex
        boldOBJ['data'] = result_string
        boldOBJ['tag'] = 'bold'
        innOBJArr.append(boldOBJ)
    if innerTxt['italics'] != '':
        startIndex = result_string.find(innerTxt['italics'])
        endIndex = startIndex + (len(innerTxt['italics']) - 1)
        italicOBJ = {}
        italicOBJ['startIndex'] = startIndex
        italicOBJ['endIndex'] = endIndex
        italicOBJ['data'] = result_string
        italicOBJ['tag'] = 'italic'
        innOBJArr.append(italicOBJ)

    return innOBJArr

def lvl2Config(innOBJArr):
    if len(innOBJArr) == 1:
        tagContainer = innOBJArr[0]['tag']

        if(tagContainer == 'bold'):
            return subLvl2Config(innOBJArr[0]['startIndex'], innOBJArr[0]['endIndex'], innOBJArr[0]['data'], 'bold')
        return subLvl2Config(innOBJArr[0]['startIndex'], innOBJArr[0]['endIndex'], innOBJArr[0]['data'], 'italics')

    elif len(innOBJArr) == 2:
        startIndexContainer0 = innOBJArr[0]['startIndex']
        endIndexContainer0 = innOBJArr[0]['endIndex']
        dataContainer0 = innOBJArr[0]['data']
        
        startIndexContainer1 = innOBJArr[1]['startIndex']
        endIndexContainer1 = innOBJArr[1]['endIndex']
        dataContainer1 = innOBJArr[1]['data']
        
        if(startIndexContainer0 == -1 or startIndexContainer1 == -1):
            if(startIndexContainer0 == -1):
                return subLvl2Config(startIndexContainer1, endIndexContainer1,  dataContainer1, 'italics')
            elif(startIndexContainer1 == -1):
                return subLvl2Config(startIndexContainer0, endIndexContainer0, dataContainer0, 'bold')
        elif(startIndexContainer0 == startIndexContainer1):
            if(endIndexContainer0 > endIndexContainer1):
                return subLvl2Config(startIndexContainer0, endIndexContainer0 + (2), subLvl2Config(innOBJArr[1]['startIndex'], innOBJArr[1]['endIndex'], dataContainer0, 'italics'), 'bold')
            return subLvl2Config(startIndexContainer1, endIndexContainer1 + (4), subLvl2Config(startIndexContainer0, endIndexContainer0, dataContainer1, 'bold'), 'italics')
        else:
            return 'something went wrong with lvl2Config 2nd elif'
        
    else:
        return 'something went wrong with lvl2Config else'

def subLvl2Config(start, end, text, tag):
    if(tag == 'bold'):
        output_line = text[:start] + "**" + text[start:end+1] + "**" + text[end+1:]
        return output_line
    else:
        output_line = text[:start] + "*" + text[start:end+1] + "*" + text[end+1:]
        return output_line
