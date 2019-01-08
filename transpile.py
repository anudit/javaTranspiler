import json
import pprint
import sys
import os
import argparse

def returnWithTemplateCode(code, className):
    processed = ""
    try:
        with open("template.class", "r") as file:  
            template = str(file.read())
            template = template.replace("/*<!--code-->*/",code)
            template = template.replace("/*<!--pkgName-->*/",PKGNAME)
            template = template.replace("/*<!--className-->*/",className)
            processed = template
    except IOError:
        print("[File Error] Can't read to File.3")
    return processed

def generateClassFiles(data):
    for cell in data['cells']:
        if(cell['cell_type'] == 'code'):
            code = ""
            className = cell['source'][0][2:-3]
            end = len(cell['source'])
            for i in range(1,end):
                if(i == 1):
                    code += cell['source'][i]
                else:
                    code += "\t\t" + cell['source'][i]
            className = className.replace(" ", "")
            print("Processing Class : ", className)

            try:
                with open("./"+ FOLDERNAME + "/" + className + ".java", "w") as file:  
                    file.write(returnWithTemplateCode(code, className))
            except IOError:
                print("[File Error] Can't write to File.2")

FILENAME = ""
FOLDERNAME = "src"
PKGNAME = ""
TEMPLATE = ""

parser = argparse.ArgumentParser()
parser.add_argument('-file',type=str, help="Specify File Name")
parser.add_argument('-pkg',type=str, help="Specify Package Name")
parser.add_argument('-template',type=str, help="Specify Template Address")
args = parser.parse_args()

if( type(args.file) != str ):
    print("Specify File Name")
    sys.exit(0)
else:
    FILENAME = args.file

if( type(args.pkg) != str ):
    print("Specify File Name")
    sys.exit(0)
else:   
    PKGNAME = args.pkg


if(os.path.exists(FOLDERNAME) != True):
    os.mkdir(FOLDERNAME)

try:
    with open(FILENAME, "r") as file:  
        data = json.load(file)
        generateClassFiles(data)
        sys.exit(0)
except IOError:
    print("[File Error] Can't read File.1")
    sys.exit(0)