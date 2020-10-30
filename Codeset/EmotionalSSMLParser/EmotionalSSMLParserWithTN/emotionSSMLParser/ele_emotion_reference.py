# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process reference element.
"""
from . import mainstructure


def getreference(reference):
    """
    Process reference element's attributes.

    Args:
        reference: Parse the reference element.
    Returns:
        uriResult: referenceAttr.get("uri"), Return reference uri.
    """

    referenceAttr = reference.attrib
    referenceChilds = reference.getchildren()
    uriResult = ""

    uriAttr = mainstructure.file_data["emotionInfo"]["reference"]["uri"]
    roleAttr = mainstructure.file_data["emotionInfo"]["reference"]["role"]
    mediaTypeAttr = mainstructure.file_data["emotionInfo"]["reference"]["media-type"]

    if len(referenceChilds) > 0:
        print("error : reference_children is not none")

    if referenceAttr.get("uri") is not None:
        print("referenceAttr_uri : " + referenceAttr.get("uri"))
        uriResult = referenceAttr.get("uri")
        uriAttr = uriResult
        mainstructure.file_data["emotionInfo"]["reference"]["uri"] = uriAttr
    else:
        print("reference's uri is none")

    if referenceAttr.get("media-type") is not None:
        print("referenceAttr_media-type : " + referenceAttr.get("media-type"))
        mediaTypeAttr = referenceAttr.get("media-type")
        mainstructure.file_data["emotionInfo"]["reference"]["media-type"] = mediaTypeAttr

    if referenceAttr.get("role") is not None:
        role_value = referenceAttr.get("role")
        if role_value in ["expressedBy", "experiencedBy", "triggeredBy", "targetedAt", ""]:
            if role_value == "":
                role_value = "expressedBy"
            print("referenceAttr_role_value : " + role_value)
            roleAttr = role_value
            mainstructure.file_data["emotionInfo"]["reference"]["role"] = roleAttr
        else:
            print("error :  referenceAttr_role's value is wrong")

    return uriResult
