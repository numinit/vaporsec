SRC=4realz.tex
TRG=$(SRC:.tex=.pdf)
TEX=xelatex
export TEXINPUTS=../contrib/kmbeamer:./tex:

.SUFFIXES: .tex .pdf

.PHONY: clean cleanup all preview

all: $(TRG) cleanup
ifdef prev
	@open $(prev)
endif

preview: $(TRG) cleanup
ifdef prev
	@open $(prev)
else
	@echo "Defaulting to last made file: `cat .current`"
	@open `cat .current`
endif

.tex.pdf:
	$(TEX) $< $@
	@echo "Made" $@ "from" $<
	@echo "`dirname $<`/`basename $@`" > .current

redo: clean all

clean: cleanup
	rm -f $(TRG)

