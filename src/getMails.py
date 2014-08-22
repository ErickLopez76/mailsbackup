__author__ = 'ErickLopez76'
import imaplib

imap_host = 'mail.inclusionsocial.gob.sv'
imap_user = 'elopez@inclusionsocial.gob.sv'
imap_pass = 'Evrk1133'

imap = imaplib.IMAP4(imap_host)

imap.login(imap_user, imap_pass)

folderStatus, UnseenInfo = imap.status('INBOX',"(UNSEEN)")

print(folderStatus)

