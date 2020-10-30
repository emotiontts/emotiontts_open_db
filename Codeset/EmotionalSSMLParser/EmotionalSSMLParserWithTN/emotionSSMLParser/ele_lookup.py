# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:41:12 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process lookup element.
"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getlookup(lookupEle):
    """
    Process lookup element's attributes and text value.

    Args:
        lookupEle: Parse the lookup element.

    """
    # Save the pre attribute's value
    oldRefAttr = mainstructure.file_data["lookup"]["ref"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(lookupEle)
    if (checkAttr):
        children_ele_processing.evalChildren(lookupEle)

    initAttr = list()  # attribute list to initialize
    if oldRefAttr != "":
        mainstructure.file_data["lookup"]["ref"] = oldRefAttr
    else:
        initAttr.append("ref")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init lookup element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(lookupEle, initAttr)
