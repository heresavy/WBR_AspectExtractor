import re
import nounExtractor

import warnings
# Importing Gensim
import gensim
from gensim import corpora


from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

def file_read(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line)
        #print(content_array)
        #print(len(content_array))
        return(content_array)

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

FolderName='C:\\Users\\Saurav Karmakar\\Downloads\\AspectExtraction\\dataset\\tData\\'
InputFile = 'r10Dataset.txt'

ReviewDataset=FolderName+InputFile

doc_r10Reviewdata=file_read(ReviewDataset)

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

doc_clean = [clean(doc).split() for doc in doc_r10Reviewdata]
#print (doc_clean)

# Creating the term dictionary of our courpus, where every unique term is assigned an index.

dictionary = corpora.Dictionary(doc_clean)
#s='dictionary.id2token'
#Print(s)
#print(dictionary.id2token)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]


# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.

num_topics1 = 70
num_words1 = 10

num_topics2 = 10
num_words2 = 30
ldamodel = Lda(doc_term_matrix, num_topics=num_topics2, id2word = dictionary, passes=50)


#ldamodel1= Lda(doc_term_matrix, num_topics=num_topics2, alpha =0.1, eta=0.01 ,id2word = dictionary, passes=100)

#print(ldamodel.print_topics(num_topics=10, num_words=10))
#print(ldamodel.get_topics())

#topic1=ldamodel.print_topic(1,1)
#str1=re.findall(r"^\w+",topic1)
#print(str1)


x=ldamodel.show_topics(num_topics=num_topics1, num_words=num_words1,formatted=False)
topics_words = [(tp[0], [wd[0] for wd in tp[1]]) for tp in x]

#Prunting Topics and Words
#for topic,words in topics_words:
#    print(str(topic)+ "::"+ str(words))
#print()
words_stack_list =[]
words_stack = " "
separator =" "

for topic,words in topics_words:
    words_stack_list.extend(words)
    words_stack +=  ' '.join(words)
    #printing topic words as strings
    #print(words)

print()

#print(words_stack_list)
#print()

#printing the topic words accumalted
print("Printing the topic words accumalted")
print("-----------------------------------")
print(words_stack)
print()

#printing the noun topic words in accumalted manner
print("Printing the noun topic words in accumalted manner")
print("-----------------------------------")
print( nounExtractor.nExtractor(words_stack))






