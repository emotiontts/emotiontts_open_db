# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process sub element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getsub(subEle):
    """
    Process sub element's attributes and text value.

    Args:
      subEle: Parse the sub element.

    """

    # Save the pre attribute's value
    oldAliasAttr = mainstructure.file_data["sub"]["alias"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(subEle)
    if checkAttr:
        children_ele_processing.evalChildren(subEle)

    initAttr = list()  # attribute list to initialize

    if oldAliasAttr is not None:
        mainstructure.file_data["sub"]["alias"] = oldAliasAttr
    else:
        initAttr.append("oldAliasAttr")
    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init sub element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(subEle, initAttr)
