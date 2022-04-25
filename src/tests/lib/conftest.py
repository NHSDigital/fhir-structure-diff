import pytest
from pytest_lazyfixture import lazy_fixture
import os, json

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = TEST_DIR + '/../data'


@pytest.fixture
def data_dir():
    return DATA_DIR


@pytest.fixture
def data_allergyintolerance_stu3_base_profile() -> dict:
    test_data = open(DATA_DIR + '/allergyintolerance.profile.json')
    return json.load(test_data)


@pytest.fixture
def data_domainresource_stu3_base_profile() -> dict:
    test_data = open(DATA_DIR + '/domainresource.profile.json')
    return json.load(test_data)


@pytest.fixture
def data_allergyintolerance_stu3_meta() -> tuple:
    return '3.0.2', 'AllergyIntolerance', 'AllergyIntolerance'


@pytest.fixture
def data_snapshot_element() -> dict:
    test_data = open(DATA_DIR + '/data_snapshot_element.json')
    return json.load(test_data)


@pytest.fixture
def data_snapshot_element_empty() -> dict:
    return \
        {
            "resourceType": "StructureDefinition",
            "snapshot": {
            }
        }


@pytest.fixture
def data_snapshot_element_choices() -> dict:
    test_data = open(DATA_DIR + '/data_snapshot_element_choices.json')
    return json.load(test_data)


@pytest.fixture(params=[[], {}, None])
def data_input_empty(request):
    return request.param


@pytest.fixture(params=[[], None])
def data_input_empty_no_dict(request):
    return request.param


@pytest.fixture(params=[
    'abc',
    123,
    True,
    False,
    ('not', 'json'),
    ''
    '2.0.1'
])
def data_primitive_invalid(request):
    return request.param


@pytest.fixture(params=[
    lazy_fixture('data_input_empty'),
    lazy_fixture('data_primitive_invalid')
])
def data_invalid(request):
    return request.param


@pytest.fixture(params=[
    lazy_fixture('data_input_empty_no_dict'),
    lazy_fixture('data_primitive_invalid')
])
def data_invalid_no_empty_dict(request):
    return request.param


@pytest.fixture(params=[
    (
            [{'valid': ['object', 'containing']}, {'lists': {'and': 'dicts'}}],
            {'valid': ['object', 'containing'], 'lists': {'and': 'dicts'}}
    ),
    (
            [{'object': ['containing', 'a', 'list']}],
            {'object': ['containing', 'a', 'list']}
    ),
    (
            [{'simpleString': 'object'}],
            {'simpleString': 'object'}
    ),
    (
            [{'integer': 123}],
            {'integer': 123}
    )
])
def data_list_contains_dict_input_and_output(request):
    return request.param


@pytest.fixture(params=[
    lazy_fixture('data_list_contains_dict_input_and_output'),
    ([[{'valid': ['object', 'containing']}], {'lists': {'and': 'dicts'}}], ['NOT_USED']),  # Not valid FHIR
])
def data_list_contains_dict(request):
    return request.param[0]


@pytest.fixture(params=[
    lazy_fixture('data_snapshot_element'),
    lazy_fixture('data_snapshot_element_choices'),
    lazy_fixture('data_list_contains_dict')
])
def data_contains_dict(request):
    return request.param


@pytest.fixture(params=[
    ['string array'],
    ['three', 'string', 'array']
    [1],
    [0, 1]
])
def data_does_not_contain_dict(request):
    return request.param


@pytest.fixture
def data_left_elements_valid():
    test_data = open(DATA_DIR + '/data_left_elements_valid.json')
    return json.load(test_data)


@pytest.fixture
def data_right_elements_valid():
    test_data = open(DATA_DIR + '/data_right_elements_valid.json')
    return json.load(test_data)


@pytest.fixture
def data_elements_valid_with_or_without_base_path():
    test_data = open(DATA_DIR + '/data_elements_valid_with_or_without_base_path.json')
    return json.load(test_data)


