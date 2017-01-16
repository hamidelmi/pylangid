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

