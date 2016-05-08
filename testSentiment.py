import sentiment_mod as s
import unittest 
a =(s.sentiment("computer science complete "))
print(s.sentiment("the art  rock is destined to be the 21st century's new " 'conan' " and that he's going to make a splash even greater than arnold schwarzenegger , jean-claud van damme or steven segal . l"))
print(s.sentiment("This art movie was awesome! The new acting was great, plot was so wonderful, and there were big pythons...so yea!"))
print(s.sentiment("This movie was utter junk. There were absolutely bad. I don't see what the point was at all. Horrible movie, 0/10 "))
print(s.sentiment("i love microcomputer assymbly "))
print(s.sentiment("The term hardware covers all of those parts of a computer that are tangible objects. Circuits, displays, power supplies, cables, keyboards, printers and mice are all hardware."))
print(s.sentiment("complete computer assymbly "))
print(s.sentiment("computer science complete "))
print(s.sentiment("Drawing is a means of making an image, using any of a wide variety of tools and techniques. "))
print a

s.showWord()



