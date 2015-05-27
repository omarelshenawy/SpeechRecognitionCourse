#!/bin/bash
shopt -s globstar
shopt -s nullglob
for file in **/*.{wav}
do
  echo "$file"
done
