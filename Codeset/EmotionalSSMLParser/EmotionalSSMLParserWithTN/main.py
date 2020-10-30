# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:38:18 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong
"""

from emotionSSMLParser import *

try:
    global doc
    inputFileName = input("inputFileName: ")
    doc = removeNamespace.removeNamespace("inputDoc/" + inputFileName)
    ele_speak.getspeak(doc.root)
except Exception as e:
    print("exception : ", e)
