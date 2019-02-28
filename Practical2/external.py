'''
Anne Harding, 12/02/2019
GEOG5790 - Practical 2 - Scripts
Python script to test running arcpy from a script.
'''

# Import modules:
import arcpy

# Define variables:
sf = "Z:\GEOG5790\practical2_scripts\Data\input\explosion.shp"
lf = "Z:\GEOG5790\practical2_scripts\Data\generated\explosion.lyr"
lyr = "explosion_lyr"

# Make feature layer from sf and to lyr location:
print "Making feature layer from {0}.".format(sf)
arcpy.management.MakeFeatureLayer(sf, lyr)
print "Saving layer file to {0}.".format(lf)
arcpy.management.SaveToLayerFile(lyr, lf, "ABSOLUTE")
