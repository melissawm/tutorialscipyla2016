# -*- coding: utf-8 -*-
import sys
# Atenção!!!!! O comando abaixo não é muito Pythonico...
# Serve apenas para que este exemplo funcione.
sys.path.append('../')
import latextools
import subprocess

def write_texfile(dirname):
    # Ler o arquivo gerado pelo ls
    with open('ls.output','r') as output:
        # Escrever o resultado em uma tabela em um arquivo .tex
        with open('ls.tex','w') as results:
            print >>results, '%& -output-directory=',dirname
            # Codigo LaTeX
            print >>results, '\\documentclass{article}'
            print >>results, '\\usepackage[utf8]{inputenc}'
            print >>results, '\\usepackage{palatino}'
            print >>results, '\\usepackage{verbatim}'
            print >>results, '\\usepackage{longtable}'
            print >>results, '\\begin{document}'
            print >>results, '\\section*{Conteúdo do diretório ',dirname,'}'
            print >>results, '\\begin{center}'
            print >>results, '\\begin{longtable}{|l|}\\hline'
            print >>results, '\\hline Nome do arquivo \\\\ \\hline \\endfirsthead'
            for line in output:
                print >>results, '\\verb+',line[:-1],'+\\\\ '
            print >>results,'\\hline'
            print >>results,'\\end{longtable}'
            print >>results,'\\end{center}'
            print >>results,'\\end{document}'

if __name__ == '__main__':
    dirname = sys.argv[1]
    # Criar a listagem do diretorio
    with open('ls.output', 'w') as f:
        subprocess.call(['ls',dirname], stdout=f)

    write_texfile(dirname)
    # Compilar e mostrar o pdf resultante.
    latextools.compile('ls', 'True',2)
    # Compilamos 2 vezes pois o pacote longtable às vezes precisa de duas compilações para acertar a largura da tabela final.
    latextools.cleanup('ls')
