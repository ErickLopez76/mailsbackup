__author__ = 'earch'
import sys
from mailsbackup import mailsBackupTools

#from mailsBackupTools import *

def main(avrg):
    mailServer, mailUser = mailsBackupTools.getMailServer()


    #config = configparser.ConfigParser()
    #config.read('config.ini')
    #mailServer = config.get('MAIL','mailServer')
    #config.sections()
    print(mailServer)
    print(mailUser)
    pass

if __name__ == '__main__':
    main(sys.argv)
