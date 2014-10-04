#Get control version from github and update all software
import request

def get_version_file():
    r = request.get('https://raw.github.com/ErickLopez76/requests/release/mailsbackup/version.txt')
    sversion=r.text
