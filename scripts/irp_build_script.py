"""
PDF document building script for all InfoSecDocs

Usage:
    irp_build_script <filepath> <company_name>
    irp_build_script -h | --help
    irp_build_script --version

Options:
    -h --help       Show this screen.
    --version       Show version.
"""
import re

from docopt import docopt

def read(filename):
    temp_file = open(filename, 'r')
    return temp_file.read()

def input_processor(var):
    return var.strip()

def replace(text, to_replace, replacement):
    return re.sub(to_replace, replacement, text)

def exporter(filename, company_name):
    pass


if __name__ == '__main__':
    company_name = input_processor(input("Company name for document: "))

    pre_complied = read('Incident Response/incident_response_plan.md')
    
    compiled = replace(pre_complied, "\{\{ COMPANY NAME }}", company_name)

    # export()