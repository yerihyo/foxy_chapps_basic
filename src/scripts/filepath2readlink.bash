#!/bin/bash -eu

ARG0=${BASH_SOURCE[0]}

if [ $# -lt 1 ]; then
    die "usage: $ARG0 <filepath>"
fi

machine_name=$($(dirname ${BASH_SOURCE[0]})/machine_name.bash)

if [ $machine_name == "Linux" ]; then
    FILE_PATH=$(readlink -f $ARG0)
elif [ $machine_name == "Mac" ]; then
    FILE_PATH=$(greadlink -f $ARG0)
else
    die "Unhandled machine - $machine_name"
fi
echo $FILE_PATH
