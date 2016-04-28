import matplotlib
import codecs
import time
matplotlib.use("TkAgg")
from nose.tools import assert_equal, assert_greater, assert_true, assert_raises
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import Tkinter as tk
import tkFileDialog
from Tkinter import *
import ttk
from random import Random
import csv
import sentiment_mod as s
from ttk import *
from PIL import ImageTk ,Image
import tkMessageBox
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.stem import PorterStemmer
from nose.tools import assert_equal, assert_greater, assert_true, assert_raises
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
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import pickle
ps = PorterStemmer()
tupleList = []
ccc = []
checkLoad =[]
checkLink = []
all_entries = []
getLink = []
listWord = []
newListWord =[]
filteredList = []
allFile =[]
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
wordFreq = []
PArt = []
PComSc = []
loadT = []
loadTr= []
textB ='0'
savedWord = []
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

class testCase():
    def checkOutput(self,output,result) :
        if output != result :
            return False
        else :
            return True

    
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Text Mining")
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(500, weight=5)
        container.grid_columnconfigure(500, weight=5)

        self.frames = {}

        for F in (StartPage,enterInput):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=100, column=100, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Text mining program", font=LARGER_FONT)
        label.pack(pady=20,padx=10)
        label2 = tk.Label(self, text="First you need to enter your url", font=LARGE_FONT)
        label2.pack(pady=50,padx=10)

        button = tk.Button(self, text="I understand, go next ",font=LARGE_FONT,width = 20,height = 5,
                            command=lambda: controller.show_frame(enterInput))
        button.pack()
        print "Program is running"



class enterInput(tk.Frame):  ### program window
    pdfCount = 0
    txtCount = 0
    linkCount = 0
    htmlCount = 0
    artC = 0
    comScC = 0
    checkSubmit  = False
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Link", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="you can enter both link and text file", font=LARGE_FONT)
##        label2.pack(pady=10,padx=10)
        artCount = 0
        comScCount = 0
       

        subbutton = tk.Button(self, text="SUBMIT",font = LARGE_FONT,width =45,height = 2 ,command=self.func)
        delbutton = tk.Button(self, text="DELETE ALL",width = 30, command=self.delAllList)
        popbutton = tk.Button(self, text="DELETE Lastest link",width = 30, command=self.delLastList)

 
##        ww = Label(self, text="After you entered all links click SUBMIT")
##    
##        ww.pack(pady=5)
        ent = Entry(self,width = 60)
        ent.pack(pady=2,padx=10)
        all_entries.append( ent )
##        subbutton.pack(pady = 25)
        sp7 = Label(self, text="")
        sp7.pack()
        button10 = tk.Button(self, text="Add Link",width = 30,
                            command=self.enterLink)
        button10.pack()
        button7 = tk.Button(self, text="Select Text File",width = 30,
                            command=self.chooseFile)
     
        button7.pack()
        button9 = tk.Button(self, text="Submit and Run",width = 30,
                            command=self.submitCheck)
        button9.pack()
##        popbutton.pack()
        delbutton.pack()
        sp1 = Label(self, text="Word Cloud")

   


    
        sp1.pack(pady = 10)
##        button1 = tk.Button(self, text="Back to Home",width = 45,height = 2,
##                         command=lambda: controller.show_frame(StartPage))
        

        button4 = tk.Button(self, text="All word cloud",width = 30,
                            command=self.showWc)
        button4.pack()
        button5 = tk.Button(self, text="Art word cloud",width = 30,
                            command=self.showWcArt)
        button5.pack()
        button6 = tk.Button(self, text="Computer Science word cloud",width = 30,
                            command=self.showWcComSc)
        button6.pack()
        sp2 = Label(self, text="Histogram ")
        
        sp2.pack(pady = 10)
        plotW = tk.Button(self, text="All word",width = 30, command=self.plotG)
        plotW.pack()

        plotWArt = tk.Button(self, text="Art word",width = 30, command=self.plotGArt)
        plotWArt.pack()
        plotWComSc = tk.Button(self, text="Computer Science word",width = 30, command=self.plotGComSc)
        plotWComSc.pack()
        sp3 = Label(self, text="")
        sp3.pack()
