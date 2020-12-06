def logdebug(area, message, keepline):
    # quick stupid function for logging debug messages
    if keepline:
        print('['+area+'] - '+message, end='')
    else:
        print('['+area+'] - '+message)
