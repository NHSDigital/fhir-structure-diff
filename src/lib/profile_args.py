import argparse
import os
from .structuredefinition_reader import read_profile


DEFAULT_TEMPLATE = '/../templates/markdown.md.jinja2'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("leftprofile", type=str, help="Filename of left-hand profile to compare")
    parser.add_argument("rightprofile", type=str, help="Filename of right-hand profile to compare")
    # Only specifying major version, since the def's are being downloaded.  Would probably need more complex package
    # management for finer control of the base versions
    parser.add_argument("-lv", "--leftversion", type=int, help="Base FHIR (only major) version of left-hand profile.")
    parser.add_argument("-rv", "--rightversion", type=int, help="Base FHIR (only major) version of right-hand profile.")
    parser.add_argument("-t", "--template", type=str, help="Jinja2 template.  Provide custom template for output. "
                                                           "Name before extension of template will be output filename")
    args = parser.parse_args()

    left, left_ver, left_name, left_type = read_profile(args.leftprofile)
    right, right_ver, right_name, right_type = read_profile(args.rightprofile)
    left_ver, right_ver = check_resource_properties(left_type, right_type, left_ver, right_ver, args)
    template = get_template(args)

    args.leftprofile = left
    args.rightprofile = right
    args.leftversion = left_ver
    args.rightversion = right_ver
    args.template = template

    return args


def check_resource_properties(left_type, right_type, left_version, right_version, args):
    if left_type != right_type:
        raise ValueError("Profile resource types do not match.\n" 
                         "Left resource type: " + left_type +
                         "Right resource type: " + right_type + "\n")

    if not left_version and not args.leftversion:
        raise ValueError("Left version is not supplied in the StructureDefinition and must be supplied.\n" 
                         "Supplied left version: " + args.leftprofile + "\n")

    if not right_version and not args.rightversion:
        raise ValueError("Left version is not supplied in the StructureDefinition and must be supplied.\n" 
                         "Supplied left version: " + args.rightprofile + "\n")

    if args.leftversion and left_version and int(left_version[0]) != int(args.leftversion):
        raise ValueError("Supplied left-hand version does not match version read from profile.\n" 
                         "Supplied left version: " + args.leftversion +
                         "Left version read from profile: " + left_version[0] + "\n")

    if args.rightversion and right_version and int(right_version[0]) != int(args.rightversion):
        raise ValueError("Supplied right-hand version does not match version read from profile.\n" 
                         "Supplied right version: " + args.rightversion +
                         "Right version read from profile: " + right_version[0] + "\n")

    left_ver = left_version if left_version else args.leftversion
    right_ver = right_version if right_version else args.rightversion

    if int(left_ver[0]) - int(right_ver[0]) > 1:
        raise NotImplementedError("Not Supported. Profile resource versions are more than one version apart.\n" 
                                  "Left version: " + left_version + ", resource type: " + left_type + "\n" +
                                  "Right version: " + right_version + ", resource type: " + right_type + "\n")

    return left_ver, right_ver


def get_versions(left_version, right_version, args):
    if not left_version and not args.leftversion:
        raise NameError("No FHIR version found or specified for the left-hand profile")

    if not right_version and not args.rightversion:
        raise NameError("No FHIR version found or specified for the right-hand profile")

    if not left_version:
        left_version = args.leftversion

    if not right_version:
        right_version = args.rightversion

    return left_version, right_version


def get_template(args):
    if args.template:
        return args.template
    else:
        return os.path.dirname(os.path.realpath(__file__)) + DEFAULT_TEMPLATE
