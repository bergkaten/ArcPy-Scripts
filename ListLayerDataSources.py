"""The first script lists the data source for each layer in an MXD’s table of contents.
The second script will list the data sources for all layers in all the maps in an ArcGIS Pro .aprx file."""

#Script to be used with ArcMap:
import arcpy
mxd = arcpy.mapping.MapDocument("E:\Projects\OCD\Example\ES007_Figures_20201014.mxd") #Update with path of MXD
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    if layer.supports("dataSource"): #Some layers might not support the property "dataSource"
        print layer.dataSource
        print " "
print "All done! :D"


#Script to be used with ArcGIS Pro:
aprx = arcpy.mp.ArcGISProject("CURRENT") #If working outside of Pro, put the file path of your aprx here.
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
        if lyr.supports("dataSource"):
            print ("    " + lyr.dataSource)
print("All done! :D")