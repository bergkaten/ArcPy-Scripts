#This script exports ArcMap Data Drive pages, specifically designed for a particular project creating lots of parcel maps for a site

import arcpy
import time

parcelMapMXD = "C:\Users\kberg\Documents\Ramboll\Projects\PRSCP\Floodplain\Parcel_Maps\S6\PRSCP_S6_Parcels_NoPII.mxd" #Path of the MXD with the Data Driven Pages functionality
outputPath = "C:\Users\kberg\Documents\Ramboll\Projects\PRSCP\Floodplain\Parcel_Maps\S6" #Path of where you'd like the exported figures to go.

#========
mxd = arcpy.mapping.MapDocument(parcelMapMXD)
ddp = mxd.dataDrivenPages
dfs = arcpy.mapping.ListDataFrames(mxd)
parentDF = ddp.dataFrame

#========
print (time.strftime("%H:%M:%S")) #Uncomment options below if you want to export a different range of pages:
#for pageNum in [39]: 					            #export the 56th page
#for pageNum in [12, 15, 104, 138, 139, 143]:		#export the 56th 58th and 60th page
#for pageNum in range(18,145):				        #export the 10th to the 19th page
for pageNum in range(1, ddp.pageCount + 1): 		#export all pages
    ddp.currentPageID = pageNum
    row = ddp.pageRow
    extent = row.Shape.extent
    name = row.getValue(ddp.pageNameField.name)
    print "Exporting page {0} of {1}: {2}".format(str(ddp.currentPageID), str(ddp.pageCount),name)
    arcpy.mapping.ExportToPDF(mxd, outputPath + "\\" + name + ".pdf", resolution=100)   #exports the DDP to PDF
    #arcpy.mapping.ExportToPNG(mxd, outputPath + "\\" + name + ".png", resolution=100)  #exports the DDP to PNG

#========
del mxd
print "All done exporting parcel maps."
print (time.strftime("%H:%M:%S"))
print ":D"