##        button1.pack(pady = 40)


##        listbox2 = Listbox(self,width =50,height = 5)
##        listbox2.pack()
        
##        for i in range(10):
##            listbox2.insert(END, str(i))
##        listbox2.insert(END,"TEXT MINING")
##        self.updateBox("TEXT MINING",listbox2)
       
    def updateBox(self,text,box):
        return box.insert(END,text)
        
    def checkCase(self,output,result):
        print testCase().checkOutput(output,result)
        
        
        
    def plotG(self): ## plot histogram all word
        c = Counter(wordCollect)
        

        labels,values = zip(*c.most_common(10))

        indexes = np.arange(len(labels))
        width = 1
        
        a = plt.bar(indexes,values,width)
        a[0].set_color('r')
        a[1].set_color('orange')
        a[2].set_color('y')
        a[3].set_color('green')
        a[4].set_color('lime')
        a[5].set_color('cyan')
        a[6].set_color('turquoise')
        plt.xticks(indexes + width * 0.5,labels)
        plt.title("Frequency of Words")
        plt.grid(True)
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.show()

    def plotGArt(self): ## plot histogram art
        try :
            c = Counter(PArt)
            

            labels,values = zip(*c.most_common(10))

            indexes = np.arange(len(labels))
            width = 1
            a = plt.bar(indexes,values,width)
            a[0].set_color('r')
            a[1].set_color('orange')
            a[2].set_color('y')
            a[3].set_color('green')
            a[4].set_color('lime')
            a[5].set_color('cyan')
            a[6].set_color('turquoise')
            plt.bar(indexes,values,width)
            plt.xticks(indexes + width * 0.5,labels)
            plt.title("Frequency of Words")
            plt.grid(True)
            plt.xlabel("Words")
            plt.ylabel("Frequency")
            plt.show()
        except :
            print "Empty"
    def plotGComSc(self): ## plot histogram comSc
        try :
            c = Counter(PComSc)
            

            labels,values = zip(*c.most_common(10))

            indexes = np.arange(len(labels))
            width = 1
            b = plt.bar(indexes,values,width)
            b[0].set_color('r')
            b[1].set_color('orange')
            b[2].set_color('y')
            b[3].set_color('green')
            b[4].set_color('lime')
            b[5].set_color('cyan')
            b[6].set_color('turquoise')
            plt.bar(indexes,values,width)
            plt.xticks(indexes + width * 0.5,labels)
            plt.title("Frequency of Words")
            plt.grid(True)
            plt.xlabel("Words")
            plt.ylabel("Frequency")
            plt.show()
        except:
            print "Empty"
    def showWc(self):   ## All word wordcloud
        try :
            a = ' '.join(wordCollect)       
            wordcloud = WordCloud(font_path='angsau.ttf' ,min_font_size = 7,background_color = 'white',max_font_size=55, relative_scaling=0.2).generate(a)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.show()
            imgWidth = 600
            imgHeight = 250
            xPoint = 0
            yPoint = 0
            num = 0
        except :
            print "Empty"
    def showWcArt(self):  ## Art wordcloud
        if artWord==[]:
            pass
        else :
            try :
                a = ' '.join(artWord)
                wordcloud = WordCloud(font_path='angsau.ttf' ,min_font_size = 7,background_color = 'white',max_font_size=60, relative_scaling=0.2).generate(a)
                plt.imshow(wordcloud)
                plt.axis("off")
                plt.show()
                imgWidth = 600
                imgHeight = 250
                xPoint = 0
                yPoint = 0
                num = 0
            except :
                print "Empty"
    def showWcComSc(self):  ## Computer science wordcloud
        if comScWord ==[]:
            pass
        else :
            try:
                c = ' '.join(comScWord)
                wordcloud = WordCloud(font_path='angsau.ttf' ,min_font_size = 7,background_color = 'white',max_font_size=60, relative_scaling=0.2).generate(c)
                plt.imshow(wordcloud)
                plt.axis("off")
                plt.show()
                imgWidth = 600
                imgHeight = 250
                xPoint = 0
                yPoint = 0
                num = 0
            except:
                "Empty"
    def func(self):
        global ent

        for number, ent in enumerate(all_entries):
            if len(ent.get()) == 0 and loadT ==[] and checkLoad ==[]:
                    
                    print "this entry is  empty555"    ## check if entry is empty or not
                    
                 
            else:
                allLinks = open("data_input/links.pickle","wb") ## if not empty then dump all links
                pickle.dump(ent.get(), allLinks)
                allLinks.close()
                checkLink.append('b')

                splitLink = ent.get().split() ## split each links
                
                print "ADD  " + ent.get()  ## print all added links
