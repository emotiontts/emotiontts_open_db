# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process action tendency element.
"""
from . import ele_emotion_trace, mainstructure , attributes_processing , children_ele_processing


def getaction_tendency(tendency, vocaItems):
    """
    Process action tendency element's attributes

    Args:
        tendency: Parse the action tendency element.
        vocaItems : Parse the vocab item list to check action tendency is in the defined vocab list.
    Returns:
        tendencyAttr.get("name") : Return tendencyAttr name to check if name in the emotion element appears only once.
    """
    tendencyAttr = tendency.attrib
    tendencyChilds = tendency.getchildren()

    isName = attributes_processing.setEmotionMLAttribute(tendency,vocaItems)

    if "trace" not in tendencyChilds:
        if tendencyAttr.get("value") is None:
            print("warning : <action-tendency> element may contain either a value attribute or a <action-tendency> element")

    if isName:
        children_ele_processing.evalChildren(tendency)
        return tendency.get("name")

