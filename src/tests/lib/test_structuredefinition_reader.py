import pytest

from ...lib import structuredefinition_reader


def test_get_profile_type_valid(data_allergyintolerance_stu3_base_profile):
    output_data = structuredefinition_reader.get_profile_type(data_allergyintolerance_stu3_base_profile)
    expected_data = 'AllergyIntolerance'
    assert output_data == expected_data


def test_get_profile_type_invalid(data_invalid):
    with pytest.raises(ValueError) as exception_info:
        structuredefinition_reader.get_profile_type(data_invalid)
    assert 'No defined type in profile' in str(exception_info)


def test_get_profile_name_valid(data_allergyintolerance_stu3_base_profile):
    output_data = structuredefinition_reader.get_profile_type(data_allergyintolerance_stu3_base_profile)
    expected_data = 'AllergyIntolerance'
    assert output_data == expected_data


def test_get_profile_name_invalid(data_invalid):
    with pytest.raises(ValueError) as exception_info:
        structuredefinition_reader.get_profile_name(data_invalid)
    assert 'No name in profile' in str(exception_info)


def test_get_fhir_version_valid(data_allergyintolerance_stu3_base_profile):
    output_data = structuredefinition_reader.get_fhir_version(data_allergyintolerance_stu3_base_profile)
    expected_data = '3.0.2'
    assert output_data == expected_data


def test_get_fhir_version_invalid(data_invalid):
    output_data = structuredefinition_reader.get_fhir_version(data_invalid)
    expected_data = None
    assert output_data == expected_data


def test_check_profile_invalid(data_invalid_no_empty_dict):
    with pytest.raises(ValueError) as exception_info:
        structuredefinition_reader.check_profile(data_invalid_no_empty_dict, data_invalid_no_empty_dict)
    assert 'Unexpected data types for element diff' in str(exception_info)


