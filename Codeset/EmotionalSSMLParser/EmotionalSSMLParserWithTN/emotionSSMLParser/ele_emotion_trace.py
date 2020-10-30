# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process trace element.
"""
from . import mainstructure


def gettrace(trace):
    """
    Process trace element's attributes

    Args:
        trace: Parse the trace element.
    """

    traceAttr = trace.attrib
    traceChilds = trace.getchildren()

    freqAttr = mainstructure.file_data["emotionInfo"]["trace"]["freq"]
    samplesAttr = mainstructure.file_data["emotionInfo"]["trace"]["samples"]

    if traceAttr.get("freq") is not None:
        print("tracefreq : " + traceAttr.get("freq"))
        freqAttr = traceAttr.get("freq")
        mainstructure.file_data["emotionInfo"]["trace"]["freq"] = freqAttr

    if traceAttr.get("samples") is not None:
        print("tracesamples : " + traceAttr.get("samples"))
        samplesAttr = traceAttr.get("samples")
        mainstructure.file_data["emotionInfo"]["trace"]["samples"] = samplesAttr

    if len(traceChilds) != 0:
        print("error : <trace> element must not have children element. ")
