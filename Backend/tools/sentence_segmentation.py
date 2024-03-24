import spacy


def split_into_sentences(paragraph):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(paragraph)

    sentences = [sent.text for sent in doc.sents]

    return {'data': {'sentences': sentences}}
