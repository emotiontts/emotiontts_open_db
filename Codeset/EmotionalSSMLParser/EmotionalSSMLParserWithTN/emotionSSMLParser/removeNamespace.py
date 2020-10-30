# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:49:20 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""
import xml.etree.ElementTree as elementtree


def removeNamespace(element):
    it = elementtree.iterparse(element)
    for _, el in list(it):
        if '}' in list(el.tag):
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

        for at in list(el.attrib.keys()):  # strip namespaces of attributes too
            if '}' in list(at):
                newat = at.split('}', 1)[1]
                el.attrib[newat] = el.attrib[at]
                del el.attrib[at]

    return it
