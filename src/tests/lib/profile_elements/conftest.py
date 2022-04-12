import pytest
from pytest_lazyfixture import lazy_fixture
import os, json

TEST_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def data_allergyintolerance_stu3_base_profile() -> dict:
    test_data = open(TEST_DIR + '/../../data/allergyintolerance.profile.json')
    return json.load(test_data)


@pytest.fixture
def data_snapshot_element() -> dict:
    return \
        {
            "resourceType": "StructureDefinition",
            "snapshot": {
                "element": [
                    {
                        "id": "BasicTest",
                        "path": "This element and others not required"
                    },
                    {
                        "id": "BasicTest.id",
                        "other": "This key wouldn't exist"
                    },
                    {
                        "id": "BasicTest.id.3rdlevel"
                    }
                ]
            }
        }


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
    return \
        {
            "id": "Communication.payload.content[x]",
            "type": [
                {
                    "code": "string"
                },
                {
                    "code": "Attachment"
                },
                {
                    "code": "Reference",
                    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Resource"
                }
            ]
        }


@pytest.fixture(params=[[], None])
def data_input_empty(request):
    return request.param


@pytest.fixture(params=[
    'abc',
    123,
    True,
    False,
    ('not', 'json')
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
    return \
        {
            "AllergyIntolerance.extension": {
                "id": "AllergyIntolerance.extension",
                "path": "AllergyIntolerance.extension",
                "slicing": {
                    "discriminator": [
                        {
                            "type": "value",
                            "path": "url"
                        }
                    ],
                    "rules": "closed"
                }
            },
            "AllergyIntolerance.extension:encounter": {
                "id": "AllergyIntolerance.extension:encounter",
                "path": "AllergyIntolerance.extension",
                "sliceName": "encounter",
                "max": "1",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "http://hl7.org/fhir/StructureDefinition/encounter-associatedEncounter-LEFT"
                    }
                ]
            },
            "AllergyIntolerance.extension:allergyEnd": {
                "id": "AllergyIntolerance.extension:allergyEnd",
                "path": "AllergyIntolerance.extension",
                "sliceName": "allergyEnd",
                "max": "1",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-CareConnect-AllergyIntoleranceEnd-1"
                    }
                ]
            }
        }


@pytest.fixture
def data_right_elements_valid():
    return \
        {
            "AllergyIntolerance.extension": {
                "id": "AllergyIntolerance.extension",
                "path": "AllergyIntolerance.extension",
                "slicing": {
                    "discriminator": [
                        {
                            "type": "value",
                            "path": "url"
                        }
                    ],
                    "rules": "open"
                }
            },
            "AllergyIntolerance.extension:encounter": {
                "id": "AllergyIntolerance.extension:encounter",
                "path": "AllergyIntolerance.extension",
                "sliceName": "encounter",
                "max": "*",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "http://hl7.org/fhir/StructureDefinition/encounter-associatedEncounter-RIGHT"
                    }
                ]
            },
            "AllergyIntolerance.extension:allergyEnd": {
                "id": "AllergyIntolerance.extension:allergyEnd",
                "path": "AllergyIntolerance.extension",
                "sliceName": "allergyEnd",
                "max": "1",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-CareConnect-GPC-AllergyIntoleranceEnd-1"
                    }
                ]
            }
        }


