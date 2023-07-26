import os

def tableMarker(data_array, num_columns):
    table = []
    rows = [data_array[i:i+num_columns] for i in range(0, len(data_array), num_columns)]  
    
    headers = "| " + " | ".join(rows[0]) + " |"
    separator = "| " + " | ".join(["-" * len(header) for header in rows[0]]) + " |"
    
    table.append(headers)
    table.append(separator)
    
    for row in rows[1:]:
        row_data = "| " + " | ".join(row) + " |"
        table.append(row_data)
    
    return "\n".join(table)

def imageMarker(line):
    folderPath = 'TBZped'
    targetFile = f"image-{line}.png"

    for filename in os.listdir(folderPath):
        if(filename == targetFile):
            return True
    return 'something went wrong in imageMarker()'
