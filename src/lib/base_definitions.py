import json
import requests

# Constants for base profile URL's.
# Might be worth adding config for this,
# but as this is only used here and none
# of this is sensitive, no need for now
BASE_URL = 'https://hl7.org/fhir/'
BASE_FILE_TYPE = '.profile.json'

# Again, only need a cache here, slightly more cohesive and would be easy to move if needed
resource_cache = {}
# TODO. Could make this more flexible to allow for using cache as opposed to web
#       Could use npm
#       Naming convention seems to be much messier
#       For simplicity leaving this for now


def get_base_component(element_operands, component, version):

    base_component = check_base_definition(element_operands, component, version)
    if base_component != {}:
        return base_component

    base_component = check_defined_base_path(element_operands, component, version)
    if base_component != {}:
        return base_component

    base_component = check_parent_element(element_operands, component, version)
    if base_component != {}:
        return base_component

    # Finally
    return check_parent_element_type(element_operands, component, version)


def check_base_definition(element_operands, component, version):
    element_key = str(*element_operands.keys())
    resource_type = element_key.split('.')[0]
    base_definition = json.loads(get_definition(resource_type, version))  # TODO pull fhirVersion out of operands

    return search_definition(base_definition, element_key, component)


def check_defined_base_path(element_operands, component, version):
    element_base_path = get_element_base_path(element_operands)

    if element_base_path:
        resource_type = element_base_path['path'].split('.')[0]
        base_element_definition = json.loads(get_definition(resource_type, version))
        return search_definition(base_element_definition, element_base_path['path'], component)

    return {}


def check_parent_element(element_operands, component, version):
    element_key = str(*element_operands.keys())
    resource_type = element_key.split('.')[-2]
    parent_element_definition = json.loads(get_definition(resource_type, version))

    sub_element = resource_type + '.' + element_key.split('.')[-1]
    return search_definition(parent_element_definition, sub_element, component)


def check_parent_element_type(element_operands, component, version):
    element_key = str(*element_operands.keys())
    resource_type = element_key.split('.')[0]
    base_definition = json.loads(get_definition(resource_type, version))

    parent_element = element_key.rsplit('.', 1)[0]
    element_base_definition = search_definition(base_definition, parent_element, 'type')
    for type_entry in element_base_definition:
        if 'code' in type_entry:
            resource_type = type_entry['code']
            sub_element_base_definition = json.loads(get_definition(resource_type, version))
            sub_element = resource_type + '.' + element_key.split('.')[-1]
            element_base_component = search_definition(sub_element_base_definition, sub_element, component)
            # First match, return.  TODO not sure about this, test it throughly...
            if element_base_component != {}:
                return element_base_component

    return {}


def get_element_base_path(element_operands):
    left_element = tuple(*element_operands.values())[0]
    right_element = tuple(*element_operands.values())[1]

    if 'base' in left_element and 'base' in right_element and \
            left_element and right_element and \
            (left_element['base'] != right_element['base']):
        raise ValueError('Corresponding elements do not have the same base path definition\n\n' +
                         'Left element -->\n\n' + left_element +
                         'Right element -->\n\n' + right_element)

    if 'base' in left_element:
        return left_element['base']

    if 'base' in right_element:
        return right_element['base']

    return None


def search_definition(base_definition, element, component):
    if not base_definition:
        return {}
    if 'snapshot' not in base_definition:
        raise ValueError('Snapshot is missing from base definition.\n\nBase definition -->\n\n' +
                         base_definition)
    if 'element' not in base_definition['snapshot']:
        raise ValueError('No elements found in base definition.\n\nBase definition -->\n\n' +
                         base_definition)

    for e in base_definition['snapshot']['element']:
        if 'id' in e and e['id'].lower() == element.lower():
            if component in e.keys():
                return e[component]

    return {}


def get_definition(resource_type, version):
    if resource_type + version not in resource_cache:
        return download_definition(resource_type, version)

    return resource_cache[resource_type + version]


def download_definition(resource_type, version):
    profile_url = get_profile_url(resource_type, version)

    # Allow exceptions to be raised, i.e. connection failure etc...
    response = requests.get(profile_url)

    if response.ok:
        resource_cache[resource_type + version] = response.content.decode('utf-8')
        return resource_cache[resource_type + version]
    else:
        # requests will have raised an exception on a connection error, so this just
        # stops attempts to download invalid types by storing an empty json object
        resource_cache[resource_type + version] = '{}'
        return resource_cache[resource_type + version]


def get_profile_url(resource_type, version):
    if not resource_type or \
            not version or \
            not str(version)[0].isnumeric() or \
            not isinstance(resource_type, str) or \
            not isinstance(version, str):
        raise ValueError('Unknown FHIR version and resourceType\nVersion: ' +
                         str(version) + ', resourceType: ' + str(resource_type))

    version_map = {
        0: 'DSTU1/',
        1: 'DSTU2/',
        3: 'STU3/',
        4: 'R4/'
    }
    fhir_version = version_map.get(int(version[0]), None)

    if not fhir_version:
        raise ValueError('Unknown FHIR version: ' + version)

    return BASE_URL + fhir_version + resource_type + BASE_FILE_TYPE
