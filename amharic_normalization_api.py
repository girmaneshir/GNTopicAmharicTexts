# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:16:41 2018

@author: hilena
"""
punctuation_0="@#%^*,./\)(።፤!#%-\"'፡»"
# input: a string that may contain multiple words.
# output: a list of strings, preprocessed
import re
def normalize(string):
        #"""Preprocessing punctuation marks
        string=string.replace("ሠ","ሰ")
        string=string.replace("ሃ", "ሀ")
        string=string.replace("ሐ", "ሀ")
        string=string.replace("ሓ", "ሀ")
        string=string.replace("ኅ", "ሀ")
        string=string.replace("ኃ", "ሀ")
        string=string.replace("ኋ", "ኋ")
        string=string.replace("ሗ", "ኋ")
        string=string.replace("ኁ", "ሁ")
        string=string.replace("ኅ", "ህ")
        string=string.replace("ኂ", "ሂ")
        string=string.replace("ኄ", "ሄ")
        string=string.replace("ኆ", "ሆ")
        string=string.replace("ሑ", "ሁ")
        string=string.replace("ሒ", "ሂ")
        string=string.replace("ሔ", "ሄ")
        string=string.replace("ሕ", "ህ")
        string=string.replace("ሡ", "ሱ")
        string=string.replace("ሖ", "ሆ")
        string=string.replace("ሢ", "ሲ")
        string=string.replace("ሣ", "ሳ")
        string=string.replace("ሤ", "ሴ")
        string=string.replace("ሥ", "ስ")
        string=string.replace("ሦ", "ሶ")
        string=string.replace("ሼ", "ሸ")
        string=string.replace("ቼ", "ቸ")
        string=string.replace("ዬ", "የ")
        string=string.replace("ዲ", "ድ")
        string=string.replace("ጄ", "ጀ")
        string=string.replace("ጸ", "ፀ")
        string=string.replace("ጹ", "ፁ")                    
        string=string.replace("ጺ", "ፂ")
        string=string.replace("ጻ", "ፃ")
        string=string.replace("ጼ", "ፄ")
        string=string.replace("ጽ", "ፅ")
        string=string.replace("ጾ", "ፆ")
        string=string.replace("ዉ", "ው")
        string=string.replace("ዴ", "ደ")
        string=string.replace("ቺ", "ች")
        string=string.replace("ዪ", "ይ")
        string=string.replace("ጪ", "ጭ")
        string=string.replace("ዓ", "አ")
        string=string.replace("ዑ", "ኡ")
        string=string.replace("ዒ", "ኢ")
        string=string.replace("ዐ", "አ")
        string=string.replace("ኣ", "አ")
        string=string.replace("ዔ", "ኤ")
        string=string.replace("ዕ", "እ")
        string=string.replace("ዖ", "ኦ")
        string=string.replace("ኚ", "ኝ")
        string=string.replace("ሺ", "ሽ")
        #punctuation="!<<“…/\@%&*.…._፦,.”?\\”"
        #for x in string:
        #    if str(x) in punctuation:
        #        string=string.replace(x,"")
                    
        return string

def remove_punctuation(s):
    punctuation="<<“…/@%&*.#%^*,./())(፤፣#%-""'፡»…._፦,.””"
    string=s
    for x in s:
        if str(x) in punctuation:
            string=string.replace(x,"")
    return string

def sentence_tokenizer(s):
    sents=re.compile('[።!?፡፡]').split(s)

    return sents

def word_tokenizer(s):
    import re
    tokens = re.findall("[\w]+", s)

    return tokens

def preprocess(s):
    return [ w for w in str(s).split() ]

#'''
########test
#
#spellcheck.load_dictionary(r'C:\Users\hilena\Downloads\amharic_spell_corrector-master\data\dictionary.txt')
#text='አክብሮሮሮሮናትና አክብሮት አሽናቆት አአአአአአአአላዋዋዋዋዋቂቂ ቂቂቂቂ'
#words=text.split()
#words=[corrector(remove_repeated_spell(word)) for word in words]
#
#words
#Out[9]: ['አክብሮትና', 'አክብሮት', 'አድናቆት', 'አላዋቂ', 'ቂ']
#'''
