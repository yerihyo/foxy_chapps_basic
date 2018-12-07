from datetime import datetime
from functools import reduce

import pytz
from flask import make_response

import settings
from utils.utils import dt2timezone, env2v_or_none,lmap
import os
from collections import defaultdict
from datetime import datetime
from urllib.request import urlretrieve
from urllib.parse import urljoin
from zipfile import ZipFile


def get(pystr):
    # raise Exception( type(j_env) )

    return make_response("hello world")


