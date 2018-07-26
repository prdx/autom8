#!/bin/bash

current_dir = `/home/prdx/Documents/CS5600-Summer/repos`

for d in monorepo-*; do 
  echo "${d}"
  cd "${d}/Assignment4_Shell"
  if [ -e shell ]
  then
    python 2.1.py
  fi
  cd "${current_dir}"
done
