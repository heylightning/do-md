import zipfile
import os

def create_zip_from_folder(folder_path, zip_filename):
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found.")
        return
    
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a folder.")
        return
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                zipf.write(os.path.join(root, file), arcname=relative_path)
                
    print(f"Zip file {zip_filename} created.")
