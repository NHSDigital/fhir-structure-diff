import pytest
from ...lib import profile_diff
from ...lib import profile_elements
from unittest import mock


@mock.patch('json.dumps')
def test_json_pretty(mocked):
    profile_diff.json_pretty('{}')
    mocked.assert_called_once_with('{}', indent=2, sort_keys=True)


def test_json_diff(data_left_right_elements_operands_right_base_path,
                   data_diff_operands_right_base_path):
    output_data = profile_diff.json_diff(
        data_left_right_elements_operands_right_base_path["AllergyIntolerance.extension"][0],
        data_left_right_elements_operands_right_base_path["AllergyIntolerance.extension"][1]);
    expected_data = data_diff_operands_right_base_path
    assert output_data == expected_data


def test_list_diff(data_operands_right_base_path_left,
                   data_operands_right_base_path_right,
                   data_diff_operands_right_base_path):
    output_data = profile_diff.list_diff(data_operands_right_base_path_left, data_operands_right_base_path_right);
    expected_data = data_diff_operands_right_base_path
    assert output_data == expected_data


def test_primitive_component_diff_all_same(data_basic_primitive):
    output_data = profile_diff.primitive_component_diff(data_basic_primitive,
                                                        data_basic_primitive,
                                                        data_basic_primitive,
                                                        'key')
    expected_data = ('Same as base', 'Same as base')
    assert output_data == expected_data


def test_primitive_component_diff_left_right_same(data_basic_primitive):
    output_data = profile_diff.primitive_component_diff(data_basic_primitive,
                                                        data_basic_primitive,
                                                        'base is different',
                                                        'key')
    expected_data = ('Match. "key" == ' + str(data_basic_primitive),
                     'Match. "key" == ' + str(data_basic_primitive))
    assert output_data == expected_data


def test_primitive_component_diff_left_empty(data_basic_primitive):
    output_data = profile_diff.primitive_component_diff({},
                                                        data_basic_primitive,
                                                        'base is different',
                                                        'key')
    expected_data = ('Not defined', data_basic_primitive)
    assert output_data == expected_data


def test_primitive_component_diff_right_empty(data_basic_primitive):
    output_data = profile_diff.primitive_component_diff(data_basic_primitive,
                                                        {},
                                                        'base is different',
                                                        'key')
    expected_data = (data_basic_primitive, 'Not defined')
    assert output_data == expected_data


def test_primitive_component_diff_empty(data_input_empty):
    with pytest.raises(ValueError) as exception_info:
        profile_diff.primitive_component_diff(data_input_empty,
                                              data_input_empty,
                                              data_input_empty,
                                              data_input_empty)
    assert 'Unable to compare (primitive) component values' in str(exception_info)


def test_object_component_diff_json_diff(data_left_right_elements_operands_right_base_path,
                                         data_diff_operands_right_base_path):
    output_data = profile_diff.object_component_diff(
        data_left_right_elements_operands_right_base_path["AllergyIntolerance.extension"][0],
        data_left_right_elements_operands_right_base_path["AllergyIntolerance.extension"][1],
        [{'code': 'Extension'}])
    expected_data = (data_diff_operands_right_base_path, ('See diff', 'See diff'))
    assert output_data == expected_data


def test_object_component_diff_right_empty(data_left_right_elements_operands_right_base_path,
                                           data_left_right_elements_operands_right_base_path_left_pretty):
    output_data = profile_diff.object_component_diff(
        data_left_right_elements_operands_right_base_path["AllergyIntolerance.extension"][0],
        {},
        [{'code': 'Extension'}])
    expected_data = (data_left_right_elements_operands_right_base_path_left_pretty,
                     ('Nothing to diff, value below', 'Not defined'))
    assert output_data == expected_data


def test_object_component_diff_left_empty(data_left_right_elements_operands_right_base_path,
                                          data_left_right_elements_operands_right_base_path_left_pretty):
    output_data = profile_diff.object_component_diff({},
                                                     data_left_right_elements_operands_right_base_path[
                                                         "AllergyIntolerance.extension"][0],
                                                     [{'code': 'Extension'}])
    expected_data = (data_left_right_elements_operands_right_base_path_left_pretty,
                     ('Not defined', 'Nothing to diff, value below'))
    assert output_data == expected_data


def test_object_component_diff_empty(data_input_empty):
    with pytest.raises(ValueError) as exception_info:
        profile_diff.object_component_diff(data_input_empty,
                                           data_input_empty,
                                           data_input_empty)
    assert 'Unable to compare (object) component values' in str(exception_info)


