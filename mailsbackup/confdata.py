import getpass
import re

class mailsbackup_crypt:

    def encrypt(raw_string):
        h = ""
        for l in raw_string:
            h = h + hex(ord(l))
        return h

    def set_server():
        s_server = input("Ingrese servidor de correo: ")
        h = mailsbackup_crypt.encrypt(s_server)
        return h

    def set_user():
        s_user = input("Ingrese correo: ")
        h = mailsbackup_crypt.encrypt(s_user)
        return h

    def set_user_pass():
        s_passwd = getpass.getpass("Ingrese clave de correo: ")
        h = mailsbackup_crypt.encrypt(s_passwd)
        return h

    def create_user():
        h_server = mailsbackup_crypt.set_server()
        h_user = mailsbackup_crypt.set_user()
        h_pass = mailsbackup_crypt.set_user_pass()
        file = open('system.bin', 'w+')
        file.write(h_server)
        file.close()

        file = open('system0.bin', 'w+')
        file.write(h_user)
        file.close()

        file = open('system1.bin', 'w+')
        file.write(h_pass)
        file.close()

        print('Datos Almacenado correctamente')

    def decrypt(hex_string):
        split_hex = re.findall('....', hex_string)
        rdata = ""
        for h in split_hex:
            rdata = rdata + chr(int(h,0))
        return rdata

    def get_server():
        file = open('system.bin', 'r')
        server = file.read()
        file.close()
        sserver = mailsbackup_crypt.decrypt(server)
        return sserver

    def get_user():
        file = open('system0.bin', 'r')
        user = file.read()
        file.close()
        suser = mailsbackup_crypt.decrypt(user)
        return suser

    def get_passwd():
        file = open('system1.bin', 'r')
        passwd = file.read()
        file.close()
        spasswd = mailsbackup_crypt.decrypt(passwd)
        return spasswd
