"""This script changes element text on all the layouts that are in an ArcGIS Pro .aprx file.
Specficially, this replaces a whole element text with a new, updated element text.
Put another way, search for exact text of an element and replace whole element text with new text."""

import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT") #If working outside of Pro, put the file path of your aprx here.
for lyt in aprx.listLayouts():
    for elm in lyt.listElements('TEXT_ELEMENT'):
        if elm.text == "PROJECT: 169000XXXX | DATED: <dyn type=\"date\" format=\"short\"/> | DESIGNER: <dyn type=\"user\"/>": #Should be the actual text of the element you'd like to change (rather than the element name).
            elm.text = "PROJECT: 1690015749-005 | DATED: <dyn type=\"date\" format=\"short\"/> | DESIGNER: <dyn type=\"user\"/>" #Should be what you'd like to change to