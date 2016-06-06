import nltk
import unicodedata
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import datetime
from unidecode import unidecode
from nltk.corpus import stopwords


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
    
sArt = open("short_reviews/art_4.txt","r").read() ## open art text
sCom = open("short_reviews/com_4.txt","r").read() ## open com text

# move this up here
all_words = []
documents = []
stop = stopwords.words('english')
allowed_word_types = ["J"]


#  j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
##allowed_word_types = ["J"]
print "start"
print datetime.datetime.now()
print " "

a1 = (sArt.decode('unicode_escape').encode('ascii','ignore'))
for p in a1.split('\n'):

    documents.append( ((p), "art") ) ## split each word then tag "art"
    try :
        words = word_tokenize(p)
        pos = nltk.pos_tag(words)
        for w in pos:
            
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())
                
##        pos = nltk.pos_tag(words)
##        for w in pos:
##            if w[1][0] in allowed_word_types:
##                all_words.append(w[0].lower())
        
    except :
        pass
print "art completed"
print datetime.datetime.now()
a2 = (sCom.decode('unicode_escape').encode('ascii','ignore'))
for p in a2.split('\n'):
##    print p
    documents.append( (p, "comSc") ) ## split each word then tag "comSc"
    try :
        words = word_tokenize(p)
        pos = nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())
            
##        pos = nltk.pos_tag(words)
##        for w in pos:
##            if w[1][0] in allowed_word_types:
##                all_words.append(w[0].lower())
    except :
        pass
print "com completed"
print datetime.datetime.now()


save_documents = open("pickled_algos/documentsFinal.pickle","wb")
pickle.dump(documents, save_documents) ## save to pickle
save_documents.close()


all_words = nltk.FreqDist(all_words)


word_features = list(all_words.keys())[:1250]
wordDE = []

save_word_features = open("pickled_algos/word_features5kFinal.pickle","wb")
pickle.dump(word_features, save_word_features) ## save to pickle
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
print "findfeature compted"
print(len(featuresets))

testing_set = featuresets[20000:]
training_set = featuresets[:20000]


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(100)

save_classifier = open("pickled_algos/originalnaivebayes5kFinal.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
print datetime.datetime.now()

