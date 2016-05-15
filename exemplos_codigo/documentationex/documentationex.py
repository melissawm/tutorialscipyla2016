# -*- coding: utf-8 -*-
import sys
# Atenção!!!!! O comando abaixo não é muito Pythonico...
# Serve apenas para que este exemplo funcione.
sys.path.append('../')
import latextools

def createTeXfile(str="", filename='arquivo.tex',title='Título',author='Melissa', date=''):
    with open(filename,'w') as results:
        print >>results, '\\documentclass{article}'
        print >>results, '\\usepackage[utf8]{inputenc}'
        print >>results, '\\usepackage{palatino}'
        print >>results, '\\title{', title, '}'
        print >>results, '\\author{', author, '}'
        print >>results, '\\date{', date, '}'
        print >>results, '\\begin{document}'
        print >>results, '\\maketitle'
        print >>results, str
        print >>results, '\\end{document}'
    
if __name__ == '__main__':

    if sys.platform.startswith('linux'):
        # Linux-specific code here...
        str = "{\\centering \\textsc{You are using Linux!}}\\\\ Cool! We're good to go...\\\\ \\paragraph*{Installation} Just run this command as superuser (\\emph{root}):\\\\ \\centering \\verb+# pip install scipy+"
    elif sys.platform.startswith('darwin'):
        # Mac OS code
        str = "Ok, just use a linux virtual machine..."
    elif sys.platform.startswith('win'):
        # Windows?
        str = "Really. No chance I'm supporting this for windows. You're on your own. Sorry"
    else:
        str = "You must really know what you're doing, so don't let me stop you."
    
    # Escrever o resultado em um arquivo .tex
    titulo = 'OS check'
    autora = 'Melissa'
    filename = 'documentationex'
    # Criar arquivo basico
    createTeXfile(str, filename+'.tex',titulo, autora)
    # Compilar e mostrar o pdf resultante.
    latextools.compile(filename, 'True')
    latextools.cleanup(filename)
