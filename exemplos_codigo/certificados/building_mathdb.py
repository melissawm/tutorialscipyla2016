import sys
import sqlite3

with open('math.txt','r') as f:
    data = f.readlines()
    data = [x.split(';') for x in data]
    data = [[x[0],x[1].lstrip(' ').rstrip('\n')] for x in data]

print data
con = None

try:
    con = sqlite3.connect('math.db')
    cur = con.cursor()    
    cur.execute('CREATE TABLE Math(Nome TEXT, Datas TEXT)')
    for row in data:
        cur.execute('INSERT INTO math (Nome,Datas) values (?,?)',(row[0],row[1]))
    con.commit()

except sqlite3.Error as e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()

