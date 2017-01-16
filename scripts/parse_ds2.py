from packages.config import Config
import os
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


config = Config()
langPath = config.dataset2Path

for file_name in os.listdir(langPath):
    if file_name.__contains__(".txt"):
        model_name = file_name[:-4]
        with open("{0}/{1}".format(langPath, file_name), 'rt') as file_handler:
            _buffer = file_handler.readlines()
            _buffer = cleanhtml(" ".join(_buffer))
            with open("{0}/_{1}".format(langPath, file_name), 'wt') as file_write_handler:
                file_write_handler.write(_buffer)


