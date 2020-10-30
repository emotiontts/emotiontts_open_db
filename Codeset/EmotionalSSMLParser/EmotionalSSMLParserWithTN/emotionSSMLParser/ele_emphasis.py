# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process emphasis element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getemphasis(emphasisEle):
    """
    Process emphasis element's attributes and text value.

    Args:
      emphasisEle: Parse the emphasis element.

    """
    # Save the pre attribute's value
    oldLevelAttr = mainstructure.file_data["emphasis"]["level"]

    attributes_processing.setAttribute(emphasisEle)

    children_ele_processing.evalChildren(emphasisEle)

    initAttr = list()  # attribute list to initialize
    if oldLevelAttr != "":
        mainstructure.file_data["emphasis"]["level"] = oldLevelAttr
    else:
        initAttr.append("level")

    # Init emphasis element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(emphasisEle, initAttr)
