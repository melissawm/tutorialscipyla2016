from subprocess import call, check_output, CalledProcessError
from os import remove

def compile(filename='arquivo', showpdf=False, runs=1):

    try:
        k=0
        while k < runs:
            check_output(['pdflatex', '-interaction=nonstopmode',filename+'.tex'])
            k += 1
        if showpdf:
            call(['xdg-open', filename+'.pdf'])
    except CalledProcessError as err:
        print("There was an error compiling your file with pdflatex. Please check your .log file for more information.")
        lines = int(raw_input("Check tail of pdflatex execution? Enter number of lines (0 to exit): "))
        err = err.output.split("\n")
        if lines > 0:
            print "\n".join(err[-lines:])
    except:
        if showpdf:
            print("Error displaying pdf file. Please check that you have the correct PDF viewer selected in diretorio.py.")
        else:
            pass
    finally:
        print("Done.")

def cleanup(filename='arquivo'):

    try:
        remove(filename+'.log')
        remove(filename+'.aux')
        remove(filename+'.output')
    except OSError:
        pass

if __name__ == "__main__":
    print "Module containing some tools useful for creating/compiling LaTeX files from Python."
