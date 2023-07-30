from spacy.tokens import Token
from word_processor.strategies.leaf_strategy import dfs

from word_processor.types import DEP_TYPES


def adverbial_strategy(doc) -> [[Token]]:
    """
    Should return an arrays of variable names based on adverbial strategy
    When a verb appears, if it has children in both directions, then remove the verb and
    add the a left child and a continue to the right child. Does so for all combinations (left,right)

    :param doc: spacy document
    :return Array of strings
    """
    suggestions = []
    for token in doc:
        if token.dep_ == DEP_TYPES['ROOT']:
            suggestions = process_adverbial_clauses(token)
            break

    return suggestions


INVALID_DEP = ['aux', 'prep']
INVALID_POS = ['DET', 'AUX', 'ADP']


def is_valid(node):
    return not (node.pos_ in INVALID_POS) and not (node.dep_ in INVALID_DEP)


# todo - this is dfs
def process_adverbial_clauses(node, result=None, output=None):
    if output is None:
        output = []
    if result is None:
        result = []

    has_children = (node.n_lefts + node.n_rights) > 0
    has_both_directions = node.n_lefts > 0 and node.n_rights > 0

    if node.pos_ == 'VERB' and has_both_directions:
        for lefty in node.lefts:
            for righty in node.rights:
                if is_valid(lefty):
                    process_adverbial_clauses(righty, [*result, lefty], output)
                # if is_valid(righty):
                #     process_adverbial_clauses(lefty, [*result, righty], output)
    elif has_children:
        for u in node.children:
            valid_results = [*result, node] if is_valid(node) else result
            process_adverbial_clauses(u, valid_results, output)
    else:
        valid_results = [*result, node] if is_valid(node) else result
        output.append(valid_results)

    return output
