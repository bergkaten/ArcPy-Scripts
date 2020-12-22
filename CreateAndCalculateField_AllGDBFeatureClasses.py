"""This script adds a field to all the polygon feature classes in a geodatabase and then calculates the area of the polygon using the newly created field."""

import arcpy, os, sys
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\kberg\Documents\Ramboll\Projects\1940074088_702_002\Data\Vector\LZ03BC.gdb" #Update with geodatabase path

"""The fcs variable below returns a list of the feature classes in the current workspace, limited by name, feature type, and optional feature dataset.
ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset})
wild_card: Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.
                e.g. *Represents zero or more characters., Te* finds Tennessee and Texas.
feature_type: Limit the results. Some valid feature types: all, point, multipatch, line, label, annotation...
For more: https://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-functions/listfeatureclasses.htm"""
fcs = arcpy.ListFeatureClasses("*","Polygon")



for fc in fcs:
    inField = "Area_Acres" #This is the name of the field you are creating
    arcpy.AddField_management(fc, inField, "DOUBLE", "#", "#", "#", inField, "NULLABLE", "NON_REQUIRED") #Change "DOUBLE" if you'd like a different field type (e.g. text, date)
    print("Updating " + fc)
   
    fileName = os.path.basename(fc)
    arcpy.CalculateField_management(fc, inField, '!shape.area@acres!', "PYTHON3") #This calculates the acres of the polygon in the newly created inField
    
    print(fc + " completed")