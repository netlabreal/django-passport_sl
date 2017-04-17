# coding: utf8

import pymssql

conn = pymssql.connect(host='192.168.2.77',
                       user='vasa',
                       password='Rfqkfc 123',
                       database='Stack_test')
cur = conn.cursor()
cur.execute('SELECT top 5 * FROM stack.[Лицевые счета]')
for row in cur:
    print row

conn.close()