@pytest.fixture
def data_elements_valid_with_or_without_base_path(request):
    return \
        {
            "AllergyIntolerance.extension": {
                "id": "AllergyIntolerance.extension",
                "path": "AllergyIntolerance.extension",
                "slicing": {
                    "discriminator": [
                        {
                            "type": "value",
                            "path": "url"
                        }
                    ],
                    "rules": "open"
                },
                "base": {
                    "path": "DomainResource.extension",
                    "min": 0,
                    "max": "*"
                }
            },
            "AllergyIntolerance.extension:encounter": {
                "id": "AllergyIntolerance.extension:encounter",
                "path": "AllergyIntolerance.extension",
                "sliceName": "encounter",
                "max": "*",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "http://hl7.org/fhir/StructureDefinition/encounter-associatedEncounter-RIGHT"
                    }
                ]
            },
            "AllergyIntolerance.extension:allergyEnd": {
                "id": "AllergyIntolerance.extension:allergyEnd",
                "path": "AllergyIntolerance.extension",
                "sliceName": "allergyEnd",
                "max": "1",
                "type": [
                    {
                        "code": "Extension",
                        "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-CareConnect-GPC-AllergyIntoleranceEnd-1"
                    }
                ]
            }
        }


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
                        }
                    },
                    {
                        "id": "AllergyIntolerance.extension",
                        "path": "AllergyIntolerance.extension",
                        "slicing": {
                            "discriminator": [{"type": "value", "path": "url"}],
                            "rules": "open",
                        }
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
                        ]
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
                        ]
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
                        ]
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
                        ]
                    },
                )
            }
        ]


@pytest.fixture
def data_extract_diff_elements_valid():
    return \
        {
            "differential": {
                "element": [
                    {
                        "id": "AllergyIntolerance",
                        "path": "AllergyIntolerance",
                        "short": "Allergy or Intolerance (generally: Risk of adverse reaction to a substance)",
                        "definition": "Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.",
                        "comment": "Substances include, but are not limited to: a therapeutic substance administered correctly at an appropriate dosage for the individual; food; material derived from plants or animals; or venom from insect stings.",
                        "alias": [
                            "Allergy",
                            "Intolerance",
                            "Adverse Reaction"
                        ],
                        "min": 0,
                        "max": "*",
                        "constraint": [
                            {
                                "key": "ait-1",
                                "severity": "error",
                                "human": "AllergyIntolerance.clinicalStatus SHALL be present if verificationStatus is not entered-in-error.",
                                "expression": "verificationStatus='entered-in-error' or clinicalStatus.exists()",
                                "xpath": "f:verificationStatus/@value='entered-in-error' or exists(f:clinicalStatus)"
                            },
                            {
                                "key": "ait-2",
                                "severity": "error",
                                "human": "AllergyIntolerance.clinicalStatus SHALL NOT be present if verification Status is entered-in-error",
                                "expression": "verificationStatus!='entered-in-error' or clinicalStatus.empty()",
                                "xpath": "f:verificationStatus/@value!='entered-in-error' or not(exists(f:clinicalStatus))"
                            }
                        ],
                        "mapping": [
                            {
                                "identity": "rim",
                                "map": "Observation[classCode=OBS, moodCode=EVN]"
                            },
                            {
                                "identity": "w5",
                                "map": "clinical.general"
                            }
                        ]
                    },
                    {
                        "id": "AllergyIntolerance.identifier",
                        "path": "AllergyIntolerance.identifier",
                        "short": "External ids for this item",
                        "definition": "This records identifiers associated with this allergy/intolerance concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation).",
                        "min": 0,
                        "max": "*",
                        "type": [
                            {
                                "code": "Identifier"
                            }
                        ],
                        "isSummary": True,
                        "mapping": [
                            {
                                "identity": "v2",
                                "map": "IAM-7"
                            },
                            {
                                "identity": "rim",
                                "map": "id"
                            },
                            {
                                "identity": "w5",
                                "map": "id"
                            }
                        ]
                    },
                    {
                        "id": "AllergyIntolerance.clinicalStatus",
                        "path": "AllergyIntolerance.clinicalStatus",
                        "short": "active | inactive | resolved",
                        "definition": "The clinical status of the allergy or intolerance.",
                        "comment": "This element is labeled as a modifier because the status contains the codes inactive and resolved that mark the AllergyIntolerance as not currently valid.",
                        "min": 0,
                        "max": "1",
                        "type": [
                            {
                                "code": "code"
                            }
                        ],
                        "condition": [
                            "ait-1",
                            "ait-2"
                        ],
                        "isModifier": True,
                        "isSummary": True,
                        "binding": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
                                    "valueString": "AllergyIntoleranceClinicalStatus"
                                }
                            ],
                            "strength": "required",
                            "description": "The clinical status of the allergy or intolerance.",
                            "valueSetReference": {
                                "reference": "http://hl7.org/fhir/ValueSet/allergy-clinical-status"
                            }
                        },
                        "mapping": [
                            {
                                "identity": "rim",
                                "map": "Observation ACT\n.inboundRelationship[typeCode=COMP].source[classCode=OBS, code=\"clinicalStatus\", moodCode=EVN].value"
                            },
                            {
                                "identity": "w5",
                                "map": "status"
                            }
                        ]
                    }
                ]
            }
        }


