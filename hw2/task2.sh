#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Pass the pw db to cmd line: $ ./task2.sh pw_db.csv"
    exit
fi

python3 task2.py "$1"