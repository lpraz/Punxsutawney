from enum import Enum

class MenuItemType(Enum):
    text = '0',
    menu = '1',
    ccso_nameserver = '2',
    error = '3',
    binhex = '4',
    dos = '5',
    uuencode = '6',
    search = '7',
    telnet = '8',
    binary = '9',
    mirror = '+',
    gif = 'g',
    image = 'I',
    telnet_3270 = 'T',
    html = 'h',
    message = 'i',
    sound = 's'

class MenuItem:
    """
    Represents an item in a Gopher menu.
    """
    def __str__(self):
        """
        Returns the item as it is written in a standard Gopher
        server response.
        """
        return "%s%s\t%s\t%s\t%s".format(
                    self.entry_type
                    self.display_string
                    self.selector
                    self.hostname
                    self.port)
