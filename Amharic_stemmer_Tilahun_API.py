import os
import math
import codecs
import string
import re
import glob
import sys
def condition1(affix, tempp):
            if len(tempp)> 2:
                if affix.__eq__(u'\u12a8'):
                        return 1
                elif affix.__eq__(u'\u1260'):
                       return 1
                elif affix.__eq__(u'\u129E\u127D'):
                       return 1
                elif affix.__eq__(u'\u1295'):
                       return 1
                elif affix.__eq__(u'\u1275'):
                       return 1
                elif affix.__eq__(u'\u1290\u1275'):
                       return 1
                elif affix.__eq__(u'\u12CE\u127D'):
                       return 1
                elif affix.__eq__(u'\u127D'):
                       return 1
                elif affix.__eq__(u'\u127D\u1295'):
                       return 1
                elif affix.__eq__(u'\u127D\u1201'):
                       return 1
                elif affix.__eq__(u'\u1278\u12CD'):
                       return 1
                elif affix.__eq__(u'\u1271'):
                       return 1
                elif affix.__eq__(u'\u1279'):
                       return 1
                elif affix.__eq__(u'\u12CA'):
                       return 1
                elif affix.__eq__(u'\u12CA\u1275'):
                       return 1
                elif affix.__eq__(u'\u12CD\u12EB\u1295'):
                       return 1
                elif affix.__eq__(u'\u1277\u120D'):
                       return 1
                elif affix.__eq__(u'\u121D'):
                       return 1
                elif affix.__eq__(u'\u1275') or affix.__eq__(u'\u12A0'):
                       return 1
                elif affix.__eq__(u'\u129B'):
                       return 1
                elif affix.__eq__(u'\u1290\u1275') or affix.__eq__(u'\u12A5'):
                       return 1
                elif affix.__eq__(u'\u121D') or affix.__eq__(u'\u12A5'):
                       return 1
                elif affix.__eq__(u'\u1208\u1275'):
                       return 1
            else:
                return 0
def condition2(affix,tempp):
            if len(tempp) > 2:
                if affix.__eq__(u'\u12A8'):
                    if tempp.__eq__(u'\u12A8\u1265\u1275') or tempp.__eq__(u'\u12A8\u1208\u12A8\u1208') or tempp.__eq__(u'\u12A8\u1290\u12A8\u1290') or tempp.__eq__(u'\u12A8\u1228\u12A8\u1228') or tempp.__eq__(u'\u12A8\u1128\u12A8\u1218') or tempp.__eq__(u'\u12A8\u1230\u12A8\u1230') or tempp.__eq__(u'\u12A8\u1270\u12A8\u1270') or tempp.__eq__(u'\u12A8\u1270\u121B') or tempp.__eq__(u'\u12A8\u1228\u1295') or tempp.__eq__(u'\u12A8\u1230\u120D') or tempp.__eq__(u'\u12A8\u134D\u1270\u129B') or tempp.__eq__(u'\u12A8\u1265\u1275'):
                        return tempp
    ##                elif len(tempp)==3:
    ####                    if (check(str)) 
    ##                    return tempp
                    else:
                        tempp = tempp[1: ]
                        tempp = preffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u1260'):
                    if tempp.__eq__(u'\u1260\u123D\u1273') or tempp.__eq__(u'\u1260\u1300\u1275') or tempp.__eq__(u'\u1260\u1228\u1260\u1228') or tempp.__eq__(u'\u1260\u1230\u1260\u1230'):
                        return tempp
                    else:
                        tempp = tempp[1: ]
                        tempp = preffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u129B'):
                    if tempp.__eq__(u'\u1260\u123D\u1273'):
                        return tempp
                    else:
                        tempp = tempp[ :-1]
                        tempp = preffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u1295'):
                    if tempp.__eq__(u'\u12D8\u1218\u1295') or tempp.__eq__(u'\u1261\u12F5\u1295') or tempp.__eq__(u'\u123D\u134B\u1295') or tempp.__eq__(u'\u12C8\u1308\u1295') or tempp.__eq__(u'\u1261\u12F5\u1295') or tempp.__eq__(u'\u123D\u134B\u1295') or tempp.__eq__(u'\u12C8\u1308\u1295') or tempp.__eq__(u'\u132D\u1241\u1295') or tempp.__eq__(u'\u1205\u133B\u1295') or tempp.__eq__(u'\u12A5\u12CD\u1295') or tempp.__eq__(u'\u12A5\u121D\u1295') or tempp.__eq__(u'\u12D8\u1348\u1295'):
                        return tempp
                    else:
                        tempp = tempp[ :-1]
