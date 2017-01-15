import numpy as np

class Ngram:
    def __init__(self, buffer, gram_size=2):
        self.model = dict()
        self.reverted_model = []
        self.gram_size = gram_size
        self.buffer = buffer.lower()
        self.normalize_buffer()
        self.alphabet = np.unique(list(self.buffer))
        self.create_model()
        self.revert_model()
        self.normalize_model()

        print(len(self.model))


    def normalize_buffer(self):
        self.buffer = self.buffer.replace("\n", " ")
        for i in range(10):
            self.buffer = self.buffer.replace(str(i), " ")
        while self.buffer.__contains__("  "):
            self.buffer = self.buffer.replace("  ", " ")

    def create_model(self):
        for idx in range(len(self.buffer) - self.gram_size):
            key = self.buffer[idx:idx + self.gram_size]
            if self.model.has_key(key):
                self.model[key] += 1
            else:
                self.model[key] = 1

    def revert_model(self):
        self.reverted_model = np.sort(np.array(self.model.items(), dtype=object), 0)[::-1]

    def normalize_model(self):
        # number_of_unigrams = np.shape(np.where(np.array(self.model.values()) == 1))[1]
        count_sum = np.sum(self.model.values())# - number_of_unigrams
        for k in self.model.keys():
            # if self.model[k] == 1:
            #     self.model.pop(k)
            # else:
            self.model[k] = 1.0 * self.model[k] / count_sum

    def limit_model(self, size):
        self.reverted_model = self.reverted_model[0:size]
        self.model = dict(zip(self.reverted_model[:, 0], self.reverted_model[:, 1]))
        self.normalize_model()

    def score(self, test_buffer):
        result = 1
        for idx in range(len(test_buffer) - self.gram_size):
            key = test_buffer[idx:idx + self.gram_size]
            if key in self.model:
                result *= self.model[key] * 100
            else:
                found_in_alphabet = False
                for l in key:
                    if l in self.alphabet:
                        found_in_alphabet = True
                        break
                if not found_in_alphabet:
                    pass #result *= 0.001
                else:
                    result *= 0.001
        return result