@pytest.fixture
def data_left_right_elements_aligned_valid():
    return \
        [
            {
                "AllergyIntolerance.extension": (
                    {
                        "id": "AllergyIntolerance.extension",
                        "path": "AllergyIntolerance.extension",
                        "slicing": {
                            "discriminator": [{"type": "value", "path": "url"}],
                            "rules": "closed",
                        },
                    },
                    {
                        "id": "AllergyIntolerance.extension",
                        "path": "AllergyIntolerance.extension",
                        "slicing": {
                            "discriminator": [{"type": "value", "path": "url"}],
                            "rules": "open",
                        },
                    },
                )
            },
            {
                "AllergyIntolerance.extension:encounter": (
                    {
                        "id": "AllergyIntolerance.extension:encounter",
                        "path": "AllergyIntolerance.extension",
                        "sliceName": "encounter",
                        "max": "1",
                        "type": [
                            {
                                "code": "Extension",
                                "profile": "http://hl7.org/fhir/StructureDefinition/encounter-associatedEncounter-LEFT",
                            }
                        ],
                    },
                    {
                        "id": "AllergyIntolerance.extension:encounter",
                        "path": "AllergyIntolerance.extension",
                        "sliceName": "encounter",
                        "max": "*",
                        "type": [
                            {
                                "code": "Extension",
                                "profile": "http://hl7.org/fhir/StructureDefinition/encounter-associatedEncounter-RIGHT",
                            }
                        ],
                    },
                )
            },
            {
                "AllergyIntolerance.extension:allergyEnd": (
                    {
                        "id": "AllergyIntolerance.extension:allergyEnd",
                        "path": "AllergyIntolerance.extension",
                        "sliceName": "allergyEnd",
                        "max": "1",
                        "type": [
                            {
                                "code": "Extension",
                                "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-CareConnect-AllergyIntoleranceEnd-1",
                            }
                        ],
                    },
                    {
                        "id": "AllergyIntolerance.extension:allergyEnd",
                        "path": "AllergyIntolerance.extension",
                        "sliceName": "allergyEnd",
                        "max": "1",
                        "type": [
                            {
                                "code": "Extension",
                                "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-CareConnect-GPC-AllergyIntoleranceEnd-1",
                            }
                        ],
                    },
                )
            },
            {
                "AllergyIntolerance.extension:evidence": (
                    {
                        "id": "AllergyIntolerance.extension:evidence",
                        "path": "AllergyIntolerance.extension",
                        "sliceName": "evidence",
                        "max": "1",
                        "type": [
                            {
                                "code": "Extension",
                                "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-CareConnect-Evidence-1",
                            }
                        ],
                    },
                    {},
                )
            },
            {
                "AllergyIntolerance.identifier.system": (
                    {},
                    {
                        "id": "AllergyIntolerance.identifier.system",
                        "path": "AllergyIntolerance.identifier.system",
                        "min": 1,
                    },
                )
            },
        ]


@pytest.fixture
def data_left_right_elements_operands_left_base_path():
    return \
        {
            "AllergyIntolerance.extension": (
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    },
                    "base": {"path": "DomainResource.extension", "min": 0, "max": "*"},
                },
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    },
                    "base": {"path": "DomainResource.extension", "min": 0, "max": "*"},
                },
            )
        }


@pytest.fixture
def data_left_right_elements_operands_right_base_path():
    return \
        {
            "AllergyIntolerance.extension": (
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    }
                },
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    },
                    "base": {"path": "DomainResource.extension", "min": 0, "max": "*"},
                },
            )
        }


@pytest.fixture
def data_left_right_elements_operands_non_matching_base_path():
    return \
        {
            "AllergyIntolerance.extension": (
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    },
                    "base": {"path": "non_matching_resource.extension", "min": 0, "max": "*"},
                },
                {
                    "id": "AllergyIntolerance.extension",
                    "path": "AllergyIntolerance.extension",
                    "slicing": {
                        "discriminator": [{"type": "value", "path": "url"}],
                        "rules": "open",
                    },
                    "base": {"path": "DomainResource.extension", "min": 0, "max": "*"},
                },
            )
        }


@pytest.fixture(params=[
    lazy_fixture('data_left_right_elements_operands_left_base_path'),
    lazy_fixture('data_left_right_elements_operands_right_base_path')
])
def data_left_right_elements_operands_base_path(request):
    return request.param


@pytest.fixture(params=[
    lazy_fixture('data_left_right_elements_aligned_valid')
])
def data_left_right_elements_operands_no_base_path(request):
    return request.param[0]


@pytest.fixture
def data_extract_diff_elements_valid():
    test_data = open(DATA_DIR + '/data_extract_diff_elements_valid.json')
    return json.load(test_data)


@pytest.fixture
def data_diff_elements_valid():
    test_data = open(DATA_DIR + '/data_diff_elements_valid.json')
    return json.load(test_data)


@pytest.fixture(params=[
    lazy_fixture('data_diff_elements_valid'),
    lazy_fixture('data_extract_diff_elements_valid'),
    lazy_fixture('data_snapshot_element'),
    lazy_fixture('data_snapshot_element_empty'),
    lazy_fixture('data_right_elements_valid'),
    lazy_fixture('data_left_elements_valid')
])
def data_dicts(request):
    return request.param

# 'slicing'
# 'AllergyIntolerance.extension'
