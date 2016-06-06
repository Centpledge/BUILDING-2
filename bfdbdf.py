features = {}
word_features = ['a','b','gsdfdsf','asdasdas']
for w in word_features:
            features[w] = (w in words)
print features
