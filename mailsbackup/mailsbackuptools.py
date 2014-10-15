__author__ = 'ErickLopez76'
import email
import imaplib
import configparser
import mysql
import mysql.connector
import fdb  # firebird library
import socket
# import ipaddress
import os
import datetime
import versioncontrol
# import confdata


def getlastcheck():
    config = configparser.ConfigParser()
    config.read('config.ini')
    lastdaycheck = config.get('Version_control', 'lastCheck')
    localv = config.get('Version_control', 'version')
    return lastdaycheck, localv


def check_update():
    lastcheck, localversion = getlastcheck()
    i = datetime.datetime.now()
    si = i.strftime('%Y/%m/%d')
    returndata = 0
    print(si)
    if lastcheck != si:
        print("se necesita revisar el servidor de actualizaciones")
        serverversion = versioncontrol.get_version_server()
        if serverversion == 0:
            # Can't connect with server
            returndata = 0
        if serverversion != localversion and serverversion !=0: #si la version es local es diferente del server
            print('tiene una version antigua')
            returndata = 1
            #execute search new version on server
            versioncontrol.get_new_version()
    return returndata
def server_db_is_enable():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('DB_server','enable')

def dbservercnxdata():
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config.get('DB_server', 'host')
    dbuser = config.get('DB_server', 'dbsUser')
    dbpassword = config.get('DB_server', 'dbsPassword')
    return host, dbuser, dbpassword

# cnx = mysql.connector.connect(user='backmail_admin', password='bkAdmin*5',
#                              host='10.20.30.126',
#                              database='mail_backup_server')
# #assert isinstance(cnx, mysql.Connection)
# cur = cnx.cursor()
# #assert isinstance(cur, mysql.connector.cursor)
# #cur.execute('select * from mailback_resume')
# sql_parameter = 'Valeria',1,'10.20.30.18','Kevin'
# cur.callproc("add_resume", sql_parameter)
# #for row in cur.fetchall():
# #    print(row[1])
# cnx.commit()
# cnx.close()

def get_information_to_resume():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mailUser = config.get('MAIL', 'mailUser')
    config.clear()
    pc_name = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    pc_ip = s.getsockname()[0]
    return mailUser, pc_name, pc_ip


def dbserver_conexion():
    lhost, ldbsuser, ldbspassword = dbservercnxdata()
    return mysql.connector.connect(host=lhost, user=ldbsuser, password=ldbspassword,database='mail_backup_server' )

def putresumein_server(newmails):
    cnx = dbserver_conexion()

    #assert isinstance(cnx, mysql.connector)
    cur = cnx.cursor()
    puser, pc_name, pc_ip = get_information_to_resume()

    sql_parameter = puser, newmails, pc_ip, pc_name

    cur.callproc("add_resume", sql_parameter)
    cnx.commit()
    cnx.close()


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

def put_newmail_dblocal(mail_id, size, pfrom, pto, pcc, subject, pdate, pstrdate):
    cnx = dblocal_conexion()
    if pcc == None:
        pcc = ''
    if pfrom == None:
        pfrom = ''
    if pto == None:
        pto = ''
    print(mail_id)
    sql_parameter = mail_id, size, pfrom[:699], pto[:699], pcc[:699], subject, pdate, pstrdate
    assert isinstance(cnx, fdb.Connection)
    cur = cnx.cursor()
    cur.callproc("ADD_MAIL", (sql_parameter))
    cnx.commit()



def getmaildata():
    """
Search information in ini file

    :rtype : object
    :return:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    # mailserver = config.get('MAIL', 'mailServer')
    # mailuser = config.get('MAIL', 'mailUser')
    # mailpassword = config.get('MAIL', 'mailPassword')
    # config.sections()

    mailserver = confdata.mailsbackup_crypt.get_server()
    mailuser = confdata.mailsbackup_crypt.get_user()
    mailpassword = confdata.mailsbackup_crypt.get_passwd()

    return mailserver, mailuser, mailpassword


def getmail_save_eml(mailid):
    lmailid = bytes(mailid)
    limap = getimap()
    limap.select()
    result, data = limap.uid('fetch',lmailid, 'RFC822')
    raw_mail = data[0][1]
    email_message = email.message_from_bytes(raw_mail)

    if not os.path.exists("mails"):
        os.makedirs("mails")

    f=open("./mails/" + str(int(mailid)) + ".eml", "w")
    f.write(str(email_message))
    size = f.tell()
    f.close()
    return  email_message['From'],email_message['To'], email_message['cc'], email_message['subject'], email_message['date'], size


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


