# -*- coding: utf-8 -*-
import sqlite3
from subprocess import call
import sys
# Atenção!!!!! O comando abaixo não é muito Pythonico...
# Serve apenas para que este exemplo funcione.
sys.path.append('../')
import latextools

con = None
filename = 'certificado'

# Abrir banco de dados para ler nomes.
try:
    con = sqlite3.connect('math.db')
    cur = con.cursor()    
    cur.execute('select * from math')
    data = cur.fetchall()

except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()

# Gerar um certificado para cada nome.
for row in data:
    f = open(filename+'.tex','r+')
    old = f.readlines()
    if old[0][1:4] == 'def':
        offset = 1
    else:
        offset = 0
    f.seek(0)
    f.write('\\def\\name {'+row[0]+'}\n')
    f.writelines(old[offset:])
    f.close()

    # Compilar arquivo LaTeX
    latextools.compile(filename)
    # Movendo cada certificado para que o nome do arquivo
    # contenha o nome da beneficiada.
    call(['mv',filename+'.pdf', filename+'_'+row[0].replace(' ','_')+'.pdf'])

# Fim!
