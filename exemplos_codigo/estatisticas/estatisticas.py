# -*- coding: utf-8 -*-
import sys
# Atenção!!!!! O comando abaixo não é muito Pythonico...
# Serve apenas para que este exemplo funcione.
sys.path.append('../')
import latextools
import pandas as pd
import locale
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def draw_plots(df, show=False):

    medias = df.mean(axis=0)

    plt.figure(1)
    plt.hist(df.values[:,0])
    plt.axhline(medias[0], linewidth=4, color='r')
    plt.savefig('prova1.png')
    if show:
        plt.show()

    plt.figure(2)
    plt.hist(df.values[:,1])
    plt.axhline(medias[1], linewidth=4, color='r')
    plt.savefig('prova2.png')
    if show:
        plt.show()

    plt.figure(3)
    plt.hist(df.values[:,2])
    plt.axhline(medias[2], linewidth=4, color='r')
    plt.savefig('prova3.png')
    if show:
        plt.show()

def write_texfile(filename, info):

    disciplina = info[0]
    turma = info[1]
    semestre = info[2]
    numerodealunos = info[3]
    # Escrever o resultado em um arquivo .tex
    with open(filename,'r+') as f:
        old = f.readlines()
        if old[0][1:4] == 'def':
            offset = 4
        else:
            offset = 0
        f.seek(0)
        f.write('\\def\\disciplina {'+disciplina+'}\n\\def\\turma {'+turma+'}\n\\def\\semestre {'+semestre+'}\n\\def\\numerodealunos {'+str(numerodealunos)+'}\n')
        f.writelines(old[offset:])

if __name__ == '__main__':

    locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

    df = pd.read_csv('notas.csv', sep=';', index_col=0)
    df = df.applymap(lambda x: '0' if x in ['-'] else x)
    df = df.applymap(locale.atof)

    numalunos = len(df.index)
    draw_plots(df)

    info = ['Calculo A', '00000', '2016.1', numalunos]
    write_texfile('relatorio.tex', info)
    # Compilar e mostrar o pdf resultante.
    latextools.compile('relatorio', 'True', 2)
    latextools.cleanup('relatorio')
