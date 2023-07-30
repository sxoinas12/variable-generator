import json

import pytest

import word_processor.generators.synonym as synonym


@pytest.mark.parametrize(
    'word',
    [
        'dog',
        'cat',
        'fetcher',
        'serializer',
        'factory',
    ]
)
def test_synonyms(snapshot, word):
    result = synonym.get_synonyms(word)

    assert result == snapshot
