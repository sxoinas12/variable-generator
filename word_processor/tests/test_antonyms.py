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
def test_antonyms(snapshot, word):
    result = synonym.get_antonyms(word)

    assert result == snapshot