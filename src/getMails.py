__author__ = 'ErickLopez76'
import imaplib

imap_host = 'mail.inclusionsocial.gob.sv'
imap_user = 'elopez@inclusionsocial.gob.sv'
imap_pass = 'Evrk1133'

imap = imaplib.IMAP4(imap_host)

imap.login(imap_user, imap_pass)

folderStatus, UnseenInfo = imap.status('INBOX',"(UNSEEN)")

imap.list()

imap.select("inbox") #Connected to inbox

print(folderStatus)

result, data = imap.search(None, "ALL")

ids = data[0] #data is a list.
print(ids)
id_list = ids.split() #ids is a space separate string
lastest_email_id = id_list[-1] # get the lastest

result, data = imap.fetch(lastest_email_id,"(RFC822)")  #fetch the mail

