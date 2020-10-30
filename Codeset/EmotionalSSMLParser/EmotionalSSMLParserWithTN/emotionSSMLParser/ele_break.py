# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process break element.
"""
from . import mainstructure, attributes_processing, children_ele_processing , mainstructure_dump


def getbreak(breakEle):
    """
    Process break element.

    Args:
      breakEle: Parse the break element.

    """

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(breakEle)
    if checkAttr:
        mainstructure.file_data["text"] = ""
        mainstructure_dump.mainstructurePrint()

    # Init break element's attributes (mainstructure)
    initAttr = ['time', 'strength']
    attributes_processing.initAttribute(breakEle, initAttr)
