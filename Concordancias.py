import nltk

director_name = "C:\\Users\\Memo Vara De Gante\\Practicas\\"
file_name = "bitcon.txt"

with open(director_name+file_name,"r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")
texto_nltk = nltk.Text(tokens)
texto_nltk.similar("bit")
print()
texto_nltk.concordance("bitcoin",200,200)