def test_base_component_diff_both_primitive(data_basic_primitive):
    output_data = profile_diff.base_component_diff('key',
                                                   data_basic_primitive,
                                                   data_basic_primitive,
                                                   data_basic_primitive)
    expected_data = {'key': {'table_result': ('Same as base', 'Same as base'),
                             'match': {},
                             'component_diff': {},
                             'base': '"key" == ' + str(data_basic_primitive)}}
    assert output_data == expected_data


def test_base_component_diff_not_primitive():
    output_data = profile_diff.base_component_diff('key',
                                                   {'simple': 'json'},
                                                   {'simple': 'json'},
                                                   {'simple': 'json'})
    expected_data = {'key': {'table_result': ('Match', 'Match'),
                             'match': '{\n  "simple": "json"\n}',
                             'component_diff': {},
                             'base': '```json\n{\n  "simple": "json"\n}\n```'}}
    assert output_data == expected_data


def test_base_component_diff_not_primitive_do_not_match():
    output_data = profile_diff.base_component_diff('key',
                                                   {'simple': 'json'},
                                                   {'simple': 'Not matching'},
                                                   {'simple': 'json'})
    expected_data = {'key': {'table_result': ('See diff', 'See diff'),
                             'match': {},
                             'component_diff': ' {  \n-  "simple": "json"  \n+  "simple": "Not matching"  \n }  \n',
                             'base': '```json\n{\n  "simple": "json"\n}\n```'}}
    assert output_data == expected_data


def test_base_component_diff_not_primitive_base_empty():
    output_data = profile_diff.base_component_diff('key',
                                                   {'simple': 'json'},
                                                   {'simple': 'json'},
                                                   {})
    expected_data = {'key': {'table_result': ('Match', 'Match'),
                             'match': '{\n  "simple": "json"\n}',
                             'component_diff': {},
                             'base': '"key" is not defined in the base element definition.'}}
    assert output_data == expected_data


@mock.patch('src.lib.profile_diff.get_base_component',
            lambda element, component_key, version: \
                    {'discriminator':
                        [
                            {'type': 'value',
                             'path': 'url'}
                        ],
                        'description': 'Extensions are always sliced by (at least) url',
                        'rules': 'open'
                    })
def test_component_level_diff(data_left_right_elements_operands_left_base_path,
                              data_component_diff_allergyintolerance_results):
    output_data = profile_diff.component_level_diff(data_left_right_elements_operands_left_base_path,
                                                    {'slicing':
                                                         (
                                                             {'discriminator': [{'type': 'value', 'path': 'url'}], 'rules': 'open'},
                                                             {'discriminator': [{'type': 'value', 'path': 'url'}], 'rules': 'open'}
                                                         )
                                                     },
                                                    '3.0.1')
    expected_data = data_component_diff_allergyintolerance_results
    assert output_data == expected_data


@mock.patch('src.lib.profile_diff.component_level_diff',
            lambda element_operands, component, version: \
                    {'AllergyIntolerance.extension':
                         {'max': {'table_result': ('Match. "max" == 1', 'Match. "max" == 1'),
                                  'match': {},
                                  'component_diff': {},
                                  'base': '"max" == *'}
                         }
                    })
def test_detailed_diff():
    output_data = profile_diff.detailed_diff({"AllergyIntolerance.extension": {"max": "1"}},
                                             {"AllergyIntolerance.extension": {"max": "1"}},
                                             '3.0.1')
    expected_data = {'AllergyIntolerance.extension':
                         {'max': {'table_result': ('Match. "max" == 1', 'Match. "max" == 1'),
                                  'match': {},
                                  'component_diff': {},
                                  'base': '"max" == *'}
                         }
                    }
    assert output_data == expected_data


@mock.patch('src.lib.profile_diff.detailed_diff',
            lambda left_elements, right_elements, version: \
                    {'AllergyIntolerance.extension':
                         {'max': {'table_result': ('Match. "max" == 1', 'Match. "max" == 1'),
                                  'match': {},
                                  'component_diff': {},
                                  'base': '"max" == *'}
                         }
                    })
def test_component_diff(data_single_element):
    output_data = profile_diff.component_diff(data_single_element,
                                              data_single_element,
                                              '3.0.1')
    expected_data = {'AllergyIntolerance.extension':
                         {'max': {'table_result': ('Match. "max" == 1', 'Match. "max" == 1'),
                                  'match': {},
                                  'component_diff': {},
                                  'base': '"max" == *'}
                         }
                    }
    assert output_data == expected_data


def test_element_diff(data_single_element):
    output_data = profile_diff.element_diff(data_single_element,
                                            data_single_element)
    expected_data = ''
    assert output_data == expected_data