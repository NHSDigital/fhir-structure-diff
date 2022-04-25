import pytest
from parameterized import parameterized
from ...lib import base_definitions
from unittest import mock
from collections import namedtuple


# ----------------------- MOCKS -----------------------
def mocked_response(url):
    Decode = namedtuple('Decode', 'decode')
    Response = namedtuple('Response', 'content ok status')
    # Lambda is mocking the decode function for the content object in the response
    if url == 'VALID_URL':
        return Response(Decode(lambda encoding: ({'responseType': 'AllergyIntolerance'})), True, 200)
    elif url == 'NOT_FOUND':
        return Response({}, False, 0)


# ----------------------- MOCKS -----------------------


@parameterized.expand([
    ['AllergyIntolerance', '3.0.2', 'STU3/'],
    ['Encounter', '1.0.2', 'DSTU2/'],
    ['Patient', '0.8.0', 'DSTU1/'],
    ['ServiceRequest', '4.0.1', 'R4/']
])
def test_get_profile_url_valid(resource_type, version, fhir_version_expected):
    output_data = base_definitions.get_profile_url(resource_type, version)
    expected_data = base_definitions.BASE_URL + fhir_version_expected + resource_type + base_definitions.BASE_FILE_TYPE
    assert output_data == expected_data


def test_get_profile_url_invalid(data_primitive_invalid):
    with pytest.raises(ValueError) as exception_info:
        base_definitions.get_profile_url(data_primitive_invalid, data_primitive_invalid)
    assert 'Unknown FHIR version' in str(exception_info)


@mock.patch('src.lib.base_definitions.get_profile_url', lambda resource_type, version: 'VALID_URL')
@mock.patch('requests.get', side_effect=mocked_response)
def test_download_definition_valid(mocked):
    output_data = base_definitions.download_definition('AllergyIntolerance', '3.0.2')
    expected_data = {'responseType': 'AllergyIntolerance'}
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.get_profile_url', lambda resource_type, version: 'NOT_FOUND')
@mock.patch('requests.get', side_effect=mocked_response)
def test_download_definition_not_found(mocked):
    output_data = base_definitions.download_definition('AllergyIntolerance', '3.0.2')
    expected_data = '{}'
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.download_definition',
            lambda resource_type, version: {'responseType': 'AllergyIntolerance'})
@mock.patch('src.lib.base_definitions.resource_cache', {})
def test_get_definition_valid_not_found():
    output_data = base_definitions.get_definition('AllergyIntolerance', '3.0.2')
    expected_data = {'responseType': 'AllergyIntolerance'}
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.resource_cache',
            {'AllergyIntolerance3.0.2': {'responseType': 'AllergyIntolerance'}})
def test_get_definition_valid_found():
    output_data = base_definitions.get_definition('AllergyIntolerance', '3.0.2')
    expected_data = {'responseType': 'AllergyIntolerance'}
    assert output_data == expected_data


def test_search_definition_valid(data_domainresource_stu3_base_profile):
    output_data = base_definitions.search_definition(data_domainresource_stu3_base_profile,
                                                     'DomainResource.extension',
                                                     'slicing')
    expected_data = {'discriminator': [{'type': 'value', 'path': 'url'}],
                     'description': 'Extensions are always sliced by (at least) url',
                     'rules': 'open'}
    assert output_data == expected_data


def test_search_definition_not_found(data_domainresource_stu3_base_profile):
    output_data = base_definitions.search_definition(data_domainresource_stu3_base_profile,
                                                     'DomainResource.extension',
                                                     'NOT_A_COMPONENT')
    expected_data = {}
    assert output_data == expected_data


def test_search_definition_empty_snapshot(data_snapshot_element_empty, data_input_empty):
    with pytest.raises(ValueError) as exception_info:
        base_definitions.search_definition(data_snapshot_element_empty, data_input_empty, data_input_empty)
    assert 'No elements found in base definition' in str(exception_info)


def test_search_definition_no_snapshot(data_snapshot_element_empty, data_input_empty):
    data_snapshot_element_empty.pop('snapshot')
    with pytest.raises(ValueError) as exception_info:
        base_definitions.search_definition(data_snapshot_element_empty, data_input_empty, data_input_empty)
    assert 'Snapshot is missing from base definition' in str(exception_info)


def test_search_definition_empty_input(data_input_empty):
    output_data = base_definitions.search_definition(data_input_empty, data_input_empty, data_input_empty)
    expected_data = {}
    assert output_data == expected_data


def test_get_element_base_path(data_left_right_elements_operands_base_path):
    output_data = base_definitions.get_element_base_path(data_left_right_elements_operands_base_path)
    expected_data = {'path': 'DomainResource.extension', 'min': 0, 'max': '*'}
    assert output_data == expected_data


def test_get_element_base_path_no_base_path(data_left_right_elements_operands_no_base_path):
    output_data = base_definitions.get_element_base_path(data_left_right_elements_operands_no_base_path)
    expected_data = None
    assert output_data == expected_data


def test_get_element_base_path_non_matching_base_path(data_left_right_elements_operands_non_matching_base_path):
    with pytest.raises(ValueError) as exception_info:
        base_definitions.get_element_base_path(data_left_right_elements_operands_non_matching_base_path)
    assert 'Corresponding elements do not have the same base path definition' in str(exception_info)


@mock.patch('src.lib.base_definitions.get_definition',
            lambda resource_type,
                   version: '{"snapshot": {"element": [{"id": "DomainResource.extension", "min": 0}]}}')
def test_check_defined_base_path(data_left_right_elements_operands_base_path):
    output_data = base_definitions.check_defined_base_path(data_left_right_elements_operands_base_path,
                                                           'min',
                                                           '3.0.2')
    expected_data = 0
    assert output_data == expected_data


def test_check_defined_base_path_no_base_path(data_left_right_elements_operands_no_base_path):
    output_data = base_definitions.check_defined_base_path(data_left_right_elements_operands_no_base_path,
                                                           'min',
                                                           '3.0.2')
    expected_data = {}
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.get_definition',
            lambda resource_type,
                   version: '{"snapshot": {"element": [{"id": "AllergyIntolerance.extension", "min": 0}]}}')
def test_check_base_definition(data_left_right_elements_operands_base_path):
    output_data = base_definitions.check_base_definition(data_left_right_elements_operands_base_path,
                                                         'min',
                                                         '3.0.2')
    expected_data = 0
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.get_definition',
            lambda resource_type,
                   version: '{"snapshot": {"element": [{"id": "AllergyIntolerance.extension", "min": 0}]}}')
def test_get_base_component_check_base_definition_found(data_left_right_elements_operands_base_path):
    output_data = base_definitions.get_base_component(data_left_right_elements_operands_base_path,
                                                      'min',
                                                      '3.0.2')
    expected_data = 0
    assert output_data == expected_data


@mock.patch('src.lib.base_definitions.get_definition',
            lambda resource_type,
                   version: '{"snapshot": {"element": [{"id": "DomainResource.extension", "min": 0}]}}')
def test_get_base_component_check_defined_base_path_found(data_left_right_elements_operands_base_path):
    output_data = base_definitions.get_base_component(data_left_right_elements_operands_base_path,
                                                      'min',
                                                      '3.0.2')
    expected_data = 0
    assert output_data == expected_data
