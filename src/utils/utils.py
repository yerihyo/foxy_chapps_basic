from functools import reduce

def pipe_funcs(l):
    def f(*args,**kwargs):
        v0 = l[0](*args,**kwargs)
        v9 = reduce(lambda v,f:f(v),l[1:], v0)
        return v9
    return f


def dt2is_aware(dt):
    if dt.tzinfo is None: return False
    if dt.tzinfo.utcoffset(dt) is None: return False
    return True

def dt2is_naive(dt): return not dt2is_aware(dt)

def dt2timezone(dt, tz):
    if dt2is_naive(dt): return tz.localize(dt)
    return dt.astimezone(tz)

lmap = pipe_funcs([map,list,])


def l_singleton2obj(l, allow_empty_list=False,):
    if len(l) == 1: return l[0]
    if not l and allow_empty_list: return None
    raise Exception(len(l), l)

def env2v_or_none(j, ll,):
    err = None
    for l in ll:
        try: return reduce(lambda h,k:h[k],l,j)
        except KeyError as e:
            err = e

    return None