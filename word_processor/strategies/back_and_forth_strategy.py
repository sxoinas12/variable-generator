from spacy.tokens import Token

from word_processor.types import DEP_TYPES


def back_and_forth_strategy(doc) -> [[Token]]:
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
            suggestions = prep_dfs(token)
            break

    return suggestions


INVALID_DEP = ['aux', 'prep']
INVALID_POS = ['DET', 'AUX', 'ADP']
FLIP_DEP = ['compound', 'amod']
PREPEND_DEP = ['pobj', 'dobj']


def is_valid(node, existing=None):
    return (
            not (node.pos_ in INVALID_POS)
            and not (node.dep_ in INVALID_DEP)
            and not (node in existing if existing else False)
    )


def should_flip(node):
    return node.dep_ in FLIP_DEP


def should_prepend(node):
    return node.dep_ in PREPEND_DEP


def merge_outputs(output, merge_outputs=None, append=None, clear=None):
    if merge_outputs is None:
        merge_outputs = []
    if append is None:
        append = []
    try:
        output.remove(clear)
    except ValueError:
        pass
    for sub_output in merge_outputs:
        output.append([*sub_output, *append])
    return output


def prep_dfs(node, result=None, output=None, root=None):
    if root is None:
        root = node
    if output is None:
        output = []
    if result is None:
        result = []

    has_parent = node.head != node and root != node
    has_children = (node.n_lefts + node.n_rights) > 0
    has_both_directions = node.n_lefts > 0 and node.n_rights > 0

    if should_flip(node) and has_parent and is_valid(node, result):
        prep_dfs(node.head, [*result[:-1], node], output, root=root)
        # dunno if i should return here
        return output

    if has_parent and should_prepend(node) and is_valid(node, result):
        sub_tree_output = prep_dfs(node, [node], [[node]] if not has_children else None, root=node)
        for child in node.head.children:
            if child != node:
                child_tree_output = prep_dfs(
                    child,
                    [child] if is_valid(child) else None,
                    [[child]] if (child.n_lefts+child.n_rights) and is_valid(child) else None,
                    root=child
                )
                for child_output in child_tree_output:
                    merge_outputs(output, [*sub_tree_output], append=[*child_output, *result], clear=result)
        merge_outputs(output, [*sub_tree_output], append=[*result], clear=result)
        return output

    if node.pos_ == 'VERB' and has_both_directions:
        for lefty in node.lefts:
            for righty in node.rights:
                if is_valid(lefty, result):
                    prep_dfs(righty, [*result, lefty], output, root=root)
                # if is_valid(righty):
                #     prep_dfs(lefty, [*result, righty], output, root=root)
    elif has_children:
        sub_trees = []

        # for child in node.children:
        #     valid_results = [*result, node] if is_valid(node, result) else result
        #     prep_dfs(child, valid_results, output, root=root)
        for child in node.children:
            valid_results = [*result, node] if is_valid(node, result) else result
            sub_trees.append(prep_dfs(child, valid_results, [*output], root=root))

        for sub_tree in sub_trees:
            merge_outputs(output, [*sub_tree])
    else:
        valid_results = [*result, node] if is_valid(node, result) else result
        output.append(valid_results)

    return output
