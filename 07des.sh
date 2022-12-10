#!/bin/bash

input="07des.txt"
while IFS= read -r line
do
  arrayline=($line)
  echo "$arrayline[0]"

  if [[ ${arrayline[0]} == "dir" ]]
  then
    mkdir ${arrayline[1]}
  elif [[ ${arrayline[0]} == "$" ]] && [[ ${arrayline[1]} == "cd" ]]
  then
    if [[ ${arrayline[2]} == "/" ]]
    then
      echo "cd /"
    else
      cd ${arrayline[2]}
    fi
  elif [[ ${arrayline[0]} =~ ^-?[0-9]+$ ]]
  then
    fallocate -l ${arrayline[0]} ${arrayline[1]}
  fi
done < "$input"
