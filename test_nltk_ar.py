import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('treebank')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk.corpus import treebank
import string

f=open("text2.txt",'r',encoding="utf-8")
text=f.read()
print(text)
print("\ntext\n\n\n")



text_words=word_tokenize(text)
print(text_words)
print("\ntextwords\n\n\n")

sw = stopwords.words('arabic')
print(sw)
print("\n\n\n")
tokens=[i for i in text if not i in sw]
print(tokens)
print("\ntokens\n\n\n")

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in text_words]
print(stemmed)
print("\nstemmed\n\n\n")
print(text_words==tokens)
