#!/bin/bash

for d in monorepo-*; do 
  echo "$d"
  cp ./run.py "${d}/Assignment5_Memory/Allocator/part1/"
  cp ./compile.py "${d}/Assignment5_Memory/Allocator/part1/"
  cp ./t-test1.c "${d}/Assignment5_Memory/Allocator/part1/tests"
  cd "${d}/Assignment5_Memory/Allocator/part1/"
  python compile.py
  python run.py > "/home/prdx/Documents/CS5600-Summer/repos/${d}.res" 2>&1 
  cd "/home/prdx/Documents/CS5600-Summer/repos"
done
