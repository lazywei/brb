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
