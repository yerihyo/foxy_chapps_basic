import ast
import json

from flask import make_response

def put(s, indent,):
    j = ast.literal_eval(s)
    s_JSON = json.dumps(j, indent=indent, ensure_ascii=False,)
    return make_response(s_JSON)

