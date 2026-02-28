import spacy

nlp = spacy.load("en_core_web_sm")

file = open("srs.txt","r")
text = file.read()

doc = nlp(text)

classes = set()
relations = []

ignore_words = ["places","makes","includes","manages"]

for sent in doc.sents:
    nouns = []
    
    for token in sent:
        if token.pos_ in ("NOUN","PROPN"):
            word = token.text.lower()
            
            if word not in ignore_words:
                nouns.append(word.capitalize())
                classes.add(word.capitalize())
    
    if len(nouns) >= 2 and nouns[0] != nouns[-1]:
        relations.append((nouns[0],nouns[-1]))

uml = "@startuml\n"

for c in classes:
    uml += f"class {c}\n"

for r in relations:
    uml += f"{r[0]} --> {r[1]}\n"

uml += "@enduml"

file = open("diagram.puml","w")
file.write(uml)
file.close()