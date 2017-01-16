import pickle as pk
import numpy as np
from config import Config
import os

config = Config()
testPath = config.test2Path

n_gram = 2

modelPath = config.models1Path
langPath = config.dataset1Path
testPath = config.test1Path


models = config.load_models(modelPath, langPath, n_gram)

wrong_list = []
test_buffer_len = []
true_positive = 0
counter = 0

with file(testPath, 'rt') as test_file_handler:
    _buffer = test_file_handler.readlines()
    for txt in _buffer:
        txt_splitted = txt.split("\t")
        true_lang = txt_splitted[1].replace("\n", "")
        if true_lang == "xx":
            continue
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

print(true_positive, counter, 1.0 * np.array(true_positive) / counter)
uniques = np.unique(wrong_list, return_counts=True)
print(zip(uniques[0], uniques[1]))