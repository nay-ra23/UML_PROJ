import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")


# ---------------- READ FILE ----------------
def read_srs(file_path):
    with open(file_path, "r") as file:
        return file.read()


# ---------------- EXTRACT CLASSES ----------------
def extract_classes(doc):
    classes = set()

    for token in doc:
        if token.pos_ in ("NOUN", "PROPN") and not token.is_stop:
            classes.add(token.lemma_.capitalize())  # remove plural issue

    return classes


# ---------------- EXTRACT RELATIONSHIPS ----------------
def extract_relationships(doc):
    relations = []

    for sent in doc.sents:
        subject = None
        object_ = None
        verb = None

        for token in sent:
            # subject
            if token.dep_ == "nsubj":
                subject = token.lemma_.capitalize()

            # object (handles more cases)
            if token.dep_ in ("dobj", "pobj", "attr"):
                object_ = token.lemma_.capitalize()

            # verb
            if token.pos_ == "VERB":
                verb = token.lemma_

        if subject and object_ and verb:
            relations.append((subject, verb, object_))

    return relations


# ---------------- GENERATE UML ----------------
def generate_plantuml(classes, relations):
    uml_code = "@startuml\n\n"

    # Add classes
    for cls in classes:
        uml_code += f"class {cls}\n"

    uml_code += "\n"

    # Add relationships
    for rel in relations:
        uml_code += f"{rel[0]} --> {rel[2]} : {rel[1]}\n"

    uml_code += "\n@enduml"

    return uml_code


# ---------------- SAVE FILE ----------------
def save_uml_file(uml_code):
    with open("diagram.puml", "w") as file:
        file.write(uml_code)


# ---------------- CONFIDENCE ----------------
def calculate_confidence(classes, relations):
    if len(classes) == 0:
        return 0
    return round(len(relations) / len(classes), 2)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    print("Reading SRS File...")
    text = read_srs("srs.txt")   # Make sure your file name is srs.txt

    doc = nlp(text)

    print("Extracting Classes...")
    classes = extract_classes(doc)
    print("Classes:", classes)

    print("Extracting Relationships...")
    relations = extract_relationships(doc)
    print("Relationships:", relations)

    print("Generating UML Code...")
    uml_code = generate_plantuml(classes, relations)

    save_uml_file(uml_code)

    confidence = calculate_confidence(classes, relations)
    print("Confidence Score:", confidence)

    print("PlantUML file 'diagram.puml' generated successfully!")