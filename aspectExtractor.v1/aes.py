import aesMethods

def printResultChoice(str):

    if(str=='Y'):
        return True
    else:
        return False



FolderName='C:\\Users\\Saurav Karmakar\\Downloads\\AspectExtraction\\dataset\\rData\\'

#_InputDataFile= '0.ReviewDataset.txt'
#_InputDataFile= 'r10Dataset.txt'
InputDataFile= 'rB073RR8T1K.txt'

ReviewDataset=FolderName+InputDataFile

Review10Dataset=FolderName+'r10Dataset.txt'

PreProcessedData=FolderName+'1.PreProcessedData.txt'

TokenizedReviews=FolderName+'2.TokenizedReviews.txt'

PosTaggedReviews=FolderName+'3.PosTaggedReviews.txt'

ExtractedAspects=FolderName+'4.Aspects.txt'

_Opinions=FolderName+'5.Opinions.txt'

choiceY = 'Y'
choiceN = 'N'

print("\nAspect Extraction System  begins to execute !")

print("-------------------------------------------------------------")

print("\n\nData Preprocessing Stage is in execution !\n..........................................")

aesMethods.preProcessing(ReviewDataset,PreProcessedData,printResultChoice(choiceN))

print("\n\nReading Review Data !\n.....................")
aesMethods.tokenizeReviews(ReviewDataset,TokenizedReviews,printResultChoice(choiceY))

print("\n\nPOS Tagging is in execution !\n.............................")

aesMethods.posTagging(TokenizedReviews,PosTaggedReviews,printResultChoice(choiceN))

print("\n\nThis function will list all the considerable nouns as aspect\n............................................................\n")
aesMethods.aspectExtraction(PosTaggedReviews,ExtractedAspects,printResultChoice(choiceY))

#print("\n\n\n\n\n\nASPECT WORDS...")

