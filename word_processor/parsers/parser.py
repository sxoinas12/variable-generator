from spacy.tokens import Token


class Parser:
    suggestions = None
    parsed_suggestions = None

    def __init__(self, suggestions=None):
        self.suggestions = suggestions

    def parse_word(self, word: Token):
        return word.text

    def parse_words(self, words: [Token]):
        return [self.parse_word(word) for word in words]

    def parse(self):
        self.parsed_suggestions = [self.parse_words(words) for words in self.suggestions]

        return self

    def present_word(self, word: str):
        return word

    def present_words(self, words: [str]):
        presented_words = [self.present_word(word) for word in words]

        return ''.join(presented_words)

    def present(self):
        self.parse()

        return [self.present_words(words) for words in self.parsed_suggestions]
