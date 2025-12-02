#!/bin/bash

YEAR=$(date +'%Y')

mkdir $YEAR

for i in {1..12}
do
    SUB="/day$i"
    mkdir $YEAR$SUB
done