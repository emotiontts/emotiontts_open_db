# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:42:56 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process item element.
"""
from . import ele_emotion_info


def getitem(item):
    """
    Process item element's attributes and child elements.

    Args:
        item : Parse the item element.

    Returns:
        name: Return the name of the item
    """

    itemAttr = item.attrib
    itemChilds = item.getchildren()
    info = True
    name = ""

    for attr in itemAttr.keys():
        if attr in ["name"]:
            if itemAttr.get("name") is not None:
                name = itemAttr.get("name")
            else:
                print("error : must contain name attribute.")
        else:
            print('error : item must contain only name attribute.')

    for child in itemChilds:
        if child.tag == "info":
            if info:
                eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
                info = False
            else:
                print("error : already have <info>")
        else:
            print("error : item must contain only info element.")

    return name
