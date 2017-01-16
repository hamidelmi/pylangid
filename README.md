# pylangid (Language Identification)

This is a relatively simple implementation of a language identification system in Python. The aim is to learn a model that would be able to discreminate the language of a set documents. 

# Model
It starts with pre-processing the training documents which consists of eliminating any annotations that are in form HTML tags as well as numbers and some punctuation marks. Then, it calcualtes the frequency of each N-grams independently for each language. There are some works like [1, 2] that uses the sorted frequency N-gram model to calculate a distanc metric. They sort the frequency N-grams in descending way and calcualte the displacement for each of N-grams in the test data. 

However, our model is design to assign a score to a test data.  The model normalizes n-grams in order to represent each language as a probability distribution over its n-grams. N-grams are based on character since it is practically inefficient to find the probability distribution over all possible words of each languages. Test dataset is being evaluated agaisnt all language models by simply finding the join probability of the test data being generated from the learned models. It then chooses the most probable model as the output. 

It is important to note that this is potentionally a sclable approach since it can be easily parallelized in a distributed platform such as Spark to speed up the learing and evaluation process. 

# Dataset
The first dataset [3] is the European Parliament Corpus that consists of 21:  European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek

Secondly, I used a more complicated dataset in which documents from very similar languages are about to be discreminate. I used the dataset of DSL-2015. It consists of 18,000 sentences for the following 13 languages:
 - South-Eastern Slavic (Bulgarian (bg), Macedonian (mk))
 - South-Western Slavic (Bosnian (bs), Croatian (hr), Serbian (sr))
 - West Slavic (Czech (cz), Slovak (sk))
 - Spanish (Argentine Spanish (es_AR), Peninsular Spanish (es_ES))
 - Portuguese (Brazilian Portuguese (pt-BR), European Portuguese (pt-PT))
 - Austronesian (Indonesian (id), Malay (my))

#Experiment and resutls

For the second dataset, I evaluate the model against a golden dataset which contains 14,000 sentences for each languages and here is the result:

![alt tag](https://s23.postimg.org/81oyz8fx7/image_2.png)

The above chart shows that 4-gram has the best overall performance in dataset #2.

#References

[1] Language Identification from Text Using N-gram Based Cumulative Frequency Addition, Bashir Ahmed, Sung-Hyuk Cha, and Charles Tappert

[2] N-Gram-Based Text Categorization, William B. Cavnar and John M. Trenkle

[3] A Parallel Corpus for Statistical Machine Translation, Philipp Koehn

[4] http://corporavm.uni-koeln.de/vardial/sharedtask.html