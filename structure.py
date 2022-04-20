from genericpath import exists
from pathlib import Path

def creating_folder_structure(file_name):

    structure = Path(file_name).open()

    for i in structure:

        folder_name = i[:i.find(">")]
        file_name = i[i.find(">")+1:].strip()
        
        current_path = Path(folder_name)

        if i.find(">") > 0:


            if not current_path.exists():

                current_path.mkdir()
            
            Path(folder_name + "/" + file_name).touch()
        
        current_path.touch()

    return ("Structure Created")


creating_folder_structure("structure.txt")
