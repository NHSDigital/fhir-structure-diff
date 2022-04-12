import pytest

from ....lib import profile_elements


def test_search_list_for_dict(data_contains_dict):
    output_data = profile_elements.search_list_for_dict(data_contains_dict)
    expected_data = True
    assert output_data == expected_data


def test_search_list_for_dict_valid_json(data_does_not_contain_dict):
    output_data = profile_elements.search_list_for_dict(data_does_not_contain_dict)
    expected_data = False
    assert output_data == expected_data


def test_search_list_for_dict_invalid(data_invalid):
    output_data = profile_elements.search_list_for_dict(data_invalid)
    expected_data = False
    assert output_data == expected_data


def test_is_or_contains_dict(data_contains_dict):
    output_data = profile_elements.is_or_contains_dict(data_contains_dict)
    expected_data = True
    assert output_data == expected_data


def test_is_or_contains_dict_valid_json(data_does_not_contain_dict):
    output_data = profile_elements.is_or_contains_dict(data_does_not_contain_dict)
    expected_data = False
    assert output_data == expected_data


def test_is_or_contains_dict_invalid(data_invalid):
    output_data = profile_elements.is_or_contains_dict(data_invalid)
    expected_data = False
    assert output_data == expected_data


def test_is_valid_dict(data_contains_dict):
    output_data = profile_elements.is_valid_dict(data_contains_dict)
    expected_data = True
    assert output_data == expected_data


def test_is_valid_no_dict_valid_json(data_does_not_contain_dict):
    output_data = profile_elements.is_valid_dict(data_does_not_contain_dict)
    expected_data = False
    assert output_data == expected_data


def test_is_valid_dict_invalid(data_invalid):
    output_data = profile_elements.is_valid_dict(data_invalid)
    expected_data = False
    assert output_data == expected_data


def test_align_elements_valid(data_left_elements_valid,
                              data_right_elements_valid,
                              data_left_right_elements_aligned_valid):
    output_data = profile_elements.align_elements(data_left_elements_valid,
                                                  data_right_elements_valid)
    expected_data = data_left_right_elements_aligned_valid
    assert output_data == expected_data


def test_align_elements_invalid(data_invalid):
    with pytest.raises(TypeError) as exception_info:
        profile_elements.align_elements(data_invalid, data_invalid)
    assert 'Unexpected data in profile_elements.align_elements' in str(exception_info)


def test_add_snapshot_elements_to_diff(data_allergyintolerance_stu3_base_profile,
                                       data_right_elements_valid,
                                       data_elements_valid_with_or_without_base_path):
    output_data = profile_elements.add_snapshot_elements_to_diff(data_allergyintolerance_stu3_base_profile,
                                                                 data_right_elements_valid)
    expected_data = data_elements_valid_with_or_without_base_path
    assert output_data == expected_data


def test_add_snapshot_elements_to_diff_empty_input(data_input_empty):
    with pytest.raises(ValueError) as exception_info:
        profile_elements.add_snapshot_elements_to_diff(data_input_empty, data_input_empty)
    assert 'Empty profile passed' in str(exception_info)


def test_add_snapshot_elements_to_diff_empty_snapshot(data_snapshot_element_empty):
    with pytest.raises(ValueError) as exception_info:
        profile_elements.add_snapshot_elements_to_diff(data_snapshot_element_empty, data_snapshot_element_empty)
    assert 'Elements are missing in profile' in str(exception_info)


def test_extract_diff_elements(data_extract_diff_elements_valid,
                               data_diff_elements_valid):
    output_data = profile_elements.extract_diff_elements(data_extract_diff_elements_valid)
    expected_data = data_diff_elements_valid
    assert output_data == expected_data


def test_extract_elements(data_extract_diff_elements_valid,
                          data_diff_elements_valid):
    output_data = profile_elements.extract_elements(data_extract_diff_elements_valid)
    expected_data = data_diff_elements_valid
    assert output_data == expected_data