##                        tempp=sadisConverter(tempp)
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u1208\u1275'):
                    if tempp.__eq__(u'\u12A0\u1208\u1275') or tempp.__eq__(u'\u12A5\u1208\u1275') or tempp.__eq__(u'\u1201\u1208\u1275'):
                        return tempp
                    else:
                        tempp = tempp[ :-2]
                        #change to sades
                        tempp = suffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u1275'):
                    if tempp.__eq__(u'\u12A0\u1263\u1275') or tempp.__eq__(u'\u12A0\u12EB\u1275') or tempp.__eq__(u'\u1205\u12ED\u12C8\u1275') or tempp.__eq__(u'\u12A0\u122B\u12CA\u1275') or tempp.__eq__(u'\u1230\u12A3\u1275') or tempp.__eq__(u'\u1218\u1265\u1275') or tempp.__eq__(u'\u1218\u1230\u1228\u1275') or tempp.__eq__(u'\u12C8\u1245\u1275') or tempp.__eq__(u'\u1325\u1228\u1275') or tempp.__eq__(u'\u1275\u122D\u134D') or tempp.__eq__(u'\u1201\u1208\u1275') or tempp.__eq__(u'\u1236\u1235\u1275') or tempp.__eq__(u'\u12A0\u122B\u1275') or tempp.__eq__(u'\u12A0\u121D\u1235\u1275') or tempp.__eq__(u'\u1235\u12F5\u1235\u1275') or tempp.__eq__(u'\u1230\u1263\u1275') or tempp.__eq__(u'\u1235\u121D\u1295\u1275') or tempp.__eq__(u'\u1275\u121D\u1205\u122D\u1275') or tempp.__eq__(u'\u1325\u1245\u121D\u1275') or tempp.__eq__(u'\u1233\u121D\u1295\u1275') or tempp.__eq__(u'\u12AD\u122B\u12CA\u1275'):
                       return tempp
                    else:
                        tempp = tempp[ :-1]
                        #change to sades
                        tempp = suffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u1290\u1275'):
                    if tempp.__eq__(u'\u12A5\u12CD\u1290\u1275') or tempp.__eq__(u'\u12A5\u121D\u1290\u1275'):
                        return tempp
                    else:
                        tempp = tempp[ :-1]
                        #change to sades
                        tempp = suffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u12CE\u127D'):
                    if tempp.__eq__(u'\u1230\u12CE\u127D'):
                        str1 = tempp[-1: ]
                        str2 = tempp[ :len(tempp)-2]
                        str3 = (u'\u12C9')
                        tempp = str2 + str3
                        #change to sades
                        return tempp
                    else:
                        tempp = tempp[ :-2]
                        #change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u129E\u127D'):
                    if tempp.__eq__(u'\u12F3\u129E\u127D'):
                        tempp = tempp[ :-1]
                        ##change to sades
                        return tempp
                    else:
                        tempp = tempp[ :-1]
                        #change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u127D'):
                        tempp = tempp[ :-1]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u127D\u1295'):
                        tempp = tempp[ :-2]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u127D\u1201'):
                        tempp = tempp[ :-2]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u1278\u12CD'):
                        tempp = tempp[ :-2]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u1271'):
                        ##change to sades