##                print splitLink
                for item in splitLink :
                    getLink.append(item)   ## append splited links in to getLink
                    ent.delete(0, 'end')   ##
##                print getLink
        self.submitCheck()
    def pullText(self,link):
        r = requests.get(link)
        r.content
        soup = BeautifulSoup(r.content,"lxml")
        g_data =soup.find_all("p")
        return g_data
    
    


    def wordToken(self,sentence,listA):
        
            for a in word_tokenize(sentence):
                listA.append(a)
        
    def sentToken(self,sentence,listA):
  
            for a in sent_tokenize(sentence):
                listA.append(a)
                
    def appendLower(self,sentence,listA):
        for item in sentence:
            listA.append(item.lower())
            
    def enterLink(self):
        global ent

        for number, ent in enumerate(all_entries):
            if len(ent.get()) == 0 and loadT ==[] and checkLoad ==[]:
                    print "this entry is  empty"    ## check if entry is empty or not
                
                 
            else:
                allLinks = open("data_input/links.pickle","wb") ## if not empty then dump all links
                pickle.dump(ent.get(), allLinks)
                allLinks.close()
                checkLink.append('b')

                splitLink = ent.get().split() ## split each links
                
                print "ADD  " + ent.get()  ## print all added links
##                print splitLink
                for item in splitLink :
                    getLink.append(item)   ## append splited links in to getLink
                    ent.delete(0, 'end')   ##
##                print getLink
        checkLink.append('a')
    def printLink(self):     ## PRINT LINK
        if len(getLink) == 0: ## if link empty print EMPTY
            print "EMPTY"    
        else :
            print getLink     ## if not print link
        
    def onclick(self):  ## CHECK CLICKED
        print("You clicked the button")

    def delAllList(self):   ## DELETE ALL LIST
        print "All saved links DELETED"
        del getLink[:]
        del tupleList[:]
        del listWord[:]
        del newListWord[:]
        del filteredList[:]
        del stemmedList[:]
        del lower[:]
        del uniToStr[:]
        del savedWord[:]
        del wordFreq[:]
        del typeList[:]
        del artWord[:]
        del comScWord[:]
        del PArt[:]
        del PComSc[:]
        del sentence[:]
        del wcText[:]
        del checkLink[:]
        del checkLoad[:]
        artCount = 0
        comScCount = 0
        enterInput.pdfCount = 0
        enterInput.txtCount = 0
        enterInput.linkCount = 0
        enterInput.htmlCount = 0
        enterInput.artC = 0
        enterInput.comScC = 0
        enterInput.checkSubmit  = False
        self.checkCase(getLink,[])
        
        
    def delLastList(self):     ### delete last index
        if len(getLink) == 0:
            print "EMPTY"
            print self.checkCase(getLink,[])
        else:
            getLink.pop()   ## if not deletd last index
            print "Lastest link deleted current link in list : "
            print getLink
            
    def checkEnd(self,fileCh):
        
        if fileCh.endswith('.txt'):
            
            return "txt"
        elif fileCh.endswith('.html'):
            
            return "html"
        elif fileCh.endswith('.pdf'):
            
            return "pdf"
            self.pdfLoad(fileCh)
            
    def chooseFile(self):
       
        
        filez = tkFileDialog.askopenfilenames()
        splitFilez = self.tk.splitlist(filez)
        for item in splitFilez :
            print "ADD %s" %item
            openIt = open(item,'r')
            allFile.append(item) #each file
