"""These script will list the data sources for all layers in all the maps in an ArcGIS Pro .aprx file."""

aprx = arcpy.mp.ArcGISProject("CURRENT") #If working outside of Pro, put the file path of your aprx here.
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
        if lyr.supports("dataSource"):
            print ("    " + lyr.dataSource)
print("All done! :D")