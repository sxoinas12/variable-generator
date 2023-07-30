import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_trf")


def test_something(text):
    doc = nlp(text)

    displacy.serve(doc, style="dep", port=5001)


test_something('allow chat communication for authenticated users')
#test_something('Stick element after scroll has passed the element')