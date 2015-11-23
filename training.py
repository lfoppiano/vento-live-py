import nltk
import sys
import os
from nltk.sentiment import SentimentAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.util import *

if len(sys.argv) == 2:
    trainingDataDirectory = sys.argv[1]
else:
    print("Usage: python training.py trainingDataDirectory")
    sys.exit(-1)

analyzerFileName = "analyzer.bin"
data = dict()

for dir, subDir, files in os.walk(trainingDataDirectory):
    print("Processing files in " + trainingDataDirectory + ". ")
    for file in files:
        if file.endswith(".csv"):
            path = dir + "\\" + file
            print("Processing file " + path)
            with open(path, 'r', encoding='utf-8') as f:
                print("\t file: " + path)
                # for line in f:
                #     tokens = nltk.word_tokenize(str(line))

                data[file] = ([(nltk.word_tokenize(str(line)), file.split('.')[0]) for line in f])


# Prepare training/test data

def dump(classifier, filename):
    f = open(filename, 'wb')
    pickle.dump(classifier, f, -1)
    f.close()


def restore(filename):
    f = open(filename, 'rb')
    loaded = pickle.load(f)
    f.close()
    return loaded


trainingData = []
testData = []

for key in data.keys():
    trainingDataRate = round(len(data[key]) * 0.8)
    trainingData.extend(data[key][0:trainingDataRate])
    testData.extend(data[key][trainingDataRate:(len(data[key]) - 1)])

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in trainingData])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(trainingData)
test_set = sentim_analyzer.apply_features(testData)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
dump(sentim_analyzer, analyzerFileName)


for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))


sentim_analyzer.classifier.most_informativeWords



