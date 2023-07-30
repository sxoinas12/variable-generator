from spacy.tokens import Token

from word_processor.types import DEP_TYPES


def compound_strategy(doc) -> [[Token]]:
    """
    Should return an arrays of variable names based on compound strategy
    Uses adverbial strategy and also adds compounds to nouns

    e.g.
    Reads black phone numbers
    Will treat PhoneNumbers as a single entity.

    :param doc: spacy document
    :return Array of strings
    """
    suggestions = []
    for token in doc:
        if token.dep_ == DEP_TYPES['ROOT']:
            suggestions = compound_dfs(token)
            break

    return suggestions


INVALID_DEP = ['aux', 'prep']
INVALID_POS = ['DET', 'AUX', 'ADP']
FLIP_DEP = ['compound', 'amod']


def is_valid(node, existing=None):
    return (
            not (node.pos_ in INVALID_POS)
            and not (node.dep_ in INVALID_DEP)
            and not (node in existing if existing else False)
    )


def should_flip(node):
    return node.dep_ in FLIP_DEP


# todo - this is dfs
def compound_dfs(node, result=None, output=None):
    if output is None:
        output = []
    if result is None:
        result = []

    has_parent = node.head != node
    has_children = (node.n_lefts + node.n_rights) > 0
    has_both_directions = node.n_lefts > 0 and node.n_rights > 0

    if should_flip(node) and has_parent and is_valid(node, result):
        compound_dfs(node.head, [*result[:-1], node], output)
        return output

    if node.pos_ == 'VERB' and has_both_directions:
        for lefty in node.lefts:
            for righty in node.rights:
                if is_valid(lefty, result):
                    compound_dfs(righty, [*result, lefty], output)
                # if is_valid(righty):
                #     compound_dfs(lefty, [*result, righty], output)
    elif has_children:
        for u in node.children:
            valid_results = [*result, node] if is_valid(node, result) else result
            compound_dfs(u, valid_results, output)
    else:
        valid_results = [*result, node] if is_valid(node, result) else result
        output.append(valid_results)

    return output
