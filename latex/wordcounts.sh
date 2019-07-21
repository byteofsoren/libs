#!/bin/bash
#############################################################################
# __        __            _  ____                  _     ____  ____  _____
# \ \      / /__  _ __ __| |/ ___|___  _   _ _ __ | |_  |  _ \|  _ \|  ___|
#  \ \ /\ / / _ \| '__/ _` | |   / _ \| | | | '_ \| __| | |_) | | | | |_
#   \ V  V / (_) | | | (_| | |__| (_) | |_| | | | | |_  |  __/| |_| |  _|
#    \_/\_/ \___/|_|  \__,_|\____\___/ \__,_|_| |_|\__| |_|   |____/|_|
#
#############################################################################
# This short script converts all .ms files in the current directory
# to PDF files and also shows the word count of the files.
# Good to have for those in the university who need to stay with in
# the provided word count
#############################################################################
# Written by Magnus Sörensen
#############################################################################


for filename in *.pdf
do
    words=$(pdftotext "$newname"  - | wc -w )
    lines=$(pdftotext "$newname"  - | wc -l )
    # Status report
    echo "Input filename $filename is containing $words words and $lines lines of text."
done
