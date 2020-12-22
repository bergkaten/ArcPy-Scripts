"""This script exports all the layouts that are in an ArcGIS Pro .aprx file to PDF.

If you'd like to export them to a different format, change the PDF portion of ".pdf" and lyt.exportToPDF to one of these: PNG, JPEG, AIX, TIF, etc.
For a full list of export options, go to: https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/layout-class.htm"""

import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")  #If working outside of Pro, put the file path of your aprx here.
for lyt in aprx.listLayouts():
    outName = r"C:\Users\kberg\Desktop" + "\\" + lyt.name + ".pdf"  #Change file location 
    lyt.exportToPDF(outName)