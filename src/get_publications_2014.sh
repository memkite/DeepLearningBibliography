#!/bin/bash

for k in 0 20 40 60 80 100 120 140 160 180 200 220 240 260 280; do
    python search_publications.py --all="gpu" --phrase="deep learning" --after=2014 --start=$k --citation=bt >> deepl.bib
    sleep 10
done





