
def dt2is_aware(dt):
    if dt.tzinfo is None: return False
    if dt.tzinfo.utcoffset(dt) is None: return False
    return True

def dt2is_naive(dt): return not dt2is_aware(dt)

def dt2timezone(dt, tz):
    if dt2is_naive(dt): return tz.localize(dt)
    return dt.astimezone(tz)