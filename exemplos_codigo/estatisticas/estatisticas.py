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

    # plt.figure(4)
    # p1 = df.boxplot(0)
    # p2 = df.boxplot(1)
    # p3 = df.boxplot(2)
    # plt.savefig('boxplot.png')
    # if show:
    #     plt.show()
    
    # Agora, queremos observar a progressão dos alunos em dois gráficos:
    # Os que foram aprovados e os que foram reprovados
    mediasfinais = df.mean(axis=1)
    # aprovados = indices dos alunos que tiveram média maior que 5.75
    # reprovados = indices dos alunos que tiveram média menor que 5.75
    aprovados = mediasfinais[mediasfinais>=5.75]
    reprovados = mediasfinais[mediasfinais<5.75]

    plt.figure(5)
    for i in range(0,len(aprovados)):
        plt.plot(df.values[aprovados.index[i]-1,:])
    plt.savefig('notasaprovados.png')
    if show:
        plt.show()

    plt.figure(6)
    for i in range(0,len(reprovados)):
        plt.plot(df.values[reprovados.index[i]-1,:])
    plt.savefig('notasreprovados.png')
    if show:
        plt.show()

    return mediasfinais, aprovados, reprovados

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
    
    # Gerar figuras
    numalunos = len(df.index)
    mediasfinais, aprovados, reprovados = draw_plots(df)

    # Escrever informações sobre a turma
    info = ['Calculo A', '00000', '2016.1', numalunos]
    write_texfile('relatorio.tex', info)

    # Compilar e mostrar o pdf resultante.
    latextools.compile('relatorio', 'True', 2)
    latextools.cleanup('relatorio')
