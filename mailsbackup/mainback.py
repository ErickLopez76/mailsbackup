__author__ = 'Erick'
import mailsbackuptools
import datetime

maillist = []
m = []

# check last update
if mailsbackuptools.check_update() > 0:
    exit()

# from mailsBackupTools import *
mailServer, mailUser, mailPassword = mailsbackuptools.getmaildata()
# print(mailsbackuptools.sumar(2,2))

byte_data = None
n = 0
# Get mail list and check in local database
try:
    maillist = mailsbackuptools.getmaillist(mailServer, mailUser, mailPassword, 'INBOX', '')
except:
    print("No se puede ingresar al correo")
    exit()

for idmail in maillist:
    # Search in local database
    if not mailsbackuptools.search_mailid_account_db(int(idmail), mailUser):
        # Save mail in eml file
        vfrom, vto, vcc, vsubject, vstrdate, vsize = mailsbackuptools.getmail_save_eml(idmail)

        # Save in db_local register
        try:
            mailsbackuptools.put_newmail_dblocal(int(idmail),vsize, vfrom, vto , vcc , vsubject ,datetime.datetime.now(),vstrdate, mailUser)
            n = n + 1
        except:
            print("No se puede conectar a dblocal")

        # Save resume in Server
if mailsbackuptools.server_db_is_enable == 1:
    print('Start send resume to sever')

    if mailsbackuptools.send_always_report() == 1:
        try:
            mailsbackuptools.putresumein_server(n)
        except:
            print("No Database Server")

    if n > 0 and mailsbackuptools.send_always_report != 1:
        try:
            mailsbackuptools.putresumein_server(n)
        except:
            print("No Database Server")
            pass
# print(maillist)
    print("Process finished")
# Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
# print(mailServer)
# Esta es la ultima linea
