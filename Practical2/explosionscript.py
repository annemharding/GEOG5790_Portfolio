'''
Anne Harding, 12/02/2019
GEOG5790 - Practical 2 - Scripts
Python script to run explosion model.
'''

# Import modules:
import arcpy

# Input parameters:
arcpy.AddMessage("Defining variables.")
buffer_feature = arcpy.GetParameterAsText(0)
buffer_distance = arcpy.GetParameterAsText(1)
output_buffer = arcpy.GetParameterAsText(2)
intersect_features = arcpy.GetParameterAsText(3)
output_intersect = arcpy.GetParameterAsText(4)

tbx = "Z:\GEOG5790\practical1_modelbuilder\Data\Practical1.tbx"

try:
    try:
        arcpy.AddMessage("Importing toolbox {0}.".format(tbx))
        arcpy.ImportToolbox(tbx, "Practical1")
    except arcpy.ExecuteError as e:
        arcpy.AddMessage("Error importing toolbox {0}.".format(tbx))
        print("Import toolbox error", e)
    try:
        arcpy.AddMessage("Running Explosion model.")
        arcpy.ExplosionModel_Practical1(buffer_feature, buffer_distance, intersect_features, output_intersect)
    except arcpy.ExecuteError as e:
        arcpy.AddMessage("Error running Explosion model.")
        print("Model run error", e)
except Exception as e:
    print(e)

