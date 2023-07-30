import json

import pytest

import spacy

from word_processor.generators import Generator
from word_processor.strategies import leaf_strategy

nlp = spacy.load("en_core_web_trf")


@pytest.mark.parametrize('text, expected', [
    ('Regex for redacted phone numbers with extra info for PlayStation',
     ['PhoneNumberRegex', 'RedactedPhoneNumberRegex'])
])
def test_leaf_strategy(snapshot, text, expected):
    generator = Generator(text=text, strategy=leaf_strategy)

    results = generator.suggest()

    text_results = []
    for suggestion in results:
        text_results.append([token.text for token in suggestion])

    assert text_results == snapshot
