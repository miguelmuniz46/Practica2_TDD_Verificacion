import string
import operator
class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def count_words(args):
        vocales = [" a ", " e ", " i ", " o ", " u "]
        articulos = [" el ", " la ", " los ", " las ", " lo ", " un ", " uno ", " una ", " unos ", " unas "]
        preposiciones = [" pero ", " hacia ", " del ", " incluso ", " más ", " menos", " y ", " a ", " ante ", " bajo ", " cabe ", " con ", " contra ", " de ", " desde ", " durante ", " en ", " entre ", " hasta ", " mediante ", " para ", " por ", " según ", " sin ", " so ", " sobre ", " tras ", " versus ", " vía ", " excepto ", " salvo ", " además ", " cual ", " cuales "]
        pronombres = [" este ", " esta ", " esto ", " estos ", " estas ", " ese ", " esa ", " eso ", " esos", " esas ", " aquel ", " aquella ", " aquellos ", " aquellas ", " le ", " les ", " yo ", " me ", " mi ", "conmigo ", " tú ", " te ", " ti ", " contigo ", " usted ", " vos ", " él ", " se ", " sí ", " consigo ", " ella ", " ello ", " nosotros ", " nos ", " nosotras ", " vosotros ", " vosotras ", " os ", " ustedes "]
        puntuaciones = [",", ".", ";", ":", "-", "'", "*", "!", "¡", "?", "¿", "<", ">", '"', "[", "]", "{", "}", "(", ")",'"', '#', '%', '€', '$', '=']
        otros = [" que ", " de ", " al ", " su ", " sus "]
        listaStopwords = []

        listaStopwords.extend(vocales)
        listaStopwords.extend(articulos)
        listaStopwords.extend(preposiciones)
        listaStopwords.extend(pronombres)
        listaStopwords.extend(otros)

        args = " "+args.lower()+" "
        for punt in puntuaciones:
            args = args.replace(punt, "")

        for stopwords in listaStopwords:
            args = args.replace(stopwords, " ")

        palabras = args.split()
        dic = {}

        for palabra in palabras:
            numero_apariciones = 0

            for repetida in palabras:
                if(palabra in repetida):
                    numero_apariciones = numero_apariciones + 1

            dic[palabra] = numero_apariciones

        resultado = sorted(dic.items(), key=operator.itemgetter(1))
        resultado.reverse()


        return resultado