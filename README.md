# UML_generator-using-AI

## Pip and Version Check
1. Go to CMD  
   - Check Python version: `python --version`  

2. If everything is okay, install required libraries  
   - Install spaCy: `pip install spacy`  
   - Install python-docx: `pip install python-docx`  
   - Download NLP model: `python -m spacy download en_core_web_sm`

## Installation of Graphviz
1. Go to website: https://graphviz.org/download/  
2. Download the EXE installer as per your system  
3. Run installer → OK → OK → OK  

### Add Graphviz to Environment Variables
1. Go to `C Drive` → `Program Files` → `Graphviz` → `bin`  
2. Copy the full `bin` path  
3. Press Windows key → Search "Environment Variables"  
4. Click "Edit the system environment variables"  
5. Click "Environment Variables"  
6. Under User Variables → Select `Path` → Click Edit  
7. Click New → Paste copied path  
8. Click OK → OK → OK  
9. Restart the system  

## Creating the Main Project
1. Create a folder named: `UML_generator using AI`  
2. Inside that folder create file:  
   - `uml_generator.py`  
   OR  
   - `uml_generator.ipynb`  
3. Paste the project code inside the file  

## Install PlantUML
1. Go to: https://plantuml.com/download  
2. Download the `.jar` file  
3. Place the jar file inside the project folder  

## Create Sample SRS File
1. Create file named: `sample_srs.txt`  
2. Add system description. Example:


Customers purchase Products.
Admins monitor Orders.
Order contains Products.
Customer makes Payment.


## Run the Project
If using Python file:

py -3.11 uml_generator.py


Then generate UML:

java -jar plantuml.jar diagram.puml


If using Jupyter Notebook:
- Run all cells after cell 6  
- Output files will be generated automatically  

## Output Files
- `diagram.puml`  
- `diagram.png`  

## Common Problems
1. Graphviz not recognized  
   - Ensure Graphviz `bin` path is added to Environment Variables  
   - Restart system  

2. spaCy model not found  
   - Run: `python -m spacy download en_core_web_sm`

## Final Output
The system automatically extracts classes and relationships from SRS and generates a UML class dia
