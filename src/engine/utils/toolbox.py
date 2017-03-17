__author__ = 'manishankargoswami'
# -*- coding: utf-8 -*-

from src.engine.promiselog import logger

# DO NOT RENAME THIS METHOD
# LINKED TO MODEL CONFIGURATION
def machinable(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


# DO NOT RENAME THIS METHOD
# LINKED TO MODEL CONFIGURATION
def convertToFloat(marker):
    return marker / 1000000000


def write_to_console(message):
    print(message)


def invalid_request_message():
    return {"error": "request is invalid"}


def invalid_model_message(e):
    logger.error(e)
    return {"error": "encountered some technical issue while processing the request. "}



def unzip(source_filename, dest_dir):
    import zipfile
    import os.path

    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)
