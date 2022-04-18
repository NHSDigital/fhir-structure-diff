import argparse
import os
from jinja2 import Template
from lib import profile_diff as pd
from lib import structuredefinition_reader as sdr


def render_diff(args):
    left, l_version, l_name, l_defined_type = sdr.read_profile(args.leftprofile)
    right, r_version, r_name, r_defined_type = sdr.read_profile(args.rightprofile)

    template = get_template(args)

    element_level_diff = pd.element_diff(left, right)
    component_level_diff = pd.component_diff(left, right, l_version)  # TODO support multiple versions

    diff_template = open(template).read()
    t = Template(diff_template)
    diff_rendered = t.render(resource_type=l_defined_type,
                             left_profile=l_name,
                             left_version=l_version,
                             right_profile=r_name,
                             right_version=r_version,
                             element_level_diff=element_level_diff,
                             component_results=component_level_diff)

    diff_file = './' + os.path.basename(template).rsplit('.', 1)[0]
    diff = open(diff_file, 'w')
    diff.write(diff_rendered)
    print(diff_rendered)


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

    return parser.parse_args()


def get_versions(l_version, r_version, args):
    if not l_version and not args.leftversion:
        raise NameError("No FHIR version found or specified for the left-hand profile")

    if not r_version and not args.rightversion:
        raise NameError("No FHIR version found or specified for the right-hand profile")

    if not l_version:
        l_version = args.leftversion

    if not r_version:
        r_version = args.rightversion

    return l_version, r_version


def get_template(args):
    if args.template:
        return args.template
    else:
        return os.path.dirname(os.path.realpath(__file__)) + '/templates/markdown.md.jinja2'


def main():
    args = get_args()
    render_diff(args)


if __name__ == "__main__":
    main()
