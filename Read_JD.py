# Import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize, punkt
from nltk.corpus import stopwords

# Read the file
df = pd.read_csv('./JD.csv')

# Keep the column we are interested
df = df['Job Descriptions']

# Turn the list of Job Descriptions into a string of words
all_words = ' '.join(df)

# Split the words with word_tokenize and save as a list of words
word_list = word_tokenize(all_words)

# Remove meaningless words, words containing numbers and punctuations, then save as a list
stop_words = set(stopwords.words('english'))
word_bag = []
for x in word_list:
    if x.isalpha() and x.lower() not in stop_words:
        word_bag.append(x)

# Remove duplicated words and save as a list
word_bag_unique = list(dict.fromkeys(word_bag))

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(word_bag_unique)
r = pd.DataFrame(vectors.toarray(),columns=vectorizer.get_feature_names_out())
r.to_csv('TFIDF.csv')

pass
