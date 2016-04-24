import matplotlib
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
import nltk
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
savedWord = []

import codecs
f=codecs.open("raspTest.html", 'r')
##a = f.read()
##print a
##soup = BeautifulSoup.get_text(a)
##print soup
##g_data = soup.find_all("p")
##raw = nltk.clean_html(a)
##print raw
##print g_data

##from bs4 import BeautifulSoup
##with open("raspTest.html") as markup:
##    soup = BeautifulSoup((markup.read()),"lxml")
##    print soup


##import html2text
##html = open("raspTest.html").read()
##print html2text.html2text(html)
##a =  f.read()
##soup = BeautifulSoup(a)
##g_data = soup.find_all("p")
##print g_data.get_text()
soup = BeautifulSoup(f,'html.parser')
##print soup.prettify()
print soup.get_text()
