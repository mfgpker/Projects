#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

sql = raw_input("Insert SQl qury: ")

with con:

    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except mdb.Error, e:
        if con:
            con.rollback()
        print "Error %d: %s" % (e.args[0],e.args[1])
        
        sys.exit(1)
        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row