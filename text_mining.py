from Tkinter import *
import csv
import sentiment_mod as s
import Tkinter as tk
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
ent = ""
notCount= ["a","is","the","for","and",';',':','(',')','[',']','{','{','}','is','am','are',
        'the','an','his','her','him','your','you','we','they','it','its','he','?','!',
        '.','this','that','these','those','of','to',',','in','``',"''",'He',"n't",
        'are','not','with','on','in','^','or','A','as','-','&','same','1','thi','at',
        '2','3','4','5','6','7','8','9','0','m.','so','/','It','=','<','>','but',
        'a','b','c','d','e','f','g','h','i','I','j','k','l','m','y','_','+',"'s",'hi',
        'from','by',' as','be','form','may','have','has','which','pp','The',
        "'",'w.','d.','so','So','!','ha','she','She']

##class Html(object) :
##    linkCount = 0
##    def __init__(self):
##        self.low = []
##        self.filteredList = []
##        self.stemmedList = []
##        self.listWord = []
##        self.link = ""
##        self.word = []
##        self.frequency = []
##        Html.linkCount += 1
##        
##
##    def displayCount(self):
##        print "Total links %d" %Html.linkCount
##
##    def linkSet(self,setlink):
##        self.link = setlink
##    def displayLink(self):
##        print self.link
##
##    def writeCSV(self):
##        
##        with open('eiei.csv', 'w') as csvfile:
##            a = Counter(self.low)
##            fieldnames = ['Address','1st', '2nd','3rd','4th','5th']
##            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##            writer.writeheader()
##            for item in tupleList:
##                
##                writer.writerow({'Address': item[0], '1st': item[1], '2nd': item[2], '3rd':item[3],'4th':item[3],'5th':item[4]})
##                image = Image.new("RGBA", (450,250), (0,0,0))
##                draw = ImageDraw.Draw(image)
##                biggest = ImageFont.truetype("angsau", 100)
##                med = ImageFont.truetype("angsau", 50)
##                draw.text((0, 0),item[1],(255,255,255),font=biggest)
##                draw.text((100, 100),item[2],(255,255,255),font=med)
##                img_resized = image.resize((188,45), Image.ANTIALIAS)
##                image.save("aaaa.png","PNG")
##                image.show()
##
##            
##    def wordSet(self):
##        r = requests.get(self.link)
##        r.content
##        soup = BeautifulSoup(r.content,"lxml")
##        g_data = soup.find_all("p")
##        foundSymbol = 0
##        for a in g_data :
##                
##                    for b in word_tokenize(a.text):
##                        self.listWord.append(b)         
##
##        for a in self.listWord:
##            self.stemmedList.append(ps.stem(a))
##
##
##        for a in self.stemmedList : 
##            for b in notCount :
##                if a==b:
##                    foundSymbol = 1
##            if foundSymbol !=1:      
##                self.filteredList.append(a)
##
##                foundSymbol = 0
##            foundSymbol = 0
##
##        for a in self.filteredList :
##            self.low.append(a.lower())
##        
##        a = ' '.join(self.low)
##        print a 
##        counts = Counter(self.low)
##        counts2 = Counter(self.listWord)
##  
##        savedWord = []
##        wordFreq = []
##        
##
##        c = Counter(self.low)
##
##    def displayWord (self):
##           print self.word
##    def createTuple(self):
##        a = Counter(self.low)
##        for i in getLink :
##            self.tup = tuple([self.link] + a.most_common(5))
##            tupleList.append(self.tup)
##




class App(object):  ### program window
    
   
    def __init__(self,master = None ):
        
        self.root = Tk()
        a = self.root
        self.low = []
        self.filteredList = []
        self.stemmedList = []
        self.listWord = []
        self.link = ""
        self.word = []
        self.frequency = []

        self.root.geometry("525x250")
        self.root.wm_title("Text Mining")
        load = Image.open('background.png')
        render = ImageTk.PhotoImage(load)
        self.img = Label(image=render)
        self.img.image = render
        self.img.place (x=0,y=0)

        subbutton = tk.Button(self.root, text="SUBMIT",width = 30, command=self.submitLink)
        delbutton = tk.Button(self.root, text="DELETE ALL",width = 30, command=self.delAllList)
        popbutton = tk.Button(self.root, text="DELETE Lastest link",width = 30, command=self.delLastList)
        a.bind('<Return>', self.func)
        w = Label(self.root, text="Paste a link in the entry then press ENTER")
        ww = Label(self.root, text="After you entered all links click SUBMIT")
        w.pack()
        ww.pack()
        ent = Entry(self.root,width = 45)
        ent.pack()
        all_entries.append( ent )
        subbutton.pack()
        popbutton.pack()
        delbutton.pack()
        self.root.mainloop()
    def func(self,event):
        global ent
##        print("You hit return.")
        for number, ent in enumerate(all_entries):
            if len(ent.get()) == 0:
                    print "this entry is  empty"    ## check if entry is empty or not
                
                   
            else:
                allLinks = open("data_input/links.pickle","wb") ## if not empty then dump all links
                pickle.dump(ent.get(), allLinks)
                allLinks.close()

                splitLink = ent.get().split() ## split each links
                
                print "ADD  " + ent.get()  ## print all added links
                print splitLink
                for item in splitLink :
                    getLink.append(item)   ## append splited links in to getLink
                    ent.delete(0, 'end')   ##
                print getLink
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
    def delLastList(self):     ### delete last index
        if len(getLink) == 0:
            print "EMPTY"
        else:
            getLink.pop()   ## if not deletd last index

    def submitLink(self):   ### PRESS SUBMIT

         with open('output.csv', 'w') as csvfile:   ### SAVE TO CSV
            a = Counter(self.low)
            fieldnames = ['Address','1st', '2nd','3rd','4th','5th']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for link in getLink:
                        r = requests.get(link)
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
                            lower.append(a.lower())
                        
                        a = ' '.join(listWord)
                        b = ' '