@pytest.fixture
def data_diff_elements_valid():
    return \
        {
            "AllergyIntolerance": {
                "id": "AllergyIntolerance",
                "path": "AllergyIntolerance",
                "short": "Allergy or Intolerance (generally: Risk of adverse reaction to a substance)",
                "definition": "Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.",
                "comment": "Substances include, but are not limited to: a therapeutic substance administered correctly at an appropriate dosage for the individual; food; material derived from plants or animals; or venom from insect stings.",
                "alias": ["Allergy", "Intolerance", "Adverse Reaction"],
                "min": 0,
                "max": "*",
                "constraint": [
                    {
                        "key": "ait-1",
                        "severity": "error",
                        "human": "AllergyIntolerance.clinicalStatus SHALL be present if verificationStatus is not entered-in-error.",
                        "expression": "verificationStatus='entered-in-error' or clinicalStatus.exists()",
                        "xpath": "f:verificationStatus/@value='entered-in-error' or exists(f:clinicalStatus)",
                    },
                    {
                        "key": "ait-2",
                        "severity": "error",
                        "human": "AllergyIntolerance.clinicalStatus SHALL NOT be present if verification Status is entered-in-error",
                        "expression": "verificationStatus!='entered-in-error' or clinicalStatus.empty()",
                        "xpath": "f:verificationStatus/@value!='entered-in-error' or not(exists(f:clinicalStatus))",
                    },
                ],
                "mapping": [
                    {"identity": "rim", "map": "Observation[classCode=OBS, moodCode=EVN]"},
                    {"identity": "w5", "map": "clinical.general"},
                ],
            },
            "AllergyIntolerance.identifier": {
                "id": "AllergyIntolerance.identifier",
                "path": "AllergyIntolerance.identifier",
                "short": "External ids for this item",
                "definition": "This records identifiers associated with this allergy/intolerance concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation).",
                "min": 0,
                "max": "*",
                "type": [{"code": "Identifier"}],
                "isSummary": True,
                "mapping": [
                    {"identity": "v2", "map": "IAM-7"},
                    {"identity": "rim", "map": "id"},
                    {"identity": "w5", "map": "id"},
                ],
            },
            "AllergyIntolerance.clinicalStatus": {
                "id": "AllergyIntolerance.clinicalStatus",
                "path": "AllergyIntolerance.clinicalStatus",
                "short": "active | inactive | resolved",
                "definition": "The clinical status of the allergy or intolerance.",
                "comment": "This element is labeled as a modifier because the status contains the codes inactive and resolved that mark the AllergyIntolerance as not currently valid.",
                "min": 0,
                "max": "1",
                "type": [{"code": "code"}],
                "condition": ["ait-1", "ait-2"],
                "isModifier": True,
                "isSummary": True,
                "binding": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
                            "valueString": "AllergyIntoleranceClinicalStatus",
                        }
                    ],
                    "strength": "required",
                    "description": "The clinical status of the allergy or intolerance.",
                    "valueSetReference": {
                        "reference": "http://hl7.org/fhir/ValueSet/allergy-clinical-status"
                    },
                },
                "mapping": [
                    {
                        "identity": "rim",
                        "map": 'Observation ACT\n.inboundRelationship[typeCode=COMP].source[classCode=OBS, code="clinicalStatus", moodCode=EVN].value',
                    },
                    {"identity": "w5", "map": "status"},
                ],
            },
        }
