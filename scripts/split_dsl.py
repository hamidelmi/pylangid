from packages.config import Config
lang_size = 18000
config = Config()
file_address = "{0}/train.txt".format(config.inputPath)

with file(file_address, 'rt') as file_handler:
    buffer = file_handler.readlines()
    for i in xrange(0,len(buffer) - lang_size, lang_size):
        lang = buffer[i+1].split("\t")[1].replace("\n", "")
        print(lang)
        with file("{0}/{1}.txt".format(config.langPath,lang), 'wt') as output_handler:
            output_handler.writelines(buffer[i:i+lang_size])





