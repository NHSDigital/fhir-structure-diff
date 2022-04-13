import json
import os

# Really useful package for converting xml to a dict, but additional logic will be needed to end up
# with the same format as a straight json, given differences in naming e.g. resourceType
# import xmltodict


def read_profile(filename):
    input_file_extension = os.path.splitext(filename)[1]

    if input_file_extension.lower() == '.json':
        profile = read_json(filename)
        # Must at least have a differential
        check_profile(profile, 'differential')
        return profile, *get_profile_meta(profile)

    elif input_file_extension.lower() == '.xml':
        raise NotImplementedError('XML type not implemented.')

    elif input_file_extension.lower() == '.ttl':
        raise NotImplementedError('Turtle type not implemented.')

    else:
        raise TypeError('Unrecognised file extension: ' + input_file_extension)


def read_json(filename):
    try:
        json_str = json.load(open(filename))

    except ValueError as e:
        raise ValueError(filename + ' is not value json.  Exception: + ' + str(e))

    except TypeError as e:
        raise TypeError(filename + ' cause a TypeError when trying to load it as a JSON file.  '
                                   'Exception: + ' + str(e))
    return json_str


def check_profile(profile, view):
    if not isinstance(profile, dict):
        raise ValueError('Unexpected data types for element diff.\n\nProfile -> ' + str(profile))

    if view not in profile:
        raise ValueError('No ' + view + 'section found profile.\n\nProfile -> ' +
                         json.dumps(profile, indent=2))

    if 'element' not in profile[view]:
        raise ValueError('No elements in ' + view + ' section.\n\nProfile -> ' +
                         json.dumps(profile, indent=2))


def get_fhir_version(profile):
    if isinstance(profile, dict) and 'fhirVersion' in profile:
        return profile['fhirVersion']

    return None


def get_profile_name(profile):
    if not isinstance(profile, dict) or 'name' not in profile:
        raise ValueError('No name in profile.\n\nProfile -> ' +
                         json.dumps(profile, indent=2))

    return profile['name']


def get_profile_type(profile):
    if not isinstance(profile, dict) or 'type' not in profile:
        raise ValueError('No defined type in profile.\n\nProfile -> ' +
                         json.dumps(profile, indent=2))

    return profile['type']


def get_profile_meta(profile):
    return get_fhir_version(profile), \
           get_profile_name(profile), \
           get_profile_type(profile)
