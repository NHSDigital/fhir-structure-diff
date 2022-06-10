import json


def extract_elements(profile) -> list:
    diff_elements = extract_diff_elements(profile)
    return add_snapshot_elements_to_diff(profile, diff_elements)


def extract_diff_elements(profile) -> dict:
    return dict(zip([e['path'] for e in profile['differential']['element'] if 'path' in e],
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
            if 'path' in e \
                    and 'path' in de \
                    and de['path'] == e['path']:
                de['base'] = e['base']

    return diff_elements


# Reasonably efficient and very simple algorithm to align elements based on element id
# If id in left and right match, pop elements off each list into tuple and append to output list
# Non-matching elements in left and right input lists appended to output list with corresponding empty dict in tuple
def align_elements(left, right):
    if not isinstance(left, dict) or not isinstance(right, dict):
        raise TypeError('Unexpected data in profile_elements.align_elements.'
                        '\n\nLeft is a ' + str(type(left)) + '. Contents:\n\n' + str(left) +
                        '\n\nRight is a ' + str(type(left)) + '. Contents:\n\n' + str(right))

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


def is_valid_dict(data):
    if not data:
        return False

    if not is_or_contains_dict(data):
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
