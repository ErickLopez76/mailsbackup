__author__ = 'earch'
import fdb
import mailsbackuptools

n = 5
print(n)
lfiledb, ldbuser, ldbpassword = mailsbackuptools.getdbcnxdata()

cnx = fdb.connect(dsn=lfiledb, user=ldbuser, password=ldbpassword)

assert isinstance(cnx, fdb.Connection)
#cur = cnx.cursor()
cur2 = cnx.cursor()
#cur = cur.execute("select * from mails")
cur2.callproc("search_mail_by_Id", [n])
output = cur2.fetchone()
print(output)
cnx.commit()
print(output)
#assert isinstance(cur, fdb.Cursor)
#a = cur.fetchall()
#print(type(a))
#print(a)
#print(len(a))
#print('pop')
#b = a.pop()
#print(type(b))
#print(b[0])
#print(b[1])
# print(b[2])
# print(b[3])
# print(output)
#print(a.pop())
#print(a.pop()[2])
#print(a.pop()[3])
#print(a.pop()[4])