##            self.checkEnd(item)
##            file_contents = openIt.read()
##            print file_contents
##            loadT.append(file_contents)
##            openIt.close()
##        a = ''.join(loadT)
##        b =  a.rstrip()
##        for word in word_tokenize(b):
##            try:
##        loadTr.append(word)
        checkLoad.append('a')
##            except:
##                pass
       

    def itsPDF(self,path):
        enterInput.pdfCount += 1
        foundSymbol = 0
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        
        for b in word_tokenize(text):
            listWord.append(b)
        for b in sent_tokenize(text):
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
            lower.append(a.lower())
            wordCollect.append(a.lower())
        
        a = ' '.join(listWord)
        b = ' '

        savedWord = []
        wordFreq = []

        c = Counter(lower)
        del listWord[:]
        del newListWord[:]                   
        del stemmedList[:]
        del lower[:]
        del uniToStr[:]
        del savedWord[:]
        del wordFreq[:]
        artCount = 0
        comScCount = 0
        for a in sentence :
            if (s.sentiment(a))=="art" : ## check type for each sentence
                artCount = artCount +1
            else :
                comScCount = comScCount +1

        allType = artCount + comScCount  ## calculate all word numbers
        artPercent = float((float(artCount)/float(allType)))*100
        comScPercent = float((float(comScCount)/float(allType)))*100
        
        if artPercent > comScPercent : 
            typeText = "ART"        ## if number of art sentence > com then it's ART
            for word in sentence :
                artWord.append(word)
            for a in filteredList :
                PArt.append(a.lower())
        else :
            typeText = "COMPUTER SCIENCE" ## if not its COM
            for word in sentence :
                comScWord.append(word)
            for a in filteredList :
                PComSc.append(a.lower())
        typeList.append((path,typeText))
    
        del sentence[:]
        del filteredList[:]
    def itsTXT(self,f) :
        foundSymbol = 0
        enterInput.txtCount += 1
        file_contents = f
        a= open(f,'r')
        
        aa = a.read()
        print aa
        loadT.append(a.read)
        
        
        
        
                        
        for b in word_tokenize(aa):
            listWord.append(b)
        for b in sent_tokenize(aa):
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
            lower.append(a.lower())
            wordCollect.append(a.lower())
        
        a = ' '.join(listWord)
        b = ' '

        savedWord = []
        wordFreq = []

        c = Counter(lower)
        del listWord[:]
        del newListWord[:]                   
        del stemmedList[:]
        del lower[:]
        del uniToStr[:]
        del savedWord[:]
        del wordFreq[:]
        artCount = 0
        comScCount = 0
        for a in sentence :
            if (s.sentiment(a))=="art" : ## check type for each sentence
                artCount = artCount +1
            else :
                comScCount = comScCount +1

        allType = artCount + comScCount  ## calculate all word numbers
        artPercent = float((float(artCount)/float(allType)))*100
        comScPercent = float((float(comScCount)/float(allType)))*100
        
        if artPercent > comScPercent : 
            typeText = "ART"        ## if number of art sentence > com then it's ART
            for word in sentence :
                artWord.append(word)
            for a in filteredList :
                PArt.append(a.lower())
        else :
            typeText = "COMPUTER SCIENCE" ## if not its COM
            for word in sentence :
                comScWord.append(word)
            for a in filteredList :
                PComSc.append(a.lower())
        typeList.append((f,typeText))
    
        del sentence[:]
        del filteredList[:]
        
    def itsHTML(self,f):
        
        enterInput.htmlCount += 1
        foundSymbol = 1
        f=codecs.open(f, 'r')
        soup = BeautifulSoup(f,'html.parser')
        
        
        for b in word_tokenize(soup.get_text()):
            try:
                listWord.append(b)
            except:
                pass
        for b in sent_tokenize(soup.get_text()):
            try:
                sentence.append(b)
            except:
                pass
        for a in listWord:
            try:
                stemmedList.append(ps.stem(a))
            except:
                pass

        for a in stemmedList :
            
            for b in notCount :
                if a==b:
                    foundSymbol = 1
            if foundSymbol !=1:      
                filteredList.append(a)

                foundSymbol = 0
            foundSymbol = 0

        for a in filteredList :
            lower.append(a.lower())
            wordCollect.append(a.lower())
        
        a = ' '.join(listWord)
        b = ' '

        savedWord = []
        wordFreq = []

        c = Counter(lower)
        del listWord[:]
        del newListWord[:]                   
        del stemmedList[:]
        del lower[:]
        del uniToStr[:]
        del savedWord[:]
        del wordFreq[:]
        artCount = 0
        comScCount = 0
        for a in sentence :
            if (s.sentiment(a))=="art" : ## check type for each sentence
                artCount = artCount +1
            else :
                comScCount = comScCount +1

        allType = artCount + comScCount  ## calculate all word numbers
        artPercent = float((float(artCount)/float(allType)))*100
        comScPercent = float((float(comScCount)/float(allType)))*100
        
        if artPercent > comScPercent : 
            typeText = "ART"        ## if number of art sentence > com then it's ART
            for word in sentence :
                artWord.append(word)
            for a in filteredList :
                PArt.append(a.lower())
        else :
            typeText = "COMPUTER SCIENCE" ## if not its COM
            for word in sentence :
                comScWord.append(word)
            for a in filteredList :
                PComSc.append(a.lower())
        typeList.append((f,typeText))
    
        del sentence[:]
        del filteredList[:]
        
    def submitCheck(self):
        if checkLoad ==[] and checkLink ==[] :
            print "Empty"
        if checkLoad !=[] and checkLink ==[]:
            self.submitLoad()
        if checkLoad ==[] and checkLink !=[]:
            self.submitLink()
        if checkLoad !=[] and checkLink !=[] :
            self.submitAll()
    def showResult(self):
        if enterInput.checkSubmit ==False :
            a= enterInput.linkCount + enterInput.pdfCount + enterInput.txtCount + enterInput.htmlCount
            self.typeResult()
            print "================================================================================"
            print " "
            print " "
            print " "
            print " "
            print "                         ====================================="
            print "                                  All document entered"
            print "                         ====================================="
            print "                                 %d      Link entered" %enterInput.linkCount
            print "                                 %d      PDF  entered" %enterInput.pdfCount
            print "                                 %d      TXT  entered" %enterInput.txtCount
            print "                                 %d      HTML entered" %enterInput.htmlCount
            print "                         ====================================="
            print "                                         RESULT               "
            print "                         ====================================="
            print " "
            print "                                 %d      ART document(s)       " %enterInput.artC
            print "                                 %d      COMPUTER SCIENCE  document(s) " %enterInput.comScC
            print " "
            print " "
            print " "
            print " "
            print "================================================================================"
            print typeList
            enterInput.checkSubmit =True
    def typeResult(self):
        for a,b in typeList:
            if b =='ART':
                enterInput.artC += 1
                
            else :
                enterInput.comScC +=1
                
    def submitAll(self):
        enterInput.checkSubmit =True
        self.submitLoad()
        self.submitLink()
        enterInput.checkSubmit =False
        self.showResult()
        
    def submitLoad(self):
        foundSymbol = 0
