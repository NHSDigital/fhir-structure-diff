import json
from functools import reduce


def extract_elements(profile) -> list:
    diff_elements = extract_diff_elements(profile)
    return add_snapshot_elements_to_diff(profile, diff_elements)


def extract_diff_elements(profile) -> dict:
    return dict(zip([e['id'] for e in profile['differential']['element'] if 'id' in e],
                    [e for e in profile['differential']['element']]))


def add_snapshot_elements_to_diff(profile, diff_elements) -> dict:
    if not profile:
        raise ValueError('Empty profile passed.\n\nProfile -->\n\n' +
                         json.dumps(profile, indent=2))

    # Just return without base paths, other searches will be attempted if empty
    # TODO think about integrating a tool to generate the snapshot if it's missing
    if 'snapshot' not in profile:
        return diff_elements

    if 'element' not in profile['snapshot']:
        raise ValueError('Elements are missing in profile.\n\nProfile -->\n\n' +
                         json.dumps(profile, indent=2))

    for de in diff_elements.values():
        for e in profile['snapshot']['element']:
            if 'id' in e \
                    and 'id' in de \
                    and de['id'] == e['id']:
                de['base'] = e['base']

    return diff_elements


# Reasonably efficient and very simple algorithm to align elements based on element id
# If id in left and right match, pop elements off each list into tuple and append to output list
# Non-matching elements in left and right input lists appended to output list with corresponding empty dict in tuple
def align_elements(left, right):
    copy_left = left.copy()
    copy_right = right.copy()

    diff_table = []
    for lft in left:
        for r in right:
            if lft == r:
                diff_table.append({lft: (copy_left.pop(lft), copy_right.pop(r))})
                break

    for lft in copy_left:
        diff_table.append({lft: (copy_left[lft], {})})

    for r in copy_right:
        diff_table.append({r: ({}, copy_right[r])})

    return diff_table


def split_elements_and_slices(elements_table) -> (list, list):
    base_elements = []
    slice_elements = []

    for e in elements_table:
        if ":" in str(list(e.keys())[0]):
            slice_elements.append(e)
        else:
            base_elements.append(e)

    return base_elements, slice_elements


def order_dict(dictionary):
    result = {}
    for k, v in sorted(dictionary.items()):
        if isinstance(v, dict):
            result[k] = order_dict(v)
        else:
            result[k] = sorted(v)
    return result


def strip_list(data):
    if not data:
        return {}
    else:
        return reduce(lambda a, b: {**a, **b}, data)


def is_valid_dict(data):
    if not data:
        return False

    if not is_or_contains_dict(data):
        return False

    try:
        json.loads(json.dumps(data))
    except ValueError as e:
        return False
    return True


def is_or_contains_dict(data) -> bool:
    if data and isinstance(data, dict):
        return True
    if data and isinstance(data, list):
        # True if one or more dictionaries exist in the list
        return search_list_for_dict(data)

    return False


def search_list_for_dict(x) -> dict:
    if not x:
        return False

    cases = {list: lambda t: search_list_for_dict(t[0]),
             dict: lambda t: t}

    try:
        return bool(cases[type(x)](x))
    except KeyError:
        return False
