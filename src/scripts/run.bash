#!/bin/bash -eu

FILE_PATH=$($(dirname ${BASH_SOURCE[0]})/filepath2readlink.bash ${BASH_SOURCE[0]})
# FILE_PATH=/Users/moon/projects/trickboxes/basic/scripts/setup.bash
FILE_DIR=$(dirname $FILE_PATH)
SCRIPTS_DIR=$FILE_DIR
SRC_DIR=$(dirname $SCRIPTS_DIR)
BASIC_DIR=$(dirname $SRC_DIR)

#python $BASIC_DIR/app.py runserver

export FLASK_APP=main.app.py
export FLASK_DEBUG=1
flask run --port=5001

