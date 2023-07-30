from .leaf_strategy import leaf_strategy


def leaf_no_prep_strategy(doc):
    """
    Should return an arrays of variable names based on leaf strategy without the preps(at, for)

    :param doc: spacy document
    :return Array of strings
    """

    suggestions = leaf_strategy(doc)

    new_suggestions = []
    for suggestion in suggestions:
        new_suggestion = []
        for token in suggestion:
            if token.dep_ != 'prep':
                new_suggestion.append(token)

        new_suggestions.append(new_suggestion)

    return new_suggestions
