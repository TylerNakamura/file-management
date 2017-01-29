#!/bin/bash

echo -n "Enter File Name [ENTER]: "
read file

hp-scan --mode=color --output=$file.pdf

#convert $file.png -rotate 90 $file.png
