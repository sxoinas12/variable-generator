from spacy.tokens import Token

from word_processor.parsers import Parser


class JavascriptParser(Parser):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse_word(self, word: Token):
        return word.lemma_.title()

    def parse_words(self, words: [Token]):
        parsed_words = super().parse_words(words)

        return parsed_words
