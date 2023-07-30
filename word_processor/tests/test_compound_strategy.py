import json

import pytest

import spacy

from word_processor.generators import Generator
from word_processor.strategies import compound_strategy

nlp = spacy.load("en_core_web_trf")


@pytest.mark.parametrize('text', [
    'Regex for redacted phone numbers with extra info for PlayStation',
    'Stick element after scroll has passed the element',
    'Stick element after scroll has passed the element',
])
def test_compound_strategy(snapshot, text):
    generator = Generator(text=text, strategy=compound_strategy)

    results = generator.suggest()

    text_results = []
    for suggestion in results:
        text_results.append([token.lemma_ for token in suggestion])

    assert text_results == snapshot
