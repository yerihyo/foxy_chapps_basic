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

def str_LOC2timezone(str_LOC):
    try: return pytz.timezone(str_LOC)
    except pytz.exceptions.UnknownTimeZoneError: pass

    h_city2tz_name = str_LOC_expansion(create_str_CITY2tz_name())
    h_set = h_city2tz_name[str_LOC.lower()]
    if len(h_set)>1: raise Exception()
    if not h_set: raise Exception()

    tz_name = next(iter(h_set))
    return pytz.timezone(tz_name)


def str_LOC2lookup(str_LOC):
    now_UTC = datetime.now(pytz.utc)

    tz = str_LOC2timezone(str_LOC)
    now_TZ = dt2timezone(now_UTC, tz)

    str_RESULT = "[{0}] {1}".format(str_LOC, now_TZ.strftime("%Y.%m.%d %I:%M:%S %p"))
    return str_RESULT



# def get(uuid_COMMAND, str_LOC_list=None,):
#     if str_LOC_list is None: str_LOC_list = ["America/Los_Angeles"]
#     # else: str_LOC_list = str_LOCs.split(",")
#
#     l = lmap(str_LOC2lookup, str_LOC_list)
#     return make_response("\n".join(l))

def post(j_env):
    # raise Exception( type(j_env) )

    f_down = lambda h,k: (h.get(k) if h else None)
    tzname_CR = env2v_or_none(j_env, [["chatroom", "timezone"]],)
    uuid_CMD = env2v_or_none(j_env, [["command","uuid"]],)
    loc_list = env2v_or_none(j_env, [["command","locations"]],)

    if not loc_list:
        loc_list = [tzname_CR] if tzname_CR else ["America/Los_Angeles"]

    l = lmap(str_LOC2lookup, loc_list)
    return make_response("\n".join(l))


def create_str_CITY2tz_name():
    basename = 'cities15000' # all cities with a population > 15000 or capitals
    filename = basename+".zip"
    filepath = os.path.join(settings.TMP_DIR,filename)

    # get file
    if not os.path.exists(filepath):
        geonames_url = 'http://download.geonames.org/export/dump/'+filename
        urlretrieve(urljoin(geonames_url, filename), filepath)

    # parse it
    h = defaultdict(set)
    with ZipFile(filepath) as zf, zf.open(basename + '.txt') as file:
        for line in file:
            fields = line.split(b'\t')
            if fields: # geoname table http://download.geonames.org/export/dump/
                name, asciiname, alternatenames = fields[1:4]
                timezone = fields[-2].decode('utf-8').strip()
                if timezone:
                    for city in [name, asciiname] + alternatenames.split(b','):
                        city = city.decode('utf-8').strip()
                        if not city: continue

                        h[city].add(timezone)
    return h

def str_LOC_expansion(h_IN):
    h_OUT = dict(h_IN)

    for str_NAME, set_TZ in h_IN.items():
        str_LOWER = str_NAME.lower()
        if str_LOWER not in h_OUT: h_OUT[str_LOWER] = set_TZ

        city_CONCAT = "".join(str_LOWER.split())
        if city_CONCAT not in h_OUT: h_OUT[city_CONCAT] = set_TZ

    return h_OUT

