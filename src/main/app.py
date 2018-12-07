# REFERENCE
# https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525

# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import connexion
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView


import sys

from flask import cli

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(MAIN_DIR)
BASE_DIR = os.path.dirname(SRC_DIR)

# app initialization
cx_app = connexion.App(__name__,) # specification_dir='swagger/')
cx_app.add_api('swagger.yaml') #, arguments={'api_local': 'local_value'})
#cx_app.add_api('../clock/swagger.yaml') #, arguments={'api_local': 'local_value'})


#app = Flask(__name__)
app = cx_app.app
app.debug = True


# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Modules
db = SQLAlchemy(app)

if False:
    from main.schema import Query
    from main.rest import Mutation
    schema = graphene.Schema(query=Query, mutation=Mutation)

    # Routes
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )


# @app.route('/')
# def index():
#     return '<p> Hello World</p>'

if __name__ == '__main__':
    #app.run()
    cx_app.run(port=5001)
    #app.run(port=args.port_number, server='flask')


