# coding=utf-8

from hashlib import sha1

def get_sha(var):
    # 此为SHA单向不可逆加密
    result = sha1()
    SHA_PRE = "zzj"
    var = SHA_PRE + var
    result.update(var.encode('utf-8'))
    return result.hexdigest()