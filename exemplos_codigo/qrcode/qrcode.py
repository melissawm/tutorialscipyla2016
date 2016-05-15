# -*- coding: utf-8 -*-
import pyqrcode
import os

if __name__ == '__main__':
    # Criar qrcode
    url = pyqrcode.create('http://github.com/melissawm')
    url.png('qrcode.png', scale=8)
    print(url.terminal(quiet_zone=1))
    # Compilar e mostrar o pdf resultante.
    try:
        os.system('pdflatex qrcode.tex')
    except OSError:
        print('LaTeX not installed.')
    if os.path.isfile('qrcode.pdf'):
        os.system('xdg-open qrcode.pdf &')
    else:
        print('Something went wrong! PDF file was not generated.')
