#-*— coding:utf-8 -*-
#Auther: wangjiana

import logging as log
def GetLogger():
    logger = log.getLogger()
    fh = log.FileHandler("log.txt")
    logger.addHandler(fh)
    return logger