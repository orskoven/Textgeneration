from nltk.stem import WordNetLemmatizer, PortStemmer
import pandas as pd

lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()

words = 'swimmer swimming swim swims swam swum'.split(' ')

words= 'wait waiting waited waits'.split(' ')

wls = [(word, lemmatizer.lemmatize(word), porter_stemmer.stem(word)) for word in words]

df = pd.DataFrame(wls, columns=['word', 'lemma', 'stem'])
df

# We get simpler form of words
# many of these repesent the same (WORD)?
# help simplify copus in nlp
# makes easier to analyse 

# widely used in search and databases, 
# can greatly enahance the chance of. finding a good match for a word

