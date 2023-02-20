import re
import pymorphy2
from nltk.corpus import stopwords

morph = pymorphy2.MorphAnalyzer()
ru_stopwords = stopwords.words('russian')
ru_stopwords += ['это', 'свой', 'который', 'ваш', 'наш']

with open('go_to_Sirius.csv', encoding="utf-8") as f:
    f.readline()
    i = 0
    dict_words = {}
    lst_count = []
    dict_count = {1: 0}

    for line in f:
        line = line.strip()
        russian_word = r'[а-ёЁ-Я]+'
        a = re.findall(russian_word, line)

        for word in a[2:]:
            word = word.lower()
            word = morph.parse(word)[0].normal_form
            if word not in ru_stopwords and len(word) > 1:
                if word not in dict_words:
                    dict_words[word] = 1
                    dict_count[1] += 1
                else:
                    dict_words[word] += 1
                    if dict_words[word] not in lst_count:
                        lst_count += [dict_words[word]]

                    if dict_count[dict_words[word] - 1] == 1:
                        del dict_count[dict_words[word] - 1]
                        ind = lst_count.index(dict_words[word] - 1)
                        del lst_count[ind]
                    else:
                        dict_count[dict_words[word] - 1] -= 1

                    if dict_words[word] in dict_count:
                        dict_count[dict_words[word]] += 1
                    else:
                        dict_count[dict_words[word]] = 1


lst_count.sort()

if len(lst_count[::-1]) > 100:
    lst_count = lst_count[::-1]
    lst_count = lst_count[0:100]

lst_count_new = []

for count in lst_count:
    if len(lst_count_new) == 100:
        break
    for key, value in dict_words.items():
        if len(lst_count_new) == 100:
            break
        if value == count:
            lst_count_new += [key]
            res = [key, count]

# print(lst_count_new, len(lst_count_new))
open('result_task_Kuzmina.txt', 'w', encoding='utf-8').writelines("\n".join(lst_count_new))



