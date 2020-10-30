# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:34:46 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process appraisal element.
"""
from . import attributes_processing, children_ele_processing


def getappraisal(appraisal, vocaItems):
    """
    Process appraisal element's attributes

    Args:
        appraisal: Parse the appraisal element.
        vocaItems : Parse the vocab item list to check appraisal is in the defined vocab list.

    Returns:
        appraisalAttr.get("name") : Return appraisal name to check if name in the emotion element appears only once.
    """

    appraisalAttr = appraisal.attrib
    appraisalChilds = appraisal.getchildren()

    isName = attributes_processing.setEmotionMLAttribute(appraisal, vocaItems)

    if "trace" not in appraisalChilds:
        if appraisalAttr.get("value") is None:
            print("warning : <appraisal> element may contain either a value attribute or a <appraisal> element")

    if isName:
        children_ele_processing.evalChildren(appraisal)
        return appraisal.get("name")
