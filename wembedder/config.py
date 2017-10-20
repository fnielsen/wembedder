"""wembedder.config.

Usage:
  wembedder.config show

"""

from __future__ import absolute_import, print_function

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import logging

from os.path import exists, expanduser


CONFIGURATION_FILENAMES = [
    'wembedder.cfg',
    '~/etc/wembedder.cfg',
    '~/wembedder.cfg']

DEFAULTS = """
[requests]
user_agent = wembedder
"""


logger = logging.getLogger(__name__)
logging.getLogger(__name__).addHandler(logging.NullHandler())


def get_configuration():
    """Return configuration."""
    configuration = configparser.SafeConfigParser()

    configuration.readfp(StringIO(DEFAULTS))

    for filename in CONFIGURATION_FILENAMES:
        full_filename = expanduser(filename)
        if exists(full_filename):
            logger.info('Reading configuration file from {}'.format(
                full_filename))
            configuration.read(full_filename)
            break
        else:
            logger.warn('No configuration file found')
    return configuration


def main():
    """Handle command-line interface."""
    from docopt import docopt

    arguments = docopt(__doc__)

    if arguments['show']:
        configuration = get_configuration()
        for section in configuration.sections():
            print('[' + section + ']')
            for item in configuration.items(section):
                print(item[0] + ' = ' + item[1])
            print()


if __name__ == "__main__":
    main()