##        for a in allFile :
##        for a in loadTr :
##            self.wordToken(a,listWord)
##            
        for item in allFile:
            if self.checkEnd(item)=='pdf' :
                self.itsPDF(item)
            elif self.checkEnd(item)=='txt':
                self.itsTXT(item)
            elif self.checkEnd(item)=='html':
                self.itsHTML(item)
        self.showResult()
    def submitLink(self):   ### PRESS SUBMIT
            
            for link in getLink:
                        enterInput.linkCount += 1
##                        r = requests.get(link)
##                        r.content
##                        soup = BeautifulSoup(r.content,"lxml")
##                        g_data =soup.find_all("p")
##                        
                        g_data = self.pullText(link)
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
                            lower.append(a.lower())
                            wordCollect.append(a.lower())
                        
                        a = ' '.join(listWord)
                        b = ' '
                
                        savedWord = []
                        wordFreq = []

                        c = Counter(lower)
                        del listWord[:]
                        del newListWord[:]                   
                        del stemmedList[:]
                        del lower[:]
                        del uniToStr[:]
                        del savedWord[:]
                        del wordFreq[:]
                        artCount = 0
                        comScCount = 0
                        for a in sentence :
                            if (s.sentiment(a))=="art" : ## check type for each sentence
                                artCount = artCount +1
                            else :
                                comScCount = comScCount +1

                        allType = artCount + comScCount  ## calculate all word numbers
                        artPercent = float((float(artCount)/float(allType)))*100
                        comScPercent = float((float(comScCount)/float(allType)))*100
                        
                        if artPercent > comScPercent : 
                            typeText = "ART"        ## if number of art sentence > com then it's ART
                            for word in sentence :
                                artWord.append(word)
                            for a in filteredList :
                                PArt.append(a.lower())
                        else :
                            typeText = "COMPUTER SCIENCE" ## if not its COM
                            for word in sentence :
                                comScWord.append(word)
                            for a in filteredList :
                                PComSc.append(a.lower())
                        typeList.append((link,typeText))
                    
                        del sentence[:]
                        del filteredList[:]
                
##            save_typeList = open("data_input/typelist.pickle","wb")
##            pickle.dump(typeList, save_typeList) ## save link and type to pickle for future usage
##            save_typeList.close()
            self.showResult()
app = SeaofBTCapp()

app.mainloop()

print "Program Closed"


'''
http://www.shmoop.com/game-of-thrones-book/summary.html
https://docs.python.org/2/library/array.html
http://www.themoviespoiler.com/2016Spoilers/Deadpool.html
https://en.wikipedia.org/wiki/Network_analysis_(electrical_circuits)
http://edition.cnn.com/2016/02/25/asia/afghanistan-war-analysis/index.html
http://www.bbc.com/news/election-us-2016-35662202
http://www.bangkokpost.com/learning/learning-from-news/876440/nok-chief-admits-pilots-have-quit-normal-he-says
https://www.yahoo.com/katiecouric/jane-sanders-on-bernie-sanders-campaign-for-210337939.html
http://www.telegraph.co.uk/news/science/science-news/12173317/Sperm-grown-in-lab-could-allow-infertile-men-to-have-children.html
https://www.sciencedaily.com/releases/2016/02/160224231734.htm
http://www.calacademy.org/explore-science/new-discoveries-a-famous-tarantula-and-a-cheating-plant


    
        
'''


'''
https://en.wikipedia.org/wiki/Art
https://en.wikipedia.org/wiki/Sculpture
https://en.wikipedia.org/wiki/Plastic_arts
https://en.wikipedia.org/wiki/Ceramic_art
https://en.wikipedia.org/wiki/Pottery
https://en.wikipedia.org/wiki/Image_processing
https://en.wikipedia.org/wiki/Digital_image_processing
https://en.wikipedia.org/wiki/Digital_signal_processing
https://en.wikipedia.org/wiki/Digital_signal_controller
https://en.wikipedia.org/wiki/Microcontroller
https://en.wikipedia.org/wiki/Clock_rate
https://en.wikipedia.org/wiki/Multi-core_processor
https://en.wikipedia.org/wiki/Integrated_circuit
https://en.wikipedia.org/wiki/Electronic_component
https://en.wikipedia.org/wiki/Buzzer
'''