##                        print a
##                        wordcloud = WordCloud().generate(a)
##                        
##                        counts = Counter(lower)
##                        counts2 = Counter(listWord)
##                        plt.imshow(wordcloud)
##                        plt.axis("on")
                        
##                        plt.imshow(wordcloud)
                        
                  
                        savedWord = []
                        wordFreq = []
                        

                        c = Counter(lower)
##                        text = g_data
##                        wordcloud = WordCloud().generate(g_data)
##                        wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
##                        plt.figure()
##                        plt.imshow(wordcloud)
##                        plt.axis("on")
##                        plt.show()
##                        
                        self.tup = tuple([link] + c.most_common(10))
                        tupleList.append(self.tup)
                        
##                        plt.show()
                        del listWord[:]
                        del newListWord[:]
                        del filteredList[:]
                        del stemmedList[:]
                        del lower[:]
                        del uniToStr[:]
                        del savedWord[:]
                        del wordFreq[:]
            print tupleList
            print sentence
##                        wordcloud = WordCloud().generate(b)
            
##            for item in tupleList:      
##                writer.writerow({'Address': item[0], '1st': item[1], '2nd': item[2], '3rd':item[3],'4th':item[4],'5th':item[5]})
####            for item,count in c.most_common(3):
##                    image = Image.new("RGBA", (600,250), (0,0,0))
##                    draw = ImageDraw.Draw(image)
##                    biggest = ImageFont.truetype("angsau", 100)
##                    med = ImageFont.truetype("angsau", 50)
##                    draw.text((0, 0),item[1],(255,255,255),font=biggest)
##                    draw.text((100, 100),item,(255,255,255),font=med)
##                    img_resized = image.resize((188,45), Image.ANTIALIAS)
##                    image.save("aaaa.png","PNG")
            imgWidth = 600
            imgHeight = 250
            xPoint = 0
            yPoint = 0
            num = 0
            for item,count in c.most_common(5):
                    wcText.append(str(item))
##            print wcText
            image = Image.new("RGBA", (imgWidth,imgHeight), (0,0,0))
            draw = ImageDraw.Draw(image)
            biggest = ImageFont.truetype("angsau", 65)
            med = ImageFont.truetype("angsau", 50)
            small =  ImageFont.truetype("angsau", 25)
            smallest = ImageFont.truetype("angsau", 20)
##            for rank in wcText:
##                if yPoint > imgHeight -50 :
##                    yPoint = imgHeight
##                    xPoint = xPoint + 75
##                if num >2 :
##                    font = med
##                elif num >5 :
##                    font = small
##                elif num >8 :
##                    font = smallest
##                else :
##                    font = biggest
##                draw.text((xPoint,yPoint),rank,(255,255,255),font)
####                xPoint = xPoint + 20
##                yPoint = yPoint + 40
##                num = num +1
##            draw.text((xPoint,yPoint),wcText[0],(255,255,255),font=biggest)
##            draw.text((50, 50),wcText[1],(255,255,255),font=med)
##            draw.text((100, 100),wcText[2],(255,255,255),font=small)
##            draw.text((150, 150),wcText[3],(255,255,255),font=small)
##            draw.text((200, 200),wcText[4],(255,255,255),font=smallest)
##            draw.text((250, 250),wcText[5],(255,255,255),font=smallest)
##            draw.text((300, 300),wcText[6],(255,255,255),font=smallest)
##            draw.text((300, 150),wcText[7],(255,255,255),font=smallest)
##            draw.text((200, 200),wcText[8],(255,255,255),font=smallest)
##            draw.text((200, 200),wcText[9],(255,255,255),font=smallest)
            
            
                
##            img_resized = image.resize((188,45), Image.ANTIALIAS)
##            image.save("aaaa.png","PNG")
##            image.show()
##        



##    def showEntries(self):
##  
##        for number, ent in enumerate(all_entries):
##
##            if len(ent.get()) == 0:
##                print "this entry is  empty"
##            
##                
##            else:
##                print ""
##                print "From this link  >>>> " + ent.get()
##                
##                r = requests.get(ent.get())
##                r.content
##                soup = BeautifulSoup(r.content,"lxml")
##                g_data =soup.find_all("p")
##                foundSymbol = 0
##
##                for sent in sent_tokenize(g_data) :
##                    sentence.append(str(sent))
##                print sentence
##                    
##                for a in g_data :
##                
##                    for b in word_tokenize(a.text):
##                        listWord.append(b)
##
##
##                for a in listWord:
##                    stemmedList.append(ps.stem(a))
##
##
##                for a in stemmedList : 
##                    for b in notCount :
##                        if a==b:
##                            foundSymbol = 1
##                    if foundSymbol !=1:      
##                        filteredList.append(a)
##
##                        foundSymbol = 0
##                    foundSymbol = 0
##
##                for a in filteredList :
##                    lower.append(a.low())
##                
##                
##                counts = Counter(low)
##                counts2 = Counter(listWord)
##          
##                savedWord = []
##                wordFreq = []
##                
##
##                c = Counter(low)
##            
##            

App()






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
