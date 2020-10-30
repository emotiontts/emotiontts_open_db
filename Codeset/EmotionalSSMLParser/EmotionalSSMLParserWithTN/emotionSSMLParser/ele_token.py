# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process token element.
(token element and w element are processed the same way.)

"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def gettoken(tokenEle):
    """
    Process token element's attributes and text value.

    Args:
      tokenEle: Parse the token element.

    """
    # Save the pre attribute's value
    oldLangAttr = mainstructure.file_data["lang"]
    oldIdAttr = mainstructure.file_data["token"]["id"]
    oldLangfailureAttr = mainstructure.file_data["onlangfailure"]
    oldRoleAttr = mainstructure.file_data["token"]["role"]
    oldEmoData = mainstructure.getEmoInfo()

    checkAttr = attributes_processing.setAttribute(tokenEle)

    # Process the attributes
    if checkAttr:
        children_ele_processing.evalChildren(tokenEle)

    initAttr = list()  # attribute list to initialize
    if oldLangAttr != "":
        mainstructure.file_data["lang"] = oldLangAttr
    else:
        initAttr.append("lang")

    if oldLangfailureAttr != "":
        mainstructure.file_data["onlangfailure"] = oldLangfailureAttr
    else:
        initAttr.append("onlangfailure")

    if oldIdAttr != "":
        mainstructure.file_data["token"]["id"] = oldIdAttr
    else:
        initAttr.append("id")

    if oldRoleAttr != "":
        mainstructure.file_data["token"]["role"] = oldRoleAttr
    else:
        initAttr.append("role")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init token element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(tokenEle, initAttr)
