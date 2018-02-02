import punxsutawney

def main():
    """
    Main method for the program. The server is created, built and
    started here.
    """
    gs = punxsutawney.GopherServer()
    gs.run()

if __name__ == '__main__':
    main()
