__author__ = 'earch'
import mailsbackuptools
import datetime

maillist = []
m = []
# from mailsBackupTools import *
mailServer, mailUser, mailPassword = mailsbackuptools.getmaildata()
#print(mailsbackuptools.sumar(2,2))

byte_data = None

maillist = mailsbackuptools.getmaillist(mailServer, mailUser, mailPassword, 'INBOX', '')
for idmail in maillist:
    #print(int(idmail))
    if not mailsbackuptools.search_mailid_db(int(idmail)): #No lo encuentra
        #print('No Encontrado') #Save in hard disk drive and add to db_local
        #get_save_mail_eml
        vto, vfrom, vcc, vsubject, vstrdate, vsize = mailsbackuptools.getmail_save_eml(idmail)
        mailsbackuptools.put_newmail_dblocal(int(idmail),vsize, vto,vfrom , vcc , vsubject ,datetime.datetime.now(),vstrdate)
    #else:
     #   print('Encontrado') #continue with next id

print(maillist)


#Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
print(mailServer)
