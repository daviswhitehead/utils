import os
from ConfigParser import SafeConfigParser


def find_pass_cfg(file_path=None):
    """ Will verify a file path given, or return default path to cfg file
    """
    if not file_path:
        file_path = '~/.pass.cfg'

    if os.path.isfile(os.path.expanduser(file_path)):
        return file_path
    else:
        return None


def read_cfg(file_path, section):
    """ Reads a cfg file and
        returns a dictionary of options for a given section.
    """
    d = {}
    parser = SafeConfigParser()

    try:
        parser.read(os.path.expanduser(file_path))
        for option in parser.options(section):
            d[option] = parser.get(section, option)
        return d
    except:
        print "Config read failed"
        return None


if __name__ == '__main__':
    find_pass_cfg()
    read_cfg()
