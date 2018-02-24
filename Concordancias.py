import nltk

class Searcher(object):

    def ReadFile(self,path):
        director_name = path
        with open(path,"r") as archivo:
            texto = archivo.read()
        return texto

    def searchConc(self,path):
        text = self.ReadFile(path)
        results = self.get_all_phrases_containing_tar_wrd('bloques', text,5,5)

        info = ""
        for result in results:
            info = info + result + '\n'
        return info

    def get_all_phrases_containing_tar_wrd(self,target_word, tar_passage, left_margin, right_margin):

        tokens = nltk.word_tokenize(tar_passage)
        text = nltk.Text(tokens)
        c = nltk.ConcordanceIndex(text.tokens,key = lambda s:s.lower())
        concordance_txt = ([text.tokens[list(map(lambda x: x - 5 if (x - left_margin) > 0 else 0, [offset]))[0]:offset + right_margin]
                            for offset in c.offsets(target_word)])
        return [''.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]

