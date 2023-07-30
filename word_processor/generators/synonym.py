import nltk
from nltk.corpus import wordnet
import os

from nltk.corpus.reader import WordNetError

print("Loading nltk", os.path.dirname(__file__) + '/../../nltk_data/')
nltk.data.path.append(os.path.dirname(__file__) + '/../../nltk_data/')


def get_synonyms(word):
    synonyms = []

    try:
        synsets_words = wordnet.synsets(word)
    except WordNetError:
        return []

    for syn in synsets_words:
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    return synonyms


def get_antonyms(word):
    antonyms = []

    try:
        synsets_words = wordnet.synsets(word)
    except WordNetError:
        return []

    for syn in synsets_words:
        for lemma in syn.lemmas():
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    antonyms.append(antonym.name())

    return antonyms