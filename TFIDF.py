# Import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize, punkt
from nltk.corpus import stopwords

# Read the file
df = pd.read_csv('./JD.csv')

# Keep the column that we are interested
df = df['Job Descriptions']

# Turn the list of Job Descriptions into a string of words
word_list = df.values.tolist()

# Remove meaningless words, words containing numbers and punctuations
stop_words = set(stopwords.words('english'))
for x in range(len(word_list)):
    word_bag = []
    temp = word_tokenize(word_list[x])
    for y in temp:
        if y.isalpha() and y.lower() not in stop_words:
            word_bag.append(y.lower())
    word_list[x] = ' '.join(word_bag)

# Compute TFIDF and save as a csv file
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(word_list)
r = pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names_out())
r.to_csv('TFIDF.csv')

pass
