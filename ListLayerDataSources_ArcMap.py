"""This script lists the data source for each layer in an MXD’s table of contents."""

import arcpy
mxd = arcpy.mapping.MapDocument("E:\Projects\OCD\Example\ES007_Figures_20201014.mxd") #Update with path of MXD
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    if layer.supports("dataSource"): #Some layers might not support the property "dataSource"
        print layer.dataSource
        print " "
print "All done! :D"