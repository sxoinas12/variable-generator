import json

import pytest
from word_processor.parsers import JavascriptParser

from word_processor.strategies.leaf_no_preps_strategy import leaf_no_prep_strategy

from word_processor.generators import Generator
from spacy import displacy

@pytest.mark.parametrize(
    'text',
    [
        # 'Regex for redacted phone numbers with extra info for PlayStation',
        # 'Two days ago i was shocked by a red pair of trousers',
        #'Setting priority for attempting hydration',
        # 'Attempting to set hydration priority',
        # 'file Cache Provider get Cache Dir',
        #'Setters Value Animator Animator Update Listener',
        'Stick element after scroll has passed the element'
    ]
)
def test_antonyms(snapshot, text):
    generator = Generator(text=text, strategy=leaf_no_prep_strategy, parser=JavascriptParser())

    results = generator.suggest()

    text_results = []
    for suggestion in results:
        text_results.append([token.lemma_ for token in suggestion])

    presented_results = generator.present()
    displacy.serve(generator.doc, port=5001)
    print(presented_results)


# ADVCL
# follow adverbial clauses and discard the verb