# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process meta element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getmeta(metaEle):
    """
    Process meta element's attributes and text value.

    Args:
      metaEle: Parse the meta element.

    """

    # Save the pre attribute's value
    oldNameAttr = mainstructure.file_data["meta"]["name"]
    oldContentAttr = mainstructure.file_data["meta"]["content"]
    oldHttpAttr = mainstructure.file_data["meta"]["http-equiv"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(metaEle)
    if checkAttr:
        children_ele_processing.evalChildren(metaEle)

    initAttr = list()  # attribute list to initialize
    if oldNameAttr != "":
        mainstructure.file_data["meta"]["name"] = oldNameAttr
    else:
        initAttr.append("name")

    if oldContentAttr != "":
        mainstructure.file_data["meta"]["content"] = oldContentAttr
    else:
        initAttr.append("content")

    if oldHttpAttr != "":
        mainstructure.file_data["meta"]["http-equiv"] = oldHttpAttr
    else:
        initAttr.append("http-equiv")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init meta element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(metaEle, initAttr)
