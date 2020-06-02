"""Configuration functions."""

from configparser import ConfigParser
from pathlib import Path


def get_value(key):
    """Return value from config file for given key."""
    # check local config.ini
    parser = ConfigParser(delimiters='|')  # Make a config parser
    path = Path('config.ini')  # Make a path object
    parser.read(path)

    if parser.has_option('DEFAULT', key):
        return parser.get('DEFAULT', key)
