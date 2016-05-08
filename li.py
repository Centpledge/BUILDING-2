import Tkinter as tk
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

def cbc(id, tex):
    return lambda : callback(id, tex)

def callback(id, tex):
    s = 'At {} f is {}\n'.format(id, id**id/0.987)
    tex.insert(tk.END, s)
    tex.see(tk.END)             # Scroll if necessary
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

class enterInput(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            app = tk.Tk()
            tex = tk.Text(master=app)
            ##addLinkButton0 = tk.Button(tex,text = "Add Link",width = 60).pack()
            tex.pack(side=tk.LEFT)

            bop = tk.Frame()
            bop.pack(side=tk.RIGHT)
            ##for k in range(1,10):
            ##    tv = 'Say {}'.format(k)
            ##    b = tk.Button(bop, text=tv,width=60, command=cbc(k, tex))
            ##    a= tk.Label(bop,text=" ")
            ##    a.pack()
            ##    b.pack()
            space0=tk.Label(bop,text=" ").pack()
            ent = tk.Entry(bop,width=60).pack()
            addLinkButton = tk.Button(bop,text = "Add Link",width = 60,command=cbc(1,tex)).pack()
            OpenButton = tk.Button(bop,text = "Open File",width = 60).pack()
            submitButton = tk.Button(bop,text = "Submit Button",width = 60).pack()
            space1=tk.Label(bop,text=" ").pack()
            histogramGroup = tk.Label(bop,text = "Histogram",width = 60).pack()
            allGraph = tk.Button(bop,text = "All Graph",width = 60).pack()
            comScGraph = tk.Button(bop,text="Computer Science Graph",width  =60).pack()
            artGraph = tk.Button(bop,text="Art Graph",width=60).pack()
            space2=tk.Label(bop,text=" ").pack()
            wordCloudGroup = tk.Label(bop,text="WordCloud",width=60).pack()
            allWordCloud = tk.Button(bop,text = "All WordCloud",width=60).pack()
            comScWordCloud = tk.Button(bop,text = "ComputerScience",width=60).pack()
            artWordCloud = tk.Button(bop,text = "Art",width=60).pack()
            a=tk.Label(bop,text=" ").pack()
            tk.Button(bop,width = 30, text='Exit', command=app.destroy).pack()
            space9 = tk.Label(bop,text = " ",width=60).pack()
        def p (self):
            print "3i3i"
app = SeaofBTCapp()
app.mainloop()
