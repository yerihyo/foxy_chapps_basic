from functools import reduce


def dt2is_aware(dt):
    if dt.tzinfo is None: return False
    if dt.tzinfo.utcoffset(dt) is None: return False
    return True

def dt2is_naive(dt): return not dt2is_aware(dt)

def dt2timezone(dt, tz):
    if dt2is_naive(dt): return tz.localize(dt)
    return dt.astimezone(tz)


def h_propdown(h, branches, f_down=None,):
    if f_down is None: f_down = lambda x,k: x.get(k) if x else None

    return reduce(f_down, branches, h)