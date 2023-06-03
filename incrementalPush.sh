#!/usr/bin/bash

git status **/* * | grep .pdf | while read p; do
echo adding $p
git add "$p" 
echo commiting $p
git commit -m "$p"
echo pushing $p
git push -u origin master
done
