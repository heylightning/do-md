
def xmlConfig(element):
    noCol = 0
    noRow = 0
    Col = 0
    Row = 0
    temp = []
    fTableArr = []

    for num in element:
        if (num.tag).endswith('tblGrid'):
            for grandnum in num:
                if (grandnum.tag).endswith('gridCol'):
                    noCol = noCol + 1
        if (num.tag).endswith('tr'):
            for grandnum in num:
                if (grandnum.tag).endswith('tc'):
                    noRow = noRow + 1
    for child in element:
        if (num.tag).endswith('tblGrid'):
            for grandchild in child:
                if (grandchild.tag).endswith('gridCol'):
                    Col = Col + 1
        if (child.tag).endswith('tr'):
            for grandchild in child:
                if (grandchild.tag).endswith('tc'):
                    Row = Row + 1
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
                            fTableArr.append(" ".join(temp))
                if(Row == noRow):
                    break
                else:
                    temp = []
        if(Col == noCol):
            break
        else:
            temp = []


    return fTableArr, noCol
