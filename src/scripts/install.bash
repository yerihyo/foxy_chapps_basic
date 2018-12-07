#!/bin/bash -eu

FILE_PATH=$(greadlink -f ${BASH_SOURCE[0]})
# FILE_PATH=/Users/moon/projects/trickboxes/basic/scripts/setup.bash
FILE_DIR=$(dirname $FILE_PATH)
SCRIPTS_DIR=$FILE_DIR
BASIC_DIR=$(dirname $SCRIPTS_DIR)


machine_name=`$FILE_DIR/machine_name.bash`

if [ $machine_name == "Linux" ]; then
    sudo apt-get install postgresql postgresql-contrib
elif [ $machine_name == "Mac" ]; then
    brew install postgresql
else
    die "Unhandled machine - $machine_name"
fi


# . $BASIC_DIR/venv/bin/activate
pip install flask flask-graphql flask-migrate flask-sqlalchemy graphene graphene-sqlalchemy connexion
pip install postgres psycopg2
xf
