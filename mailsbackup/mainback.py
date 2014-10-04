__author__ = 'Erick'
import mailsbackuptools
import datetime

maillist = []
m = []

# check last update
mailsbackuptools.check_update()

# from mailsBackupTools import *
mailServer, mailUser, mailPassword = mailsbackuptools.getmaildata()
#print(mailsbackuptools.sumar(2,2))

byte_data = None
n = 0
#Get mail list and check in local database
maillist = mailsbackuptools.getmaillist(mailServer, mailUser, mailPassword, 'INBOX', '')
for idmail in maillist:
    if not mailsbackuptools.search_mailid_db(int(idmail)): #Not found mail
        #Save mail in eml file
        vfrom, vto, vcc, vsubject, vstrdate, vsize = mailsbackuptools.getmail_save_eml(idmail)

        #Save in db_local register
        mailsbackuptools.put_newmail_dblocal(int(idmail),vsize, vfrom, vto , vcc , vsubject ,datetime.datetime.now(),vstrdate)
        n = n + 1

        #Save resume in Server
if mailsbackuptools.server_db_is_enable == 1:
    print('Start send resume to sever')
    if n > 0:
        try:
            mailsbackuptools.putresumein_server(n)
        except:
            print("No Database Server")
            pass
#print(maillist)
    print("Process finished")
#Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
#print(mailServer)
<<<<<<< HEAD
#Esta es la ultima lineai
#otra lina final 1
=======
#Esta es la ultima linea
>>>>>>> terminal_master