##                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u1279'):
                        tempp = tempp[ :-1]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u12CA'):
                        tempp = tempp[ :-1]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u12CA\u1275'):
                    if tempp.__eq__(u'\u12A0\u122B\u12CA\u1275'):
                        return tempp
                    else:
                        tempp = tempp[ :-2]
                        #change to sades
                        tempp = suffix(tempp);
                        return tempp
                elif affix.__eq__(u'\u12CD\u12EB\u1295'):
                        tempp = tempp[ :-3]
                        ##change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u1277\u120D'):
                    if tempp.__eq__(u'\u121E\u1277\u120D'):
                        tempp = tempp[ :-1]
                        ##change to sades
                        return tempp
                    else:
                        tempp = tempp[ :-2]
                        #change to sades
                        tempp = suffix(tempp)
                        return tempp
                elif affix.__eq__(u'\u121D'):
                    if tempp.__eq__(u'\u1308\u12F3\u121D') or tempp.__eq__(u'\u1230\u120B\u121D') or tempp.__eq__(u'\u12A0\u1208\u121D'):
                        return tempp
                    else:
                        tempp = tempp[ :-1]
                        #change to sades
                        tempp = suffix(tempp);
                        return tempp
            else:
                return tempp
def preffix(word):
            if len(word)<3:
                return word
            else:
                while len(word)>=3:
                    tempp=word[ :3]
                    #p=codecs.open("prefix.txt",'r', encoding = 'utf-8' )
                    #pr = p.read()
                    #ours light weight prefix
                    pr="ስልኧምኣይ|ዕንድኧ|ይኧትኧ|ብኧምኣ|ብኧትኧ|ዕኧል|ስልኧ|ምኧስ|ዕይኧ|ዕኧስ|ዕኧት|ዕኧን|ዕኧይ|ይኣል|ስኣት|ስኣን|ስኣይ|ስኣል|ይኣስ|ይኧ|ልኧ|ክኧ|እን|ዕን|ዐል|ይ|ት|አ|እ"
                    y=pr.split('|')
                    
                    #geez prefix
                    y= ["የ", "ለ", "ይ", "አል", "በ", "እየ", "ሳይ", "አት", "አስ", "እንደ", "እስኪ", "ያል", "ባለ", "እንዲ", "እያስ",   "በስተ", "ወደ", "ያስ", "ት","ል", "ስለ", "እስክ", "ሲ", "እንድ", "አስ", "ምት", "በስተ", "ወደ", "ያለ", "ማይ", "የ", "ሳት", "ያስ", "እንዲ", " ት", "ያ", "አላ", "እስከ", "በ", "ተ","ት", "ሚ", "እን", "በት", "ከ", "ተ", "ወ", "አይ", "የ"]
                    #Amharic prefix
                    y=["የ", "ለ", "ይ", "አል", "በ", "እየ", "ሳይ", "አት", "አስ", "እንደ", "እስኪ", "ያል", "ባለ", "እንዲ", "እያስ",   "በስተ", "ወደ", "ያስ", "ት","ል", "ስለ", "እስክ", "ሲ", "እንድ","አስ", "ምት", "በስተ", "ወደ", "ያለ", "ማይ", "የ", "ሳት","ያስ", "እንዲ", " ት", "ያ", "አላ", "እስከ", "በ", "ተ", "ት", "ሚ", "እን", "በት", "ከ", "ተ", "ወ", "አይ", "የ"]
                    #p.close()
                    if y.__contains__(tempp):
                        if (condition1(tempp,word)):
                            word=condition2(tempp,word)
                            return word
                        else:
                            word=word[3: ]
                            preffix(word)
                    else:
                        tempp=word[ :2]
                        if  y.__contains__(tempp):
                            if (condition1(tempp,word)):
                                word=condition2(tempp,word)
                                return word
                            else:
                                word=word[2: ]
                                preffix(word)
                        else:
                            tempp=word[ :1]
                            if  y.__contains__(tempp):
                                if (condition1(tempp,word)):
                                    word=condition2(tempp,word)
                                    return word
                                else:
                                    word=word[1: ]
                                    preffix(word)

                            else:
                                return word
                                
            return word
