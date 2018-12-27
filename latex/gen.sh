#!/bin/bash

# ---- Latex generator using pdflatex -----
# - Written by Magnus Sörensen -

# Base file is the starting point for the documens with out tex ending i.e main.tex is just main.
# pdfshow is the pdf viewer.
baseFile=main
pdfshow=zathura

ps aux | grep $pdfshow > /dev/null
if [ $? -eq 0 ];
then
    echo "$pdfshow is running. Kill ing it."
    pkill $pdfshow
fi
cp $baseFile.tex $baseFile.bac
# if [ ! -f $baseFile.pdf ];
# then
#     rm $baseFile.pdf
# fi
if [ -f $baseFile.tex ];
then
    pdflatex $baseFile.tex > /dev/null
fi
if [ -f $baseFile.pdf ];
then
    $pdfshow $baseFile.pdf &
fi
rm *.out *.bac *.bac *.aux > /dev/null
