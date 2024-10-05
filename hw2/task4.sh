#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Pass the pw db to cmd line: $ ./task4.sh pw_db.csv"
    exit
fi

python3 task4.py "$1"