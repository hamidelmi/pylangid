import pickle as pk
import numpy as np
from config import Config
import os

config = Config()
testPath = config.test2Path

n_gram = 2

modelPath = config.models2Path
langPath = config.dataset2Path
testPath = config.test2Path

models = config.load_models(modelPath, langPath, n_gram)

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

print(true_positive, counter, 1.0 * np.array(true_positive) / counter)
uniques = np.unique(wrong_list, return_counts=True)
print(zip(uniques[0], uniques[1]))
