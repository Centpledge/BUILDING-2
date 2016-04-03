import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import Tkinter as tk
from Tkinter import *
import ttk
import csv
import sentiment_mod as s
from Tkinter import *
from ttk import *
from PIL import ImageTk ,Image
import tkMessageBox
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.stem import PorterStemmer
import requests
from bs4 import BeautifulSoup
from collections import Counter
import operator
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import pickle
ps = PorterStemmer()
tupleList = []
all_entries = []
getLink = []
listWord = []
newListWord =[]
filteredList = []
f = filteredList
stemmedList = []
lower = []
uniToStr = []
all_entries = []
wcText = []
sentence = []
typeList = []
artWord = []
comScWord = []
PArt = []
PComSc = []
wordCollect = ["Empty"]
ent = ""
notCount= ["a","is","the","for","and",';',':','(',')','[',']','{','{','}','is','am','are',
        'the','an','his','her','him','your','you','we','they','it','its','he','?','!',
        '.','this','that','these','those','of','to',',','in','``',"''",'He',"n't",
        'are','not','with','on','in','^','or','A','as','-','&','same','1','thi','at',
        '2','3','4','5','6','7','8','9','0','m.','so','/','It','=','<','>','but',
        'a','b','c','d','e','f','g','h','i','I','j','k','l','m','y','_','+',"'s",'hi',
        'from','by',' as','be','form','may','have','has','which','pp','The',
        "'",'w.','d.','so','So','!','ha','she','She']
LARGE_FONT= ("Verdana", 12)
LARGER_FONT = ("Verdana",20)
LARGEST_FONT = ("Verdana",25)
style.use("ggplot")
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)



def submitLink():   ### PRESS SUBMIT
    

    r = requests.get("https://en.wikipedia.org/wiki/Art")
    r.content
    soup = BeautifulSoup(r.content,"lxml")
    g_data =soup.find_all("p")
    foundSymbol = 0
    for a in g_data :
    
        for b in word_tokenize(a.text):
            listWord.append(b)
        for b in sent_tokenize(a.text):
            sentence.append(b)


    for a in listWord:
        stemmedList.append(ps.stem(a))


    for a in stemmedList : 
        for b in notCount :
            if a==b:
                foundSymbol = 1
        if foundSymbol !=1:      
            filteredList.append(a)

            foundSymbol = 0
        foundSymbol = 0

    for a in filteredList :
        try :
            lower.append(str(a.lower()))
            wordCollect.append(a.lower())
        except :
            print "unicode deleted"
            

    strLower = ' '.join(lower) 
    aa = str(strLower)
    return aa
class testCase():
    def testLower(self,output,expected):
            if output.islower()!=expected :
                return False
            else :
                return True
a = submitLink()
b = testCase().testLower(a,True)
print b 
