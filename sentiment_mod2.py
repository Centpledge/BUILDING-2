#File: sentiment_mod.py

import nltk
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


documents_f = open("pickled_algos/documents2.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open("pickled_algos/word_features5k2.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



open_file = open("pickled_algos/originalnaivebayes5k2.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()






voted_classifier = VoteClassifier(
                                  classifier
                                  )


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats)

def showWord():
    classifier.show_most_informative_features(200)

def acc():
    print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)

##,voted_classifier.confidence(feats)
