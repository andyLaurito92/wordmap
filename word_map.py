import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("Word map generator")
parser.add_argument("file_name", help="The csv file name. The format of the csv should be frequency;word, where frequency is a number and word is a string.", type=str)
parser.add_argument("output", help="The output path", type=str)
args = parser.parse_args()
file_name = args.file_name
output_path = args.output

d = {}
general_words_to_remove = {"Multimedia", "omitido", "a", "de", "la", "el","las",
                           "del", "d", "www", "le", "q", "que", "los", "es", "en", "pero",
                           "una", "me", "y", "https", "m", "A", "t", "O", "ac", "ana", "al", "lo"
                            "un", "con", "Le", "os", "Q", "su", "ni", "est", "lo", "un", "M", "esa",
                            "ese", "aca", "En", "Esta", "hab", "S", "O", "c", "n", "s", "as", "mi",
                            "com", "As", "da", "Los", "les", "ar", "O", "do", "Ah", "Por", "sin",
                            "mes", "xq", "Un", "hs", "otra", "esta", "ahi", "all", "para", "Hay",
                            "elimin", "Que", "X", "despu", "aa", "Me", "0", "muy", "Lo", "tu",
                            "son", "mas", "eso", "an", "te", "nos", "Hasta", "vas", "mensaje",
                            "Eso", "este", "tan", "desde", "Aca", "Te", "mam", "porq", "donde",
                            "puede", "Es", "vez", "El", "De", "dos", "ella", "despues", "fue", "e"
                            "tener", "Pero", "sea", "menos", "Pero", "para", "por", "1", "l", "u"
                           "e", "qu", "nde", "pas", "u", "como", "otro", "cuando", "Est", "quer",
                           "C", "D", "sino", "dec", "e", "ahí", "Cómo", "Está", "él", "está", "Ma",
                           "más", "así", "había", "acá", "estás", "recién", "teneés", "día", "querés",
                           "tenía", "Qué", "quería", "qué", "Ahí", "dónde", "iba", "cómo", "Recién",
                           "Con", "digo", "dice", "tamb", "ir", "unos", "solo", "tener", "tiene", "anda",
                           "eh", "van", "Así", "tiempo", "Capaz", "quieras", "mí", "Tengo", "cosa",
                           "seguro", "tengo", "hasta", "ganas", "Voy", "Porque", "mismo", "Cuando", "Yo",
                           "dijo", "Estoy", "hace", "veo", "estar", "yo", "queda", "hora", "tomar",
                           "mando", "no", "No", "se", "Y", "y", "s", "si", "x", "X", "Se", "Como",
                           "eliminó", "Muy", "vos", "sus", "Para", "era", "Asi", "Vos", "Estamos",
                           "estamos", "nosotros", "tienen", "La", "vi", "va", "vamos", "medio", "decir",
                           "acuerdo", "Nos", "fui", "lugar"}
words_to_remove = {}
words_to_remove.update(general_words_to_remove)


df = pd.read_csv(file_name, sep=";", names=["quantity", "word"])
for index, row in df.iterrows():
    if row["word"] in words_to_remove:
        continue
    d[row["word"]] = float(row["quantity"])

# my_stopwords = set(stopwords.words('spanish', 'english'))
# my_stopwords.add("Andy")
# my_stopwords.add("Gaby")
# my_stopwords.add("Multimedia")
# my_stopwords.add("Schneider")
# print(my_stopwords)

# Generate a word cloud image
mywordcloud = WordCloud(width=800, height=800,
                        background_color="black",
                        #stopwords = my_stopwords,
                        min_font_size = 10).generate_from_frequencies(d) 

mywordcloud.to_file(output_path)

# Displaying the WordCloud                    
plt.figure(figsize = (10, 10), facecolor = None) 
plt.imshow(mywordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
