#Simple translation program with dictionaries

##English to French Dictionary
EngToFrench={'Yes':'Oui','No':'Non','white':'blanc','people':'peuple','woman':'la femme','girl':'la fille','children':'lenfant','boy':'le garcon','man':'lhomme','cat':'le chat','rich':'riche','red': 'rouge','she':'elle','bread': 'du pain', 'wine': 'du vin','eats': 'mange', 'drinks': 'bois','likes': 'aime', 1:'un','6.00':'6.00','he':'il','it':'il','car':'voiture','is':'est'}


#Function to translate word

def TranslateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word
def TranslateToFrench(sentence):
    Translation=''
    Word=''
    for c in sentence:
           if c !=' ':
                 Word =Word+c
           else:
                 Translation=Translation+' '+TranslateWord(Word,EngToFrench)
                 
                 Word=''
    return Translation+' '+TranslateWord(Word,EngToFrench)
sentence=raw_input("Enter a sentence: ")
print TranslateToFrench(sentence)
##Sample data
##print translate('John eats bread')
##print translate('Steve drinks wine')
##print translate('John likes 6.00')
##






