import string
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist
# import nltk
#
#
# f = open('go_to_Sirius.txt', "r", encoding="utf-8")
# text = f.read()
# text = text.lower()
#
# print(string.punctuation)
# spec_chars = string.punctuation + '\n\xa0«»\t—…'
# text = "".join([ch for ch in text if ch not in spec_chars])
# def remove_chars_from_text(text, chars):
#     return "".join([ch for ch in text if ch not in chars])
#
# text = remove_chars_from_text(text, spec_chars)
# text = remove_chars_from_text(text, string.digits)
#
#
# nltk.download('stopwords')
#
# import pymorphy2
# from nltk.corpus import stopwords
# morph = pymorphy2.MorphAnalyzer()
# ru_stopwords = stopwords.words('russian')
# digits = [str(i) for i in range(10)]
# def preprocess(tokens):
#     return [morph.normal_forms(word)[0]
#             for word in tokens
#                 if (word[0] not in digits and
#                     word not in ru_stopwords)]

# text_tokens = nltk.word_tokenize(text)
# #
# text = nltk.Text(text_tokens)
#
# fdist = FreqDist(text)
#
# print(fdist)
#
# russian_stopwords = stopwords.words("russian")
#
# russian_stopwords.extend(['это', 'нею'])

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# matplotlib inline
#
# text_raw = " ".join(text)
#
# wordcloud = WordCloud().generate(text_raw)

import pymorphy2
from nltk.corpus import stopwords
morph = pymorphy2.MorphAnalyzer()
ru_stopwords = stopwords.words('russian')
# digits = [str(i) for i in range(10)]
# def preprocess(tokens):
#     return [morph.normal_forms(word)[0]
#             for word in tokens
#                 if (word[0] not in digits and
#                     word not in ru_stopwords)]
#
# print(ru_stopwords)
# from pyspark.sqk.types import ArrayType, StringType
#
# preprocess_udf = F.udf(preprocess, ArrayType(StringType()))
# df = df.withColumn('finished', preprocess_udf('tokens'))
line = ['мы', 'ее', 'между', 'собой', 'но', 'что', 'по', 'снова', 'там', 'о', 'однажды', 'вне', 'очень', 'иметь', 'с',
        'они', 'свой', 'самой', 'или', 'ему', 'каждому', 'тому', 'за', 'самим', 'до', 'ниже', 'мы', 'эти', 'ваши', 'его'
        , 'до', 'не', 'ни', 'же', 'только', 'вам', 'бы', 'этот', 'при', 'которые',  'я', 'были', 'ее', 'больше', 'это',
        'вниз', 'должен', 'их', 'пока', 'выше', 'оба', 'вверх', 'уже', 'кто', 'вас', 'нас', 'еще', 'этом', 'чем', 'того',
        'до', 'наш', 'имел', 'она', 'все', 'нет', 'когда', 'в', 'любое', 'до', 'им', 'и', 'был', 'имейте', 'в', 'будет',
        'на', 'делает', 'вы', 'тогда', 'тот', 'над', 'почему', 'так', 'может', 'сделал', 'не', 'сейчас', 'под', 'он',
        'ты', 'сама', 'имеет', 'просто', 'где', 'тоже', 'только' 'который', 'те', 'я', 'после', 'несколько', 'кого',
        'бытие', 'если', 'их', 'мое', 'против', 'a', 'делать', 'это', 'как', 'дальше', ' было', 'здесь', 'то', 'а',
        'для', 'к', 'из', 'от', 'у', 'также', 'том', 'мне', 'ведь', 'поэтому', 'свои', 'своих', 'через', 'нам']
res_line = []
for word in line:
    res_line.append(morph.parse(word)[0].normal_form)


print(res_line)
open('./pymorphy2.txt', 'w', encoding='utf-8').writelines("\n".join(res_line))
