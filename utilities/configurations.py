import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def removeAttr(d, key):
    r = dict(d)
    del r[key]
    return r
