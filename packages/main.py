import numpy as np
import pickle as pk
import os
from config import Config
from ngram import Ngram


config = Config()
n_gram = 2

models = dict()


# Train one model per language
for file_name in os.listdir(config.langPath):
    if file_name.__contains__(".txt"):
        model_name = file_name[:-4]
        if os.path.isfile("{0}/{1}/{2}".format(config.modelsPath, n_gram, file_name)):
            with open("{0}/{1}/{2}".format(config.modelsPath, n_gram, file_name), 'rb') as model_file_handler:
                models[model_name] = pk.load(model_file_handler)
        else:
            with open("{0}/{1}".format(config.langPath, file_name),'rt') as file_handler:
                buffer = file_handler.readlines()
                buffer = " ".join(buffer)
                print(model_name)
                model = Ngram(buffer, n_gram)
                with open("{0}/{1}/{2}".format(config.modelsPath, n_gram, file_name), 'wb') as model_file_handler:
                    pk.dump(model, model_file_handler)
                models[model_name] = model


#Test

wrong_list = []
true_positive = 0
counter = 0
with file(config.testPath, 'rt') as test_file_handler:
    buffer = test_file_handler.readlines()
    for txt in buffer:
        txt_splitted = txt.split("\t")
        true_lang = txt_splitted[1].replace("\n", "")
        # if true_lang == "xx":
        #     continue
        test_buffer = txt_splitted[0]
        max_score = 0
        max_lang = ""
        for lang in models.keys():
            score = models[lang].score(test_buffer)
            if score > max_score:
                max_lang = lang
                max_score = score
        print(true_lang, max_lang, max_score)
        if true_lang == max_lang:
            true_positive += 1
        else:
            wrong_list.append(true_lang + "-" + max_lang)
        counter += 1
        # if len(wrong_list) > 10:
        #     break

print(true_positive, counter, 1.0 * true_positive / counter)
uniques = np.unique(wrong_list, return_counts=True)
print(zip(uniques[0], uniques[1]))

# max_score = 0
# max_lang = ""
# for lang in models.keys():
#     score = models[lang].score(test_buffer)
#     if score > max_score:
#         max_lang = lang
#         max_score = score

# print(max_lang, max_score)

#2 864
#2 138 * 00000000.1
#2 249 * 000.1
#2 53 /2
#2 13074 out of 28000
# (13074, 26000)
# (21014, 26000)
# (20957, 26000)
# (21035, 26000)
# (21041, 26000)
#(21053, 26000)


