#!/bin/bash -eu

FILE_PATH=$(greadlink -f ${BASH_SOURCE[0]})
# FILE_PATH=$(pwd)/src/scripts/virtualenv_activate.bash
FILE_DIR=$(dirname $FILE_PATH)
SCRIPTS_DIR=$FILE_DIR
SRC_DIR=$(dirname $SCRIPTS_DIR)
ROOT_DIR=$(dirname $SRC_DIR)
VENV_DIR=$ROOT_DIR/venv

. $VENV_DIR/bin/activate
