from __future__ import unicode_literals
import mysql.connector

def mySQLconnection():
    cn = mysql.connector.connect(user='root', password='Rocky@2009', database='studentportal')
    cursor=cn.cursor()
    print 



def test(x):
    print(x)

text="hey \n"
test(text)


