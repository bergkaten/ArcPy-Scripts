"""This script changes element text on all the layouts that are in an ArcGIS Pro .aprx file.
There are two versions. The first replaces a whole element text with a new, updated element text.
The second searchs elements that have a specific word/phrase (in this case, "PROJECT:") and if the element has that, it changes specific text within that. """

#Option 1: Search for exact text of an element and replace whole element text with new text.
import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT") #If working outside of Pro, put the file path of your aprx here.
for lyt in aprx.listLayouts():
    for elm in lyt.listElements('TEXT_ELEMENT'):
        if elm.text == "PROJECT: 169000XXXX | DATED: <dyn type=\"date\" format=\"short\"/> | DESIGNER: <dyn type=\"user\"/>": #Should be the actual text of the element you'd like to change (rather than the element name).
            elm.text = "PROJECT: 1690015749-005 | DATED: <dyn type=\"date\" format=\"short\"/> | DESIGNER: <dyn type=\"user\"/>" #Should be what you'd like to change to

#Option 2: Search for an element with a specific word and replace a single thing within it.
import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT") #If working outside of Pro, put the file path of your aprx here.
for lyt in aprx.listLayouts():
    for elm in lyt.listElements('TEXT_ELEMENT'):
        if "PROJECT:" in elm.text: #Change what's in the parentheses to a word that's in the element box you're interested in. Or just comment this out and ignore.
            elm.text = elm.text.replace("169000XXXX", "1690015749-005") #Before the comma is what it is currently and after the comma is what you'd like to change it to.