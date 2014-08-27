__author__ = 'ErickLopez76'
import imaplib
import email
import datetime
from mailsbackuptools import *

imap_host = 'mail.inclusionsocial.gob.sv'
imap_user = 'elopez@inclusionsocial.gob.sv'
imap_pass = 'Evrk1133'

imap = imaplib.IMAP4(imap_host)

imap.login(imap_user, imap_pass)

folderStatus, UnseenInfo = imap.status('INBOX',"(UNSEEN)")

imap.list()

imap.select("inbox") #Connected to inbox

print(folderStatus)

result, data = imap.uid('search', None, "ALL")

ids = data[0] #data is a list.
print('print ids')
print(ids)
id_list = ids.split() #ids is a space separate string
lastest_email_id = data[0].split()[-1] # get the lastest

#result, data = imap.fetch(lastest_email_id,"(RFC822)")  #fetch the mail


print(lastest_email_id)

result, data = imap.uid('fetch', lastest_email_id, '(RFC822)')
print("-------------")
print(type(lastest_email_id))
#result, data = imap.uid('fetch', lastest_email_id, '(X-GM-THRID X-GM-MSGID)')

status, AllMessage = imap.fetch('1','(RFC822)')

raw_email = data[0][1]

#raw_email = data

#fetch mail

print(raw_email)
print (str(lastest_email_id))

email_message = email.message_from_bytes(raw_email)
print('To: ')
print(email_message['To'])
print('From: ')
print (email.utils.parseaddr(email_message['From']))
print('cc: ')
print(email_message['cc'])
print(email_message['subject'])
print(email_message['date'])
print (email_message.items()) #print all headers



f=open(str(int(lastest_email_id)) + ".eml","w")
#f.write(str(raw_email))
f.write(str(email_message))
print(f.tell())
f.close()