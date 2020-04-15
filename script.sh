#!/bin/sh

cd crawler
python3 singapore.py
python3 sea.py
cd ../
git add .
git commit -m "data update"
git push
