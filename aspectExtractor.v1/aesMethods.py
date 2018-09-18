import nltk

import ast

import re

from nltk.tokenize import word_tokenize

from nltk.corpus import wordnet

from nltk.corpus import sentiwordnet

def preProcessing(inputFileStr,outputFileStr,printResult):

    inputFile = open(inputFileStr,"r").read()

    outputFile=open (outputFileStr,"w+")

    cachedStopWords = nltk.corpus.stopwords.words("english")

    cachedStopWords.append('OMG')

    cachedStopWords.append(':-)')

    cachedStopWords.append(':-(')

    cachedStopWords.append(':-D')

    result=(' '.join([word for word in inputFile.split() if word not in cachedStopWords]))

    if(printResult):

        print('Following are the Stop Words')

        print(cachedStopWords)

        print(str(result))

    outputFile.write(str(result))

    outputFile.close()

def tokenizeReviews(inputFileStr, outputFileStr, printResult):

        tokenizedReviews = {}

        inputFile = open(inputFileStr, "r").read()

        outputFile = open(outputFileStr, "w")

        tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

        uniqueId = 1;

        cachedStopWords = nltk.corpus.stopwords.words("english")

        for sentence in tokenizer.tokenize(inputFile):
            tokenizedReviews[uniqueId] = sentence

            uniqueId += 1

        outputFile.write(str(tokenizedReviews))

        if (printResult):

            for key, value in tokenizedReviews.items():
                print(key, ' ', value)

        outputFile.close()

def posTagging(inputFileStr, outputFileStr, printResult):

        inputFile = open(inputFileStr, "r").read()

        outputFile = open(outputFileStr, "w")

        inputTupples = ast.literal_eval(inputFile)

        outputPost = {}

        for key, value in inputTupples.items():
            outputPost[key] = nltk.pos_tag(nltk.word_tokenize(value))

        if (printResult):

            for key, value in outputPost.items():
                print(key, ' ', value)

        outputFile.write(str(outputPost))

        outputFile.close()

def aspectExtraction(inputFileStr,outputFileStr,printResult):

    inputFile = open(inputFileStr,"r").read()

    outputFile=open (outputFileStr,"w")

    inputTupples=ast.literal_eval(inputFile)

    prevWord=''

    prevTag=''

    currWord=''

    aspectList=[]

    outputDict={}

    #Extracting Aspects

    for key,value in inputTupples.items():

        for word,tag in value:

            if(tag=='NN' or tag=='NNP'):

                if(prevTag=='NN' or prevTag=='NNP'):

                    currWord= prevWord + ' ' + word

                else:

                    aspectList.append(prevWord.upper())

                    currWord= word

                    #print(*aspectList)
                    #print('CWord '+currWord+' '+tag)

            prevWord=currWord

            prevTag=tag

    #Considering the aspects as nouns which has 2 or more occurences

    for aspect in aspectList:

            if(aspectList.count(aspect)>1):

                    if(outputDict.keys()!=aspect):

                            outputDict[aspect]=aspectList.count(aspect)

    outputAspect=sorted(outputDict.items(), key=lambda x: x[1],reverse = True)

    if(printResult):

        print(outputAspect)

    outputFile.write(str(outputAspect))
    #writeList2FileLinewise(outputAspect,'aspectOutput.txt')
    outputFile.close()

def writeList2FileLinewise(list,fileName):
    with open(fileName, 'w') as filehandle:
        for listitem in list:
            filehandle.write('%s\n' % listitem)

def aspectExtraction_N(inputFileStr,outputFileStr,printResult):

    inputFile = open(inputFileStr,"r").read()

    outputFile=open (outputFileStr,"w")

    inputTupples=ast.literal_eval(inputFile)

    prevWord=''

    prevTag=''

    currWord=''

    aspectList=[]

    outputDict={}

    #Extracting Aspects

    for key,value in inputTupples.items():

        for word,tag in value:

            if(tag=='NN' or tag=='NNP'):

                if(prevTag=='NN' or prevTag=='NNP'):

                    currWord= prevWord + ' ' + word

                else:

                    aspectList.append(prevWord.upper())

                    currWord= word

            prevWord=currWord

            prevTag=tag

    #Eliminating aspect which has 1 or less count

    for aspect in aspectList:

            if(aspectList.count(aspect)>1):

                    if(outputDict.keys()!=aspect):

                            outputDict[aspect]=aspectList.count(aspect)

    outputAspect=sorted(outputDict.items(), key=lambda x: x[1],reverse = True)

    if(printResult):

        print(outputAspect)

    outputFile.write(str(outputAspect))

    outputFile.close()