#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Pass the pw db to cmd line: $ ./task3.sh pw_db.csv"
    exit
fi

python3 task3.py "$1"