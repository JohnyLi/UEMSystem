
import logging

import logging.handlers

import os

from tool.Time_Tool import *
from conf.Global_Config import logs_dir

def update_log():
    global logger,rotatingFileHandler,console

    logging.getLogger("").removeHandler(console)
    logging.getLogger("").removeHandler(rotatingFileHandler)

    if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        pass
    else:
        os.mkdir(logs_dir)

    log_filename=logs_dir+"/"+ from_year_to_day()+".log"

    rotatingFileHandler = logging.handlers.RotatingFileHandler(filename =log_filename,

                                                               maxBytes = 1024 * 1024 * 50,

                                                               backupCount = 5)

    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

    rotatingFileHandler.setFormatter(formatter)

    logging.getLogger("").addHandler(rotatingFileHandler)

    console = logging.StreamHandler()

    console.setLevel(logging.NOTSET)

    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

    console.setFormatter(formatter)

    logging.getLogger("").addHandler(console)

    logger = logging.getLogger("")
    logger.setLevel(logging.NOTSET)
    logger.info("更换日志名称成功")
    return logger


global logger,rotatingFileHandler,console
LEVELS = {'NOSET': logging.NOTSET,
          'DEBUG': logging.DEBUG,
          'INFO': logging.INFO,
          'WARNING': logging.WARNING,
          'ERROR': logging.ERROR,
          'CRITICAL': logging.CRITICAL}

if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

log_filename = logs_dir + "/" + from_year_to_day() + ".log"

rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=log_filename,

                                                           maxBytes=1024 * 1024 * 50,

                                                           backupCount=5)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

rotatingFileHandler.setFormatter(formatter)

logging.getLogger("").addHandler(rotatingFileHandler)

console = logging.StreamHandler()

console.setLevel(logging.NOTSET)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

console.setFormatter(formatter)

logging.getLogger("").addHandler(console)

logger = logging.getLogger("")
logger.setLevel(logging.NOTSET)
