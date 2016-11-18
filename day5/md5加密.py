# -*- coding:utf-8 -*-
__auth__ = 'christian'

import hashlib
hash = hashlib.md5()
hash.update('段炼')
print hash.hexdigest()