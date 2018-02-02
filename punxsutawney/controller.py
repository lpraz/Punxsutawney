class Controller:
    """
    Controls functionality of the Gopher server under a certain set of
    selectors.
    """
    
    def run(self, requested_selector):
        """
        Runs the appropriate action for the given selector.
        """
        for selector in actions:
            if selector == requested_selector:
                actions[requested_selector]()
