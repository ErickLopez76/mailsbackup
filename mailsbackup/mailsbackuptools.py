__author__ = 'ErickLopez76'
import email
import imaplib
import configparser
import fdb  # firebird library


def search_mailid_db(idmail):
    return_data = False
    cnx = dblocal_conexion()
    assert isinstance(cnx, fdb.Connection)
    cur = cnx.cursor()
    cur.callproc("search_mail_by_id", [idmail])
    # Buscar id en la db
    if cur.fetchone()[0] == 'T':
        return_data = True
    return return_data


def dblocal_conexion():
    lfiledb, ldbuser, ldbpassword = getdbcnxdata()
    return fdb.connect(dsn=lfiledb, user=ldbuser, password=ldbpassword)


def getdbcnxdata():
    config = configparser.ConfigParser()
    config.read('config.ini')
    filedb = config.get('DB_local', 'filedb')
    dbuser = config.get('DB_local', 'dbUser')
    dbpassword = config.get('DB_local', 'dbPassword')
    return filedb, dbuser, dbpassword


def getmaildata():
    """
Search information in ini file

    :rtype : object
    :return:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    mailserver = config.get('MAIL', 'mailServer')
    mailuser = config.get('MAIL', 'mailUser')
    mailpassword = config.get('MAIL', 'mailPassword')
    # config.sections()
    return mailserver, mailuser, mailpassword


def getmail_save_eml(mailid):
    lmailid = bytes(mailid)
    print(lmailid)
    print(type(lmailid))
    limap = getimap()
    limap.select()
    result, data = limap.uid('fetch',lmailid, 'RFC822')
    raw_mail = data[0][1]
    email_message = email.message_from_bytes(raw_mail)
    f=open(str(int(mailid)) + ".eml", "w")
    f.write(str(email_message))
    f.close()
    return


def getimap(imap_server=None, user=None, passw=None, folder = None, filter = None):
    if imap_server== None:
        imap_server, user, passw = getmaildata()
    imap_host = imap_server
    imap_user = user
    imap_pass = passw

    imap = imaplib.IMAP4(imap_host)

    imap.login(imap_user, imap_pass)
    return imap


def getmaillist(imap_server, user, passw, folder, filter):
    limap = getimap(imap_server, user, passw, folder, filter)
    folderStatus, UnseenInfo = limap.status(folder, "(UNSEEN)")
    limap.list()
    limap.select("inbox")  # Connected to inbox
    result, data = limap.uid('search', None, "ALL")
    return data[0].split() # data is a list.


def convert_listmail_to_array(list):
    stonum = ''
    result_list = []
    for s in list:
        if s.isnumeric():
            stonum += s
        if s.isspace() and len(stonum) > 0:
            result_list.append(int(stonum))
            stonum = ''
    return result_list


def sumar(a, b):
    """
    This module is for help
    :param a: First integer
    :param b:
    :return:
    """
    return a + b
