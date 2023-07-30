import spacy
from py.error import Error

nlp = spacy.load("en_core_web_trf")


class Generator():
    """
        Generator class that will use a strategy resolver to generate suggestions for a text
        :return:

    """

    # passed text
    text = None
    # parsed text from spacy lib
    doc = None
    # the strategy resolver to use
    strategy_resolver = None
    # the parser for the presentation
    parser = None

    # suggestions calculated
    suggestions = None

    def __init__(self, text=None, strategy=None, parser=None):
        self.strategy_resolver = strategy
        self.parser = parser
        if text is not None:
            self.set_text(text)

    def suggest(self):
        if self.doc is None or self.text is None:
            raise Error('No document')

        self.suggestions = self.strategy_resolver(self.doc)

        return self.suggestions

    def set_text(self, text):
        self.text = text
        self.doc = nlp(text)

    def set_strategy(self, strategy_resolver):
        self.strategy_resolver = strategy_resolver

    def present(self):
        self.parser.suggestions = self.suggestions
        return self.parser.present()