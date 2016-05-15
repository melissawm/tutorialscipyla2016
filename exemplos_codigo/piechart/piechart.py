# -*- coding: utf-8 -*-
import os
import sys
# Atenção!!!!! O comando abaixo não é muito Pythonico...
# Serve apenas para que este exemplo funcione.
sys.path.append('../')
import latextools

def createPiechart(dados):
    pie = '\\newcommand{\\slice}[5]{\\pgfmathparse{0.5*#1+0.5*#2}\\let\\midangle\\pgfmathresult \\draw[thick,fill=blue!#5!white] (0,0) -- (#1:1) arc (#1:#2:1) -- cycle; \\node[label=\\midangle:#4] at (\\midangle:1) {}; \\pgfmathparse{min((#2-#1-10)/110*(-0.3),0)} \\let\\temp\\pgfmathresult \\pgfmathparse{max(\\temp,-0.5) + 0.8} \\let\\innerpos\\pgfmathresult \\node[rectangle] at (\\midangle:\\innerpos) {#3};} \n \\begin{figure}[ht] \n \\begin{center} \n \\begin{tikzpicture}[scale=3] \n \\newcounter{a} \\newcounter{b} \n \\foreach \\p/\\t in {'
    frase = []
    total = 0
    for k,v in dados.iteritems():
        total = total+v
        frase.append(str(v)+'/'+k)
    if total < 100:
        frase.append(str(100-total)+'/Outros')
    print frase
    pie += ','.join(frase)
    pie += '} {\\setcounter{a}{\\value{b}} \\addtocounter{b}{\\p} \\slice{\\thea/100*360} {\\theb/100*360} {\\p\\%}{\\t}{\\theb} } \n \\end{tikzpicture} \n \\end{center} \n \\caption{Dados recolhidos durante a palestra.} \n \\end{figure}'
    return pie

def createTeXfile(pie, filename='piechart.tex',title='Título',author='Melissa', date=''):
    with open(filename,'w') as results:
        print >>results, '\\documentclass{article}'
        print >>results, '\\usepackage{calc}'
        print >>results, '\\usepackage{tikz}'
        print >>results, '\\usepackage[utf8]{inputenc}'
        print >>results, '\\usepackage[T1]{fontenc}'
        print >>results, '\\usepackage{palatino}'
        print >>results, '\\title{', title, '}'
        print >>results, '\\author{', author, '}'
        print >>results, '\\date{', date, '}'
        print >>results, '\\begin{document}'
        print >>results, '\\maketitle'
        print >>results, pie
        print >>results, '\\end{document}'
    
if __name__ == '__main__':
    dados = {'Debian':15, 'Fedora':6, 'Slackware':16, 'Gentoo':5, 'OpenSUSE': 7, 'Chakra':5}
    # Escrever o resultado em um arquivo .tex
    titulo = 'Distribuições Linux entre participantes do SciPy-LA 2016'
    autora = 'Melissa'
    # Criar piechart
    pie = createPiechart(dados)
    # Criar arquivo basico
    createTeXfile(pie, 'piechart.tex',titulo, autora)
    # Compilar e mostrar o pdf resultante.
    latextools.compile('piechart','True')
    latextools.cleanup('piechart')
