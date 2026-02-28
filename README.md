** Pip & Version Check **

Open Command Prompt (CMD) and check:

Check Python version
python --version

If it work properly, proceed to installation.

** Required Installations **

2.1 Install Required Python Libraries
  pip install spacy
  pip install python-docx
2.2 Download NLP Model
  python -m spacy download en_core_web_sm
** Install Graphviz **

Go to: https://graphviz.org/download/

Download the EXE installer according to your system (Windows).

Run the installer:

Click OK → OK → OK (default settings).

** Configure Graphviz (Important) **

After installing Graphviz:

Go to C Drive

Open Program Files

Open Graphviz

Open bin folder

Copy the full path of the bin folder

Now:

Click Windows button

Search: Environment Variables

Click: Edit the system environment variables

Click: Environment Variables

Under User Variables, select Path

Click Edit

Click New

Paste the copied Graphviz bin path

Click OK → OK → OK

Restart your system

** Creating the Main Project **

Create a folder named:
UML_generator using AI
Inside that folder create:
uml_generator.py
OR
uml_generator.ipynb
(Use whichever you prefer.)
Paste the project code inside the file.

** Install PlantUML **

Go to: https://plantuml.com/download
Click Download
Download the .jar file.
Place the .jar file inside the project folder:

UML_generator using AI
** Create Sample SRS File **
Create a file named:
sample_srs.txt
Inside it, write your system description.

Example:

Customers purchase Products.
Admins monitor Orders.
Order contains Products.
Customer makes Payment.
** Run the Project **

If using Python file:

py -3.11 uml_generator.py

Then generate diagram:

java -jar plantuml.jar diagram.puml

If using Jupyter Notebook:

Run all cells after cell 6

Output files will be generated

** Output File **

After execution, you will get:

diagram.puml
diagram.png

Common Problems & Solutions
Problem: Graphviz not recognized

Solution:

Ensure Graphviz bin folder path is added to Environment Variables

Restart the system after adding the path

Problem: spaCy model not found

Run:

python -m spacy download en_core_web_sm
*** Final Output ***

The system automatically extracts:

Classes
Relationships
Verb labels
UML Diagram
And generates a visual class diagram from SRS text.

