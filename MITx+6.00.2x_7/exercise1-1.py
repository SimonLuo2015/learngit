"""
Created on 03/18/2017
@ author: Simon
"""


def metric1(item):
    return item.getValue() / item.getWeight()

def metric2(item):
    return -item.getWeight()

def metric3(item):
    return item.getValue()