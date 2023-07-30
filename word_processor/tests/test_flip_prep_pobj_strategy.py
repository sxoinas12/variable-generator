import json

import pytest

import spacy

from word_processor.generators import Generator
from word_processor.strategies import flip_prep_pobj_strategy

nlp = spacy.load("en_core_web_trf")


@pytest.mark.parametrize('text', [
    'allow chat communication for authenticated users',
    'Regex for redacted phone numbers with extra info for PlayStation',
    'generate an authentication token for offline users',
    'serializer for contact roles',
    'Stick element after scroll has passed the element',
])
def test_flip_prep_pobj_strategy(snapshot, text):
    generator = Generator(text=text, strategy=flip_prep_pobj_strategy)

    results = generator.suggest()

    text_results = []
    for suggestion in results:
        text_results.append([token.lemma_ for token in suggestion])

    assert text_results == snapshot
