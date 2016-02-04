# -*- coding: utf-8 -*-

"""
Cache
"""

import sys

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

# ---------
# Specifics
# ---------

if is_py2:
    pass

elif is_py3:
    from functools import lru_cache
    cacher = lru_cache


# Usage:
#
# def foo(bar, baz):
#    print(bar)
#    print(baz)
#    return ', '.join([bar, baz])
#
# brb.cache(foo, baz="lo")

cached_funcs = {}

def _encoder(d):
    return "&".join(["{}={}".format(k, v) for k, v in d.items()])

def cache(user_func, maxsize=128, typed=False, **keywords):
    key = _encoder(keywords)

    if key not in cached_funcs:

        def func(*args, **kwargs):
            newkeywords = keywords.copy()
            newkeywords.update(kwargs)
            return user_func(*args, **newkeywords)

        cached_funcs[key] = cacher(maxsize=maxsize, typed=typed)(func)

    return cached_funcs[key]
