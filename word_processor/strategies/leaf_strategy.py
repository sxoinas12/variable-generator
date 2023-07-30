from spacy.tokens import Token

from word_processor.types import DEP_TYPES


def leaf_strategy(doc) -> [[Token]]:
    """
    Should return an arrays of variable names based on leaf strategy

    :param doc: spacy document
    :return Array of strings
    """

    for token in doc:
        if token.dep_ == DEP_TYPES['ROOT']:
            suggestions = dfs(token)
            break

    return suggestions or []


def dfs(graph, result=None, output=None):
    if output is None:
        output = []
    if result is None:
        result = []

    flag = False
    for u in graph.children:
        flag = True
        dfs(u, [*result, graph], output)
    if flag is False:
        output.append([*result, graph])
    return output
