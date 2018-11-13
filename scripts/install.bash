#!/bin/bash -eu

FILE_PATH=$BASH_SOURCE[0]
# FILE_PATH=/Users/moon/projects/trickboxes/basic/scripts/setup.bash

FILE_DIR=$(dirname $FILE_PATH)
SCRIPTS_DIR=$FILE_DIR
BASIC_DIR=$(dirname $SCRIPTS_DIR)


# . $BASIC_DIR/venv/bin/activate
pip install flask flask-graphql flask-migrate flask-sqlalchemy graphene graphene-sqlalchemy
