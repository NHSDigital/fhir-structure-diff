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


@mock.patch('src.lib.base_definitions.resource_cache', {'AllergyIntolerance3.0.2': {'responseType': 'AllergyIntolerance'}})
def test_get_definition_valid_found():
    output_data = base_definitions.get_definition('AllergyIntolerance', '3.0.2')
    expected_data = {'responseType': 'AllergyIntolerance'}
    assert output_data == expected_data
