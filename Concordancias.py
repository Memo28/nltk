import nltk
from nltk.stem.snowball import SnowballStemmer

class Searcher(object):

    #Leemos el archivo proveniente de la interfaz
    def readFile(self,path):
        with open(path,"r") as archivo:
            texto = archivo.read()
        return texto

    def searchConc(self,path,word):
        root = self.searchConcordanceRoot(path,word)
        word = self.searConcordanceWord(path,word)
        return self.joinResult(root,word)

    #Bucamos las cooncordancias de la palabra como tal
    def searConcordanceWord(self,path,word):
        text = self.readFile(path)
        results = self.get_all_phrases_containing_tar_wrd(word, text,5,5)

        info = ""
        for result in results:
            info = info + result + '\n'

        return info

    #Bucamos las cooncordancias en la raiz de la palabra
    def searchConcordanceRoot(self,path,word):
        text = self.readFile(path)
        word = self.getRoot(word)
        print(word)
        results = self.get_all_phrases_containing_tar_wrd(word, text,5,5)

        info = ""
        for result in results:
            info = info + result + '\n'

        return info

    #Unimos los resultados en una sola lista y obtenemos un set() que casteamos a str() para poder
    #hacer el split en la interfaz y mostrar los datos de manera "ordenada"
    def joinResult(self,rWord,rRoot):
        rWordSplit = rWord.split('\n')
        rRootSplit = rRoot.split('\n')

        join = str(set().union(rWordSplit,rRootSplit))
        return join

    #Obtenemos la raiz de la palabra con el Lemmatizer del nltk
    def getRoot(self,word):
        root = SnowballStemmer("spanish")
        return root.stem(word)


    #Metodo que obtiene las cooncordacias
    def get_all_phrases_containing_tar_wrd(self,target_word, tar_passage, left_margin, right_margin):

        tokens = nltk.word_tokenize(tar_passage)
        text = nltk.Text(tokens)
        c = nltk.ConcordanceIndex(text.tokens,key = lambda s:s.lower())
        concordance_txt = ([text.tokens[list(map(lambda x: x - 5 if (x - left_margin) > 0 else 0, [offset]))[0]:offset + right_margin]
                            for offset in c.offsets(target_word)])
        return [''.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]

