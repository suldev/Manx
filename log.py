verbose = False

def info(message):
    if verbose:
        print (f":: {message}")

def warn(message):
    print (f"WW {message}")

def error(message):
    print (f"EE {message}")

def fatal(message):
    print (f"FF {message}")
    quit()

def debugstop(message):
    print (f"DS {message}")
    quit()

def debug(message):
    print (f"DD {message}")