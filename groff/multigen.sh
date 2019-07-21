#!/bin/bash
#####################################################################
#    ____            __  __       _
#  / ___|_ __ ___  / _|/ _|     | | ___ __ ___  ___  __      _____
# | |  _| '__/ _ \| |_| |_ _____| |/ / '_ ` _ \/ __| \ \ /\ / / __|
# | |_| | | | (_) |  _|  _|_____|   <| | | | | \__ \  \ V  V / (__
#  \____|_|  \___/|_| |_|       |_|\_\_| |_| |_|___/   \_/\_/ \___|
#
#####################################################################
# This short script converts all .ms files in the current directory
# to PDF files and also shows the word count of the files.
# Good to have for those in the university who need to stay with in
# the provided word count
#####################################################################
# Written by Magnus Sörensen
#####################################################################


for filename in *.ms
do
    # Remove the .ms from filenames.
    newname=${filename%%.*}
    # Convert the .ms files to .pdf
    groff -kms $filename -T pdf > $newname.pdf
    # Word count
    words=$(pdftotext "$newname.pdf"  - | wc -w )
    # Status report
    echo "Input filename $filename convert to $newname.pdf containing $words words."
done
