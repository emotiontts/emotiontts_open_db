# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:22:44 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""
from . import mainstructure
from . import leafnode_processing
import json
import queue

q = queue.Queue()

jsonList = list()


def mainstructurePrint():
    q.put(json.dumps(mainstructure.file_data, ensure_ascii=False, indent=4))


def putStatus(eleStr, code):
    status = {
        "ele": eleStr,
        "code": code
    }
    q.put(json.dumps(status, ensure_ascii=False, indent=4))


def sendQueue():
    leafnode_processing.queueProcessing(q)
