#!/bin/bash
for filename in ../data/input/langs/dataset2/txt/*; do
    find $filename -exec cat {} >> $filename.txt \;
done

mv ../data/input/langs/dataset2/txt/*.txt ../data/input/langs/dataset2/