import spacy

nlp = spacy.load("en_core_web_sm")

def split_into_sentences(paragraph):
    doc = nlp(paragraph)

    sentences = [sent.text for sent in doc.sents]

    return sentences
