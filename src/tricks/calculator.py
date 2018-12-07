import ast
import math
import operator

from flask import Flask, url_for

from src.utils.utils import l_singleton2obj

# app = Flask(__name__)


# def index():


operators = {ast.Add: operator.add,
             ast.Sub: operator.sub,
             ast.Mult: operator.mul,
             ast.Div: operator.truediv,
             ast.Pow: operator.pow,
             ast.BitXor: operator.xor,
             ast.USub: operator.neg,
             }

h_func_unary = {"sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "floor": math.floor,
                "ceil": math.ceil,
                "round": round,
                }
h_name = {"PI": math.pi}


def calculate(s, ):
    h_env = {}
    return _eval_calculate(ast.parse(s, mode='eval').body, h_env)


def _eval_calculate(node, h_env):
    t = type(node)

    if isinstance(node, ast.Num):  # <number>
        return node.n

    if isinstance(node, ast.BinOp):  # <left> <operator> <right>
        v_LEFT = _eval_calculate(node.left, h_env)
        v_RIGHT = _eval_calculate(node.right, h_env)
        f_op = operators[type(node.op)]
        return f_op(v_LEFT, v_RIGHT)

    if isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        v_OPERAND = _eval_calculate(node.operand, h_env)
        f_op = operators[type(node.op)]
        return f_op(v_OPERAND)

    if isinstance(node, ast.Name):
        if node.id not in h_name: raise Exception()
        return h_name[node.id]

    if isinstance(node, ast.Call):
        func_name = node.func.id.lower()
        if func_name in h_func_unary:
            if len(node.args) > 1: raise Exception()
            if node.keywords: raise Exception()

            f_op = h_func_unary[func_name]
            arg = _eval_calculate(l_singleton2obj(node.args), h_env)
            return f_op(arg)

    raise TypeError(node)
