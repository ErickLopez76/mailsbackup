__author__ = 'earch'
import mailsbackuptools


#from mailsBackupTools import *
mailServer, mailUser, mailPassword = mailsbackuptools.getmaildata()
#print(mailsbackuptools.sumar(2,2))

maillist = mailsbackuptools.getmaillist(mailServer,mailUser, mailPassword,'INBOX','')

print(maillist)

#Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
print(mailServer)

