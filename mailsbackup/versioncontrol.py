#Get control version from github and update all software
import requests
import configparser
from ftplib import FTP
from os import listdir
from os.path import isfile, join
import os

# rewrite this funcion using ftp
def get_version_server():
    #r = requests.get('https://raw.github.com/ErickLopez76/mailsbackup/release/mailsbackup/version.txt')
    #server_version=float(r.text)
    #return server_version
    config = configparser.ConfigParser()
    config.read('config.ini')
    server = config.get('Version_control','server')
    user = config.get('Version_control', 'readuser')
    passwd = config.get('Version_control', 'readpass')
    
    #connect to server for every file
    ftp = FTP(server,user,passwd)
    ftp.retrbinary('RETR version.txt', open('temp.txt','wb').write)
    ftp.quit()
    
    vdata = float(open('temp.txt','r').read())
    return vdata


def get_ftpread_conn_param():
    config = configparser.ConfigParser()
    config.read('config.ini')
    server = config.get('Version_control','server')
    user = config.get('Version_control', 'readuser')
    passwd = config.get('Version_control', 'readpass')
    return server,user,passwd

## This function get the list files of server
def get_new_version():
    server, user, passwd = get_ftpread_conn_param()
    ftp = FTP(server,user,passwd)
    #get list of file in server
    lfiles = ftp.nlst()

    for lf in lfines:
        get_file()

    
def get_file(filename):
    server, user, passwd = get_ftpread_conn_param()
    ftp = FTP(server,user,passwd)
    
    ftp.retrbinary('RETR ' + filename, open(filename,'wb').write)
    #get list of fils in server
    #connect to server to get every file

def get_ext(filename):
    extension = os.path.splitext(filename)
    return extension[1]

def excludefiles(listfiles,excludeString):
    excludeList = excludeString.split(";")
    #for f in listfiles:
    #    if get_ext(f) in excludeList poero si :
        

def send_file(filename):
    config = configparser.ConfigParser()
    config.read('config.ini')
    server = config.get('Version_control','server')
    user = config.get('Version_control', 'user')
    passwd = config.get('Version_control','pass')
    #connect to server for every file
    ftp = FTP(server,user,passwd)

    #save every file to server
    file = open(filename,'rb')
    print(filename)
    ftp.storbinary('STOR ' +  filename, file)
    file.close()
    ftp.quit()


def put_new_Version():
    config = configparser.ConfigParser()
    config.read('config.ini')
    exclude = config.get('Version_control','excludeext')
    
    excludeList = exclude.split(";")

    # get list files in local
    onlyfiles = [f for f in listdir('./') if isfile(join('./',f))]
    
    # exclude files

    for fi in onlyfiles:
        if get_ext(fi) in excludeList:
            #exclude file
            print('archivo excluido')
        else:
            send_file(fi)


