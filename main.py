#/usr/bin/env python
""" jinja2-nxos-config

    Accepts arguments from YAML config file
    and generates a Jinja2 configuration
"""

import sys
import methods

def run():
    """Function docstring"""
    try:
        yamlfile = sys.argv[1]
    except IndexError:
        print "Please refer to documentation for proper arguments"
    configdict = methods.get_config(yamlfile)

    #Generate configurations for the core snippets
    for snippet in configdict['coresnippets']:
        print methods.gen_snippet(snippet, configdict[snippet])

if __name__ == "__main__":
    run()