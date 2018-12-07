from datetime import datetime

import pytz
from flask import make_response

import settings
from utils.utils import dt2timezone
import os
from collections import defaultdict
from datetime import datetime
from urllib.request import urlretrieve
from urllib.parse import urljoin
from zipfile import ZipFile


def lookup(uuid_COMMAND, str_LOCs=None,):
    pass
