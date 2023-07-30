import json

import pytest

from word_processor.generators import Generator
from word_processor.parsers import Parser
from word_processor.strategies import leaf_strategy

@pytest.mark.parametrize('text', [
    'Regex for redacted phone numbers with extra info for PlayStation'
])
def test_parser(snapshot, text):
    generator = Generator(text=text, strategy=leaf_strategy, parser=Parser())

    generator.suggest()

    presentation = generator.present()

    assert presentation == snapshot

