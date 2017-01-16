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



