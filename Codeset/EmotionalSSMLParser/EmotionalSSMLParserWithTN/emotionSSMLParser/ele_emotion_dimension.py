# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process dimension element.
"""
from . import attributes_processing, children_ele_processing


def getdimension(dimension, vocaItems):
    """
    Process dimension element's attributes

    Args:
        dimension: Parse the dimension element.
        vocaItems : Parse the vocab item list to check dimension is in the defined vocab list.

    Returns:
        dimensionAttr.get("name") : Return dimension name to check if name in the emotion element appears only once.
    """
    dimensionChilds = dimension.getchildren()
    dimensionAttr = dimension.attrib

    isName = attributes_processing.setEmotionMLAttribute(dimension, vocaItems)

    if "trace" not in dimensionChilds:
        if dimensionAttr.get("value") is None:
            print("error : <dimension> element must contain either a value attribute or a <trace> element")

    if isName:
        children_ele_processing.evalChildren(dimension)
        return dimensionAttr.get("name")