def suffix(word):
            if len(word)<3:
                return word
            else:
                while len(word)>=3:
                    tempp=word[len(word)-3: ]
                    #s=codecs.open("sufix.txt",'r', encoding = 'utf-8' )
                    #su = s.read()
                    
                    #Light weight sufix
                    su="ኢዕኧልኧሽ|ኣውኢው|ኣችኧውኣል|ኧችኣት|ኧው|ኧችኣችህኡ|ኧችኣችኧው|ኣልኧህኡ|ኣውኦች|ኣልኧህ|ኣልኧሽ|ኣልችህኡ|ኣልኣልኧች|ብኣችኧውስ|ብኣችኧው|ኣችኧውን|ኣልኧች|ኣልኧን|ኣልኣችህኡ|ኣችህኡን|ኣችህኡ||ኣችህኡት|ውኦችንንኣ|ውኦችን|ኣችኧው|ውኦችኡን|ውኦችኡ|ኧውንኣ|ኦችኡን|ኦውኦች|ኧኝኣንኧትም|ኧኝኣንኣ| ኧኝኣንኧት|ኧኝኣን|ኧኝኣውም|ኧኝኣው|ኝኣውኣ|ብኧትን|ኣችህኡም|ኦውኣ|ኧችው|ኧችኡ|ኤችኡ|ንኧው|ንኧት|ኣልኡ|ኣችን|ክኡም|ክኡት|ክኧው|ኧችን|ኧችም|ኧችህ|ኧችሽ|ኧችን|ኧችው|ይኡሽን|ይኡሽ|ኧውኢ|ኦችንንኣ|ኣውኢ|ብኧት|ኦች|ኦችኡ|ውኦን|ኧኝኣ|ኝኣውን|ኝኣው|ኦችን|ኣል|ኧም|ሽው|ክም|ኧው|ትም|ውኦ|ውም|ውን|ንም|ሽን|ኣች|ኡት|ኢት|ክኡ|ኤ|ህ|ሽ|ኡ|ሽ|ክ|ኧ|ኧች|ኡን|ን|ም|ንኣ|ው"
                    
                    x=su.split('|')
                    
                    #Geez sufix
                    x=["ን", "ና", "ሽ", "ነት",  "ቸው", "ህ", "ባት", "ኞች", "ዋ", "ችኋል", "ዎች", "ም", "ለን", "ለት", "ዊ","ቹ", "ውያን", "ዎች", "ዋ", "ኝ", "ኞች", "ያ", "ችን", "ቸው","ች", "ቸው" "ዊ", "በት", "ችሁ", "ዋ", "ን", "ህ", "ኛ", "አቸዋል", "ቹ", "ችሁ", "ውያን", "ቻቸው", " ይ", "ቸው", "ህ", "ኞቸ", "ለ", "ት"]
                    
                    #Amharic sufix
                    x=["ን", "ና", "ሽ", "ነት",  "ቸው", "ህ", "ባት", "ኞች", "ዋ", "ችኋል", "ዎች", "ም", "ለን", "ለት", "ዊ","ቹ", "ውያን", "ዎች", "ዋ", "ኝ", "ኞች", "ያ", "ችን", "ቸው","ች", "ቸው" "ዊ", "በት", "ችሁ", "ዋ", "ን", "ህ","ኛ", "አቸዋል", "ቹ", "ችሁ", "ውያን", "ቻቸው", " ይ", "ቸው", "ህ", "ኞቸ", "ለ", "ት"]
                    #s.close()
                    if x.__contains__(tempp):
                        if (condition1(tempp,word)):
                            word=condition2(tempp,word)
                            return word
                        else:
                            word=word[ :len(word)-3]
                            suffix(word)
                    else:
                        tempp=word[len(word)-2: ]
                        if  x.__contains__(tempp):
                            if (condition1(tempp,word)):
                                word=condition2(tempp,word)
                                return word
                            else:
                                word=word[ :len(word)-2]
                                suffix(word)
                        else:
                            tempp=word[len(word)-1: ]
                            if  x.__contains__(tempp):
                                if (condition1(tempp,word)):
                                    word=condition2(tempp,word)
                                    return word
                                else:
                                    word=word[ :len(word)-1]
                                    suffix(word)

                            else:
                                return word
                                
                                
            return word
'''
#testing
text="የኬንያና የአልሸባብ ፍጥጫ"
for word in text.split():
    print (word ,"=> ", preffix(suffix(word)))
    
'''
def stemer(word):
    return preffix(suffix(word))

    