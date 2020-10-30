# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process info element.
"""


def infochildren(infoChilds):
    """
    Process info Children

    Args:
        infoChilds: Parse the info Children elements.
    """
    for child in infoChilds:
        print("info_child_element : " + child.tag)
        childAttrs = child.attrib
        for childAttr in childAttrs:
            print("info_child_attr:" + childAttr)
            print("info_child_attr_value:" + childAttrs.get(childAttr))
        if child.text is not None:
            print("info_child_element_value: " + child.text)
        if child.tail is not None:
            print("info_child_element_Value_tail : " + child.tail)
        if child.getchildren() is not None:
            infochildren(child.getchildren())


def getinfo(info):
    """
    Process info element's attributes

    Args:
        info: Parse the info element.
    """
    infoAttr = info.attrib
    infoChilds = info.getchildren()

    if infoAttr.get("id") is not None:
        print("info_id: " + infoAttr.get("id"))

    infochildren(infoChilds)
