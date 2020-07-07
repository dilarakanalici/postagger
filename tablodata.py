# -*- coding: utf-8 -*-
"""

@author:
"""


import numpy as np
import pandas as pd


    words=[]
    tags=[]
    for line in lines.split("\n"):
        if line=="":
            continue
        w=line.split()[0]
        if(w.find("'")!=-1):
            words.append(w[:w.find("'")])
            tags.append(line.split()[1])
            words.append(w[w.find("'"):])
            tags.append("")
        else:
            words.append(w)
            tags.append(line.split()[1])
    return words, tags



def find_tag(tag):
    start=tag.find("+")+1
    if tag[start:].find("+")==-1:
        tag=tag[start:]
    else:
        end=tag[start:].find("+")+start
        tag=tag[start:end]
    return tag





def change_tag(tag_list):
    turkish_tag_list_adj = ["AFutPart","APastPart","APresPart","Adj"]
    turkish_tag_list_noun = ["NFutPart","NPastPart","NPresPart","NInf","Noun","Prop"]
    turkish_tag_list_num = ["Card","Distrib","Num","Ord","Range","Real"]
    turkish_tag_list_pron = ["DemonsP","PersP","Pron","QuesP","ReflexP"]
    turkish_tag_list_pun = ["Punc","Ques"]
    turkish_tag_list_verb = ["Verb","Zero"]
    
    
    for i, w in enumerate(tag_list):
        if w in turkish_tag_list_adj:
            tag_list[i] = "ADJ"
        if w in turkish_tag_list_noun:
            tag_list[i] = "NOUN"
        if w in turkish_tag_list_num:
            tag_list[i] = "NUM"
        if w in turkish_tag_list_pron:
            tag_list[i] = "PRON"
        if w in turkish_tag_list_pun:
            tag_list[i] = "."
        if w in turkish_tag_list_verb:
            tag_list[i] = "VERB"
        if w == "Adverb":
            tag_list[i] = "ADV"
        if w == "Conj":
            tag_list[i] = "CONJ"
        if w == "Det":
            tag_list[i] = "DET"
        if w == "Dup":
            tag_list[i] = "PRT"
        if w == "Interj":
            tag_list[i] = "X"
        if w == "Postp":
            tag_list[i] = "ADP"
            return tag_list
         
            
            
            
def tag(doc_no, filename):
    file = open(filename, "r")
    f=file.read()
    words, tags=split_lines(f)
    doc={"doc_no":[], "sentence_no":[], "word":[], "tag":[]}
    sentence_no=0
    for i in range(len(words)):
        if(words[i]!=""):
            if words[i]!="</S>" and words[i]!="<S>": 
                doc["doc_no"].append(doc_no)
                doc["sentence_no"].append(sentence_no)
                doc["word"].append(words[i])
                doc["tag"].append(find_tag(tags[i]))
                if(words[i].find(".")!=-1 or words[i].find("?")!=-1 or words[i].find("!")!=-1):
                    sentence_no+=1
    return doc






doc=tag(doc_no=2800, filename="dunyaitu_out.txt")

df=pd.DataFrame(doc)



df




df["new_tag"]=change_tag(df.tag.copy())
df[30:50]




#df.drop("tag", axis=1).to_csv("001.csv", index=False)



