import os
from ConfigParser import SafeConfigParser


def find_pass_cfg(file_path=None):
    """Returns existing path to cfg file.

    Verifies existence of file_path argument or returns default file_path
    for pass.cfg file.

    Args:
        file_path (Optional(str)): Path to pass.cfg file.

    Returns:
        string: Verified path to pass.cfg file.

    """
    if not file_path:
        file_path = '~/.pass.cfg'

    if os.path.isfile(os.path.expanduser(file_path)):
        return file_path
    else:
        return None


def read_cfg(file_path, account):
    """
    Reads pass.cfg file and returns dictionary of accounts.

    Args:
        file_path (str): Path to pass.cfg file.
        account (str): Account information to extract.

    Returns:
        dict: Account information object.

    """
    d = {}
    parser = SafeConfigParser()

    try:
        parser.read(os.path.expanduser(file_path))
        for option in parser.options(account):
            # [1:-1] strips apostrophes wrapping the string
            d[option] = parser.get(account, option)[1:-1]
        return d
    except:
        print "Config read failed"
        return None


if __name__ == '__main__':
    find_pass_cfg()
    read_cfg()
