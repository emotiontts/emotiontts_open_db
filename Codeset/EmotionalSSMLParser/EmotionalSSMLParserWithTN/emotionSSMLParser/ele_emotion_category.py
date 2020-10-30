# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process category element.
"""
from . import attributes_processing, children_ele_processing


def getcategory(category, vocaItems):
    """
    Process category element's attributes

    Args:
        category: Parse the category element.
        vocaItems : Parse the vocab item list to check category is in the defined vocab list.

    Returns:
        categoryAttr.get("name") : Return appraisal name to check if name in the emotion element appears only once.
    """
    categoryChilds = category.getchildren()
    categoryAttr = category.attrib
    isName = attributes_processing.setEmotionMLAttribute(category, vocaItems)

    if "trace" not in categoryChilds:
        if categoryAttr.get("value") is None:
            print("warning : <category> element may contain either a value attribute or a <trace> element")

    if isName:
        children_ele_processing.evalChildren(category)
        return categoryAttr.get("name")
