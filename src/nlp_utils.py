import spacy

def cargar_modelo():
    return spacy.load("es_core_news_sm")

def procesar_texto(nlp, texto):
    return nlp(texto)
