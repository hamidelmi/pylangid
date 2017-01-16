import numpy as np

class Ngram:
    def __init__(self, buffer, gram_size=2):
        self.model = dict()
        self.reverted_model = []
        self.gram_size = gram_size
        self.buffer = buffer.lower()
        self.buffer = self.normalize_text(self.buffer)
        self.alphabet = np.unique(list(self.buffer))
        self.create_model()
        self.revert_model()
        self.normalize_model()

        print(len(self.model))

    def normalize_text(self, buffer):
        rep = [("\n", " "), (".", " "), (",", " "), (";", " ")]
        for item in rep:
            result = buffer.replace(item[0], item[1])
        for i in range(10):
            result = result.replace(str(i), " ")
        while result.__contains__("  "):
            result = result.replace("  ", " ")
        return result

    def create_model(self):
        for idx in range(len(self.buffer) - self.gram_size):
            key = self.buffer[idx:idx + self.gram_size]
            if self.model.has_key(key):
                self.model[key] += 1
            else:
                self.model[key] = 1

    def revert_model(self):
        self.reverted_model = self.__revert_model(self.model)

    def __revert_model(self, model):
        tmp = np.array(model.items(), dtype=object)
        arg_idx = np.argsort(tmp[:, 1])[::-1]
        result = tmp[arg_idx]
        return result

    def normalize_model(self):
        # # number_of_unigrams = np.shape(np.where(np.array(self.model.values()) == 1))[1]
        # count_sum = np.sum(self.model.values())# - number_of_unigrams
        # for k in self.model.keys():
        #     # if self.model[k] == 1:
        #     #     self.model.pop(k)
        #     # else:
        #     self.model[k] = 1.0 * self.model[k] / count_sum
        count_sum = np.sum(self.model.values())
        for idx, item in enumerate(self.reverted_model):
            key = item[0]
            if isinstance(item[1], int):
                value = item[1]
            else:
                value = item[1][0]
            self.model[key] = (1.0 * value / count_sum, idx)

    def limit_model(self, size):
        self.reverted_model = self.reverted_model[0:size]
        self.model = dict(zip(self.reverted_model[:, 0], self.reverted_model[:, 1]))
        self.normalize_model()

    def distance(self, test_buffer):
        test_buffer = self.normalize_text(test_buffer)
        result = 0
        test_model = dict()
        for idx in range(len(test_buffer) - self.gram_size):
            key = self.buffer[idx:idx + self.gram_size]
            if test_model.has_key(key):
                test_model[key] += 1
            else:
                test_model[key] = 1

        test_reverted_model = self.__revert_model(test_model)
        for idx, item in enumerate(test_reverted_model):
            key = item[0]
            if key in self.model:
                idx_model = self.model[key][1]
                result += abs(idx - idx_model)
            else:
                result += 1000
        return result

    def score(self, test_buffer):
        result = 1
        m = pow(10, self.gram_size)
        for idx in range(len(test_buffer) - self.gram_size):
            key = test_buffer[idx:idx + self.gram_size]
            if key in self.model:
                result *= self.model[key][0] * m
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



