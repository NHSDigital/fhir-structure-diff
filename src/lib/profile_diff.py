import json
import difflib
from itertools import islice
from .profile_elements import extract_elements, align_elements, is_valid_dict
from .base_definitions import get_base_component

# Components within element that should not be diff-ed
IGNORED_COMPONENTS = ['id', 'path', 'base']

# Constants for use in table results.
MATCH_RESULT = 'Match'
MATCH_WITH_VALUE_RESULT = 'Match. "{component}" == '
DIFF_RESULT = 'See diff'
NOT_DEFINED_RESULT = 'Not defined'
NOTHING_TO_DIFF = 'Nothing to diff, value below'
SAME_AS_BASE_RESULT = 'Same as base'
BASE_WITH_VALUE_RESULT = '"{component}" == '
BASE_NOT_DEFINED_RESULT = '"{component}" is not defined in the base element definition.'
BASE_NOT_DEFINED_IS_SLICE_RESULT = '"{component}" is a custom slice and therefore not defined in the base'


def element_diff(left, right):
    cc_element_list = [e['id'] for e in left['differential']['element'] if 'id' in e]
    gpc_element_list = [e['id'] for e in right['differential']['element'] if 'id' in e]

    return list_diff(cc_element_list, gpc_element_list)


def component_diff(left, right):
    left_elements = extract_elements(left)
    right_elements = extract_elements(right)
    return detailed_diff(left_elements, right_elements)


def detailed_diff(left, right):
    elements_table = align_elements(left, right)
    diff = dict()

    for element_operands in elements_table:
        left_element = tuple(*element_operands.values())[0]
        right_element = tuple(*element_operands.values())[1]
        components_table = align_elements(left_element, right_element)

        for component in components_table:
            diff |= component_level_diff(element_operands, component)

    return diff


def component_level_diff(element, component):
    element_key = str(*element.keys())
    component_results = {}
    component_key = str(*component.keys())

    if component_key not in IGNORED_COMPONENTS:
        left_component = tuple(*component.values())[0]
        right_component = tuple(*component.values())[1]
        base_component = get_base_component(element, component_key)
        component_results = {element_key: base_component_diff(component_key,
                                                              left_component,
                                                              right_component,
                                                              base_component)}
    return component_results


def base_component_diff(component_key, left, right, base):
    table_result = {}
    match = {}
    component_diff = {}

    if not is_valid_dict(left) and \
            not is_valid_dict(right):
        table_result = primitive_component_diff(left, right, base, component_key)
    elif left == right:
        match = json_pretty(left)
        table_result = (MATCH_RESULT, MATCH_RESULT)
    elif component_key not in IGNORED_COMPONENTS:
        component_diff, table_result = object_component_diff(left, right, base)

    if is_valid_dict(base):
        base = '```json\n' + json_pretty(base) + '\n```'
    elif base == {}:
        base = BASE_NOT_DEFINED_RESULT.replace('{component}', component_key)
    else:
        base = BASE_WITH_VALUE_RESULT.replace('{component}', component_key) + str(base)

    return {
        component_key: {'table_result': table_result,
                        'match': match,
                        'component_diff': component_diff,
                        'base': base}
    }


def object_component_diff(left, right, base):
    if left and right and \
            is_valid_dict(left) and is_valid_dict(right):
        return json_diff(left, right), \
               (DIFF_RESULT, DIFF_RESULT)

    elif left and not right:
        # return json_diff(left, base), \
        return json_pretty(left), \
               (NOTHING_TO_DIFF, NOT_DEFINED_RESULT)

    elif right and not left:
        # return json_diff(base, right), \
        return json_pretty(right), \
               (NOT_DEFINED_RESULT, NOTHING_TO_DIFF)

    else:
        raise ValueError("Unable to compare (object) component values'" + left + "' and '" +
                         right + "', where base component is '" + base + "'")


def primitive_component_diff(left, right, base, component_key):
    if base == {}:
        base = ''

    if left == right == base:
        return SAME_AS_BASE_RESULT, SAME_AS_BASE_RESULT

    elif left == right and left and right:
        return MATCH_WITH_VALUE_RESULT.replace('{component}', component_key) + str(left), \
               MATCH_WITH_VALUE_RESULT.replace('{component}', component_key) + str(right)

    elif left == {} and right:
        return NOT_DEFINED_RESULT, right

    elif right == {} and left:
        return left, NOT_DEFINED_RESULT

    else:
        raise ValueError("Unable to compare (primitive) component values '" + str(left) + "' and '" +
                         str(right) + "', where base component is '" + str(base) + "'")


def list_diff(left, right) -> str:
    diff_text = ''

    # Ensure context covers full diff
    diff_generator = difflib.unified_diff(left,
                                          right,
                                          n=max(len(left), len(right)))

    # Remove line number and operand details
    for diff in islice(diff_generator, 3, None):
        diff_text = diff_text + diff + '  \n'

    return diff_text


def json_diff(left, right) -> str:
    left_lines = json_pretty(left).splitlines()
    right_lines = json_pretty(right).splitlines()

    return list_diff(left_lines, right_lines)


def json_pretty(data):
    return json.dumps(
        data,
        indent=2,
        sort_keys=True
    )
