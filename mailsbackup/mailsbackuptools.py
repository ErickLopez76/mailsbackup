__author__ = 'ErickLopez76'
import email
import imaplib
import configparser

def getmaildata():
    """
Search information in ini file

    :return:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    mailserver = config.get('MAIL','mailServer')
    mailuser = config.get('MAIL','mailUser')
    mailpassword = config.get('MAIL','mailPassword')
    #config.sections()
    return mailserver, mailuser, mailpassword

def getmaillist(imap_server,user,passw, folder, filter):
    imap_host = imap_server
    imap_user = user
    imap_pass = passw

    imap = imaplib.IMAP4(imap_host)

    imap.login(imap_user, imap_pass)

    folderStatus, UnseenInfo = imap.status(folder,"(UNSEEN)")

    imap.list()

    imap.select("inbox") #Connected to inbox

    print(folderStatus)

    result, data = imap.uid('search', None, "ALL")

    return data[0] #data is a list.


def sumar(a,b):
    """
    This module is for help
    :param a: First integer
    :param b:
    :return:
    """
    return a + b
