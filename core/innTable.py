# prototype/main.py

import xml.etree.ElementTree as ET

xml_data = """
<w:tbl xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
  <w:tblPr>
    <w:tblStyle w:val="TableGrid"/>
    <w:tblW w:w="0" w:type="auto"/>
    <w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
  </w:tblPr>
  <w:tblGrid>
    <w:gridCol w:w="4508"/>
    <w:gridCol w:w="4508"/>
  </w:tblGrid>
  <w:tr w:rsidR="00A7205E" w14:paraId="6911B7E0" w14:textId="77777777" w:rsidTr="00A7205E">
    <w:tc>
      <w:tcPr>
        <w:tcW w:w="4508" w:type="dxa"/>
      </w:tcPr>
      <w:p w14:paraId="2AF0132A" w14:textId="375457E8" w:rsidR="00A7205E" w:rsidRDefault="00A7205E" w:rsidP="00A7205E">
        <w:pPr>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
        </w:pPr>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t xml:space="preserve">This is a table </w:t>
        </w:r>
        <w:proofErr w:type="gramStart"/>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t>which !contain</w:t>
        </w:r>
        <w:proofErr w:type="gramEnd"/>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t xml:space="preserve"> links. C1</w:t>
        </w:r>
      </w:p>
    </w:tc>
    <w:tc>
      <w:tcPr>
        <w:tcW w:w="4508" w:type="dxa"/>
      </w:tcPr>
      <w:p w14:paraId="571C05A7" w14:textId="2CAC3376" w:rsidR="00A7205E" w:rsidRDefault="00A7205E" w:rsidP="00A7205E">
        <w:pPr>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
        </w:pPr>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t xml:space="preserve">This is a table which contains links. C2 </w:t>
        </w:r>
        <w:hyperlink r:id="rId10" w:history="1">
          <w:r w:rsidRPr="00161380">
            <w:rPr>
              <w:rStyle w:val="Hyperlink"/>
              <w:lang w:val="en-US"/>
            </w:rPr>
            <w:t>https://www.table-col.com</w:t>
          </w:r>
        </w:hyperlink>
      </w:p>
    </w:tc>
  </w:tr>
  <w:tr w:rsidR="00A7205E" w14:paraId="34AFE460" w14:textId="77777777" w:rsidTr="00A7205E">
    <w:tc>
      <w:tcPr>
        <w:tcW w:w="4508" w:type="dxa"/>
      </w:tcPr>
      <w:p w14:paraId="67C7EEE7" w14:textId="42263074" w:rsidR="00A7205E" w:rsidRDefault="00A7205E" w:rsidP="00A7205E">
        <w:pPr>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
        </w:pPr>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t xml:space="preserve">C1R1 </w:t>
        </w:r>
        <w:hyperlink r:id="rId11" w:history="1">
          <w:r w:rsidRPr="00161380">
            <w:rPr>
              <w:rStyle w:val="Hyperlink"/>
              <w:lang w:val="en-US"/>
            </w:rPr>
            <w:t>https://www.table-row.com</w:t>
          </w:r>
        </w:hyperlink>
      </w:p>
    </w:tc>
    <w:tc>
      <w:tcPr>
        <w:tcW w:w="4508" w:type="dxa"/>
      </w:tcPr>
      <w:p w14:paraId="7C250EA6" w14:textId="686D3F67" w:rsidR="00A7205E" w:rsidRDefault="00A7205E" w:rsidP="00A7205E">
        <w:pPr>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
        </w:pPr>
        <w:proofErr w:type="gramStart"/>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t>!C</w:t>
        </w:r>
        <w:proofErr w:type="gramEnd"/>
        <w:r>
          <w:rPr>
            <w:lang w:val="en-US"/>
          </w:rPr>
          <w:t xml:space="preserve">2R1 </w:t>
        </w:r>
      </w:p>
    </w:tc>
  </w:tr>
</w:tbl>
"""

root = ET.fromstring(xml_data)

def xmlConfig(element):
    noCol = 0
    noRow = 0
    temp = []
    for child in element:
        if (child.tag).endswith('tr'):
            noCol = noCol + 1
            for grandchild in child:
                if (grandchild.tag).endswith('tc'):
                    noRow = noRow + 1
                    for greatgrandchild in grandchild:
                        if (greatgrandchild.tag).endswith('p'):
                            for greatgreatgrandchild in greatgrandchild:
                                if (greatgreatgrandchild.tag).endswith('r'):
                                    for finalchild in greatgreatgrandchild:
                                        if (finalchild.tag).endswith('t'):
                                            temp.append(finalchild.text.strip())
                                elif (greatgreatgrandchild.tag).endswith('hyperlink'):
                                    for finalchild in greatgreatgrandchild:
                                        if (finalchild.tag).endswith('r'):
                                            for finalgrandchild in finalchild:
                                                if (finalgrandchild.tag).endswith('t'):
                                                    temp.append(finalgrandchild.text.strip())
                if(noRow == 3):
                    break
                else:
                    temp = []
        if(noCol == 2):
            print(" ".join(temp))
            break
        else:
            temp = []
                            
    print(f"Number of Columns: {noCol}.\nNumber of Rows: {int(noRow/noCol)}.\nHence, total elements are: {noRow}\n")

xmlConfig(root)
