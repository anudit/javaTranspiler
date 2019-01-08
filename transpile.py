import json
import pprint
import sys

FOLDERNAME = "src"

def generateClassFiles(data):
    for cell in data['cells']:
        if(cell['cell_type'] == 'code'):
            code = ""
            className = cell['source'][0][2:-3]
            for line in cell['source']:
                code+=line

            print(className)

            try:
                with open("./"+ FOLDERNAME + "/" + className + ".java", "w") as file:  
                    file.write(code)
            except IOError:
                print("[File Error] Can't write to File. -1")


FILENAME = "Lab1.ipynb"

try:
    with open(FILENAME, "r") as file:  
        data = json.load(file)
        generateClassFiles(data)
        sys.exit(0)
except IOError:
    print("[File Error] Can't read to File. -1")
    sys.exit(0)