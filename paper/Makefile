
target=sbc-template

all:
	latex  $(target).tex
	bibtex $(target).aux
	latex  $(target).tex
	latex  $(target).tex
	dvipdf $(target).dvi
	make clean

clean:
	rm -f *.aux *.bbl *.blg *.dvi *.log
