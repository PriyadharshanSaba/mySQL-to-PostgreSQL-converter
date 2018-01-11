from __future__ import unicode_literals
import mysql.connector

global cursor

#def mySQLconnection():


def getTabs():
    tables="show tables"
    #checkDATA={'uid':usn}s
    cursor.execute(tables)
    fet = cursor.fetchall()
    j = 0
    for i in fet:
        if j==2:
            getCons(i[0])
        j+=1

def getCons(name):
    creTA = "show create table "+str(name)
    cursor.execute(creTA)
    fet=cursor.fetchone()
    for i in fet:
        print(i)
        print(" ")



def test(x):
    print(x)



#mySQLconnection()
cn = mysql.connector.connect(user='root', password='Rocky@2009', database='studentportal')
cursor=cn.cursor()
getTabs()


