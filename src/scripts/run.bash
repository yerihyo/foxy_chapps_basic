#!/bin/bash -eu

ARG0=${BASH_SOURCE[0]}
FILE_PATH=$($(dirname $ARG0)/filepath2readlink.bash $ARG0)
# FILE_PATH=/Users/moon/projects/trickboxes/basic/scripts/setup.bash
FILE_DIR=$(dirname $FILE_PATH)
FILE_NAME=$(basename $FILE_PATH)

SCRIPTS_DIR=$FILE_DIR
SRC_DIR=$(dirname $SCRIPTS_DIR)
BASIC_DIR=$(dirname $SRC_DIR)

#python $BASIC_DIR/app.py runserver
echo "[$FILE_NAME] START"

echo "[$FILE_NAME] pushd $SRC_DIR"
pushd $SRC_DIR


export FLASK_APP=main/app.py
export FLASK_DEBUG=1
flask run --port=5001

popd

echo "[$FILE_NAME] END"
