'''
Anne Harding, 12/02/2019
GEOG5790 - Practical 2 - Scripts
Standalone Python script to run explosion model outside of Arc.
'''

# Import modules:
import arcpy

# Set Arc workspace:
arcpy.env.workspace = "Z:\GEOG5790\practical2_scripts"

# Input parameters:
buffer_feature = "Z:/GEOG5790/practical2_scripts/Data/input/explosion.shp"
buffer_distance = "100 Meters"
output_buffer = "Z:/GEOG5790/practical2_scripts/Data/generated/external_modelrun_buffer.shp"
intersect_features = "Z:/GEOG5790/practical2_scripts/Data/input/buildings.shp"
output_intersect = "Z:/GEOG5790/practical2_scripts/Data/generated/external_modelrun_intersect.shp"

# Check if output locations exist and delete files at those locations:
if arcpy.Exists(output_buffer):
	arcpy.Delete_management(output_buffer)
	print("{0} already exists. Deleting file.".format(output_buffer))
	
if arcpy.Exists(output_intersect):
	arcpy.Delete_management(output_intersect)
	print("{0} already exists. Deleting file.".format(output_intersect))

# Run Explosion model:
try:
    try:
        arcpy.ImportToolbox("Z:\GEOG5790\practical1_modelbuilder\Data\Practical1.tbx", "Practical1")
    except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
    try:
        arcpy.ExplosionModel_Practical1(buffer_distance, buffer_feature, intersect_features, output_intersect)
    except arcpy.ExecuteError as e:
        print("Model run error", e)
except Exception as e:
    print(e)
