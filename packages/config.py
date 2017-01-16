import pickle as pk
import os

class Config:
    basePath = ".."
    dataPath = "{0}/data".format(basePath)
    inputPath = "{0}/input".format(dataPath)
    langPath = "{0}/langs".format(inputPath)
    dataset1Path = "{0}/dataset1".format(langPath)
    dataset2Path = "{0}/dataset2/merged".format(langPath)
    test1Path = "{0}/test.dat".format(dataset1Path)
    test2Path = "{0}/dataset2/test".format(langPath)
    outputPath = "{0}/output".format(dataPath)
    modelsPath = "{0}/models".format(outputPath)
    models1Path = "{0}/dataset1".format(modelsPath)
    models2Path = "{0}/dataset2".format(modelsPath)

    def load_models(self, modelPath, langPath, n_gram):
        models = dict()
        # Load trained models
        for file_name in os.listdir(langPath):
            if file_name.__contains__(".txt"):
                print("Load lang:" + file_name)
                model_name = file_name[:-4]
                if model_name in ["xx"]:
                    continue
                if os.path.isfile("{0}/{1}/{2}".format(modelPath, n_gram, file_name)):
                    with open("{0}/{1}/{2}".format(modelPath, n_gram, file_name), 'rb') as model_file_handler:
                        models[model_name] = pk.load(model_file_handler)
                        models[model_name].revert_model()
        return models

