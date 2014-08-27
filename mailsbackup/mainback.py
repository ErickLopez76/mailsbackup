__author__ = 'earch'
import mailsbackuptools

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
        print('No Encontrado') #Save in hard disk drive and add to db_local
        #get_save_mail_eml
        mailsbackuptools.getmail_save_eml(idmail)

    else:
        print('Encontrado') #continue with next id

print(maillist)


#Review all mails, check each mail, if don't exist in dblocal then download and save in dblocal, if exit then next
print(mailServer)
