import numpy as np
import pickle as pk
import os
from config import Config
from ngram import Ngram


config = Config()
n_gram = 2

models = dict()

modelPath = config.models2Path
langPath = config.dataset2Path
testPath = config.test2Path

# Train one model per language
for file_name in os.listdir(langPath):
    if file_name.__contains__(".txt"):
        print(file_name)
        model_name = file_name[:-4]
        if model_name in ["xx"]:
            continue
        if os.path.isfile("{0}/{1}/{2}".format(modelPath, n_gram, file_name)):
            with open("{0}/{1}/{2}".format(modelPath, n_gram, file_name), 'rb') as model_file_handler:
                models[model_name] = pk.load(model_file_handler)
                models[model_name].revert_model()
        else:
            with open("{0}/{1}".format(langPath, file_name), 'rt') as file_handler:
                _buffer = file_handler.readlines()
                _buffer = " ".join(_buffer)
                print(model_name)
                model = Ngram(_buffer, n_gram)
                with open("{0}/{1}/{2}".format(modelPath, n_gram, file_name), 'wb') as model_file_handler:
                    pk.dump(model, model_file_handler)
                models[model_name] = model
        print('done')

print('learning done')
# Change models configuration
# for model_name in models:
#     models[model_name].limit_model(400)


#Test
wrong_list = []
test_buffer_len = []
true_positive = 0
counter = 0

s = 1
for file_name in os.listdir(testPath):
    print(file_name)
    true_lang = file_name[-2:]
    if true_lang in ["el", "gz", ".e"]:
        continue
    with file("{0}/{1}".format(testPath,file_name), 'rt') as test_file_handler:
        _buffer = test_file_handler.readlines()
        for i in xrange(0, len(_buffer), s):
            test_buffer = " ".join(_buffer[i:i + s])
            max_score = 0
            max_lang = ""
            for lang in models.keys():
                score = models[lang].score(test_buffer)
                if score > max_score:
                    max_lang = lang
                    max_score = score

            print(true_lang, max_lang, max_score, len(test_buffer))

            if true_lang == max_lang:
                true_positive += 1
            else:
                wrong_list.append(true_lang + "-" + max_lang)
            counter += 1

# with file(testPath, 'rt') as test_file_handler:
#     _buffer = test_file_handler.readlines()
#     for txt in _buffer:
#         txt_splitted = txt.split("\t")
#         true_lang = txt_splitted[1].replace("\n", "")
#         if true_lang == "xx":
#             continue
#         test_buffer = txt_splitted[0]
#         max_score = 0
#         max_lang = ""
#         for lang in models.keys():
#             score = models[lang].score(test_buffer)
#             if score > max_score:
#                 max_lang = lang
#                 max_score = score
#
#         print(true_lang, max_lang, max_score)
#
#         if true_lang == max_lang:
#             true_positive += 1
#         else:
#             wrong_list.append(true_lang + "-" + max_lang)
#         counter += 1
#         # if len(wrong_list) > 10:
#         #     break

print(true_positive, counter, 1.0 * np.array(true_positive) / counter)
uniques = np.unique(wrong_list, return_counts=True)
print(zip(uniques[0], uniques[1]))
