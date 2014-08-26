__author__ = 'earch'
import mailsbackuptools


#from mailsBackupTools import *
mailServer, mailUser, mailPassword = mailsbackuptools.getmaildata()
#print(mailsbackuptools.sumar(2,2))

print(mailsbackuptools.getmaillist(mailServer,mailUser, mailPassword,'INBOX',''))

#Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
print(mailServer)

