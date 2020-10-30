# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:12:10 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getg2p(g2pEle):
    checkAttr = attributes_processing.setAttribute(g2pEle)

    if (checkAttr):
        children_ele_processing.evalChildren(g2pEle)
