# Ipynb to Java Transpiler

## Getting Started

#### Download the [Latest Release](https://github.com/anuditnagar/javaTranspiler/releases "Latest Release")

Use `transpile` to convert any `.ipynb` file to Seperate `.java` Files

| Arguments     | Description                   | Usage                               |
|:-------------:|:-----------------------------:|:-----------------------------------:|
| -file         |Enter File Name                |`transpile -file test.ipynb`         |
| -pkg          |Enter Package Name             |`transpile -pkg pkgNameHere`         |
| -template     |Enter Template File Name       |`transpile -template template.class` |

Example `transpile -file test.ipynb -pkg tallo -template template.class`

## Running from Source

1. Run `git clone https://github.com/anuditnagar/javaTranspiler.git` to download the Source Code
2. Run `python transpile.py` to start converting.