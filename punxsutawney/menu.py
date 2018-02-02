from enum import Enum

class MenuItemType(Enum):
    """
    The type of content that a MenuItem leads to.
    """
    TEXT = '0',
    MENU = '1',
    CCSO_NAMESERVER = '2',
    ERROR = '3',
    BINHEX = '4',
    DOS = '5',
    UUENCODE = '6',
    SEARCH = '7',
    TELNET = '8',
    BINARY = '9',
    MIRROR = '+',
    GIF = 'g',
    IMAGE = 'I',
    TELNET_3270 = 'T',
    HTML = 'h',
    MESSAGE = 'i',
    SOUND = 's'

class MenuItem:
    """
    Represents an item in a Gopher menu.
    """
    def __init__(self, entry_type, display, selector="null", host="null",
        port=70):
        """
        Constructor method. Creates a new MenuItem.
        """
        self.entry_type = entry_type
        self.display = display
        self.selector = selector
        self.host = host
        self.port = port
    
    def __str__(self):
        """
        Returns the item as it is written in a standard Gopher
        server response.
        """
        return "{}{}\t{}\t{}\t{}\n".format(
                    self.entry_type.value[0],
                    self.display,
                    self.selector,
                    self.host,
                    self.port)

class Menu:
    """
    Represents a Gopher menu.
    """
    def __init__(self):
        """
        Constructor method. Creates a new list to contain MenuItems.
        """
        self.items = []
    
    def append(self, item):
        """
        Appends a MenuItem to the menu.
        """
        self.items.append(item)
    
    def __str__(self):
        """
        Returns the list as written in a standard Gopher server
        response.
        """
        response_str = ""
        
        for item in self.items:
            response_str += item.__str__()

        response_str += "."
        return response_str
