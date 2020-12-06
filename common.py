def logdebug(area, message, keepline):
    if keepline:
        print('['+area+'] - '+message, end='')
    else:
        print('['+area+'] - '+message)
