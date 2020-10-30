# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong 

Process prosody element.
"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getprosody(prosodyEle):
    """
    Process prosody element's attributes and text value.

    Args:
      prosodyEle: Parse the prosody element.

    """

    # Save the pre attribute's value
    oldPitchAttr = mainstructure.file_data["prosody"]["pitch"]
    oldContourAttr = mainstructure.file_data["prosody"]["contour"]
    oldRangeAttr = mainstructure.file_data["prosody"]["range"]
    oldRateAttr = mainstructure.file_data["prosody"]["rate"]
    oldDurationAttr = mainstructure.file_data["prosody"]["duration"]
    oldVolumeAttr = mainstructure.file_data["prosody"]["volume"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(prosodyEle)
    if checkAttr:
        children_ele_processing.evalChildren(prosodyEle)

    initAttr = list()  # attribute list to initialize

    if oldPitchAttr != "":
        mainstructure.file_data["prosody"]["pitch"] = oldPitchAttr
    else:
        initAttr.append("pitch")

    if oldContourAttr != "":
        mainstructure.file_data["prosody"]["contour"] = oldContourAttr
    else:
        initAttr.append("contour")

    if oldRangeAttr != "":
        mainstructure.file_data["prosody"]["range"] = oldRangeAttr
    else:
        initAttr.append("range")

    if oldRateAttr != "":
        mainstructure.file_data["prosody"]["rate"] = oldRateAttr
    else:
        initAttr.append("rate")

    if oldVolumeAttr != "":
        mainstructure.file_data["prosody"]["volume"] = oldVolumeAttr
    else:
        initAttr.append("volume")

    if oldDurationAttr != "":
        mainstructure.file_data["prosody"]["duration"] = oldDurationAttr
    else:
        initAttr.append("duration")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init prosody element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(prosodyEle, initAttr)
