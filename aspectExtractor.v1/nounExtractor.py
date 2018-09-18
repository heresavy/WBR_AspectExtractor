from textblob import TextBlob
txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
actions between computers and human (natural) languages."""



def  nExtractor(txt):
    blob = TextBlob(txt)
    return(blob.noun_phrases)

#print(nExtractor(txt))