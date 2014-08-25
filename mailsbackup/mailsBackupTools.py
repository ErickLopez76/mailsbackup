__author__ = 'ErickLopez76'
import email
import configparser


def getMailServer():
    """
Search information in ini file

    :return:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    mailserver = config.get('MAIL','mailServer')
    mailuser = config.get('MAIL','mailUser')
    #config.sections()
    return mailserver, mailuser

def sumar(a,b):
    """
    This module is for help
    :param a: First integer
    :param b:
    :return:
    """
    return a + b
