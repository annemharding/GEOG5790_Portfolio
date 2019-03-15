'''
GEOG5790 - Practical 4 (GUI)
Anne Harding (200754573), 14/02/2019
------------------------------------------------
Python script of Trafford Model to be called by Add-In button.
'''

# Import modules:
import arcpy

# Define Arc environments:
wkspc = r"Z:/GEOG5790/practical4"           # define workspace
arcpy.env.workspace = wkspc                 # set workspace
mxd = arcpy.mapping.MapDocument("CURRENT")  # get current .mxd
df = mxd.activeDataFrame                    # get current dataframe

# PARAMETERS:
# Get input parameters from GUI:
Burglaries = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Buildings = arcpy.GetParameterAsText(2)
# Define location of output parameters:
Out = wkspc + "/generated_data/crime.shp"
Sorted_Out = wkspc + "/generated_data/crime_sorted.shp"

# Check if output files are already open in the .mxd. If so, remove.
arcpy.AddMessage("Removing existing output files from .mxd:")
for lyr in arcpy.mapping.ListLayers(mxd, "crime", df):  
    arcpy.mapping.RemoveLayer(df,lyr)
for lyr in arcpy.mapping.ListLayers(mxd, "crime_sorted", df):
    arcpy.mapping.RemoveLayer(df,lyr)

# Loop through output files to check they don't already exist. If so, delete.
files = [Out, Sorted_Out]
arcpy.AddMessage("Checking if output files already exist.")
for file in files:
    if arcpy.Exists(file):
        arcpy.AddMessage(file + " exists. Deleting existing file.")
        arcpy.Delete_management(file)

# Run Trafford Model from Practical 4 toolbox:
arcpy.AddMessage("Running Trafford Model.")
arcpy.ImportToolbox("Z:/GEOG5790/practical4/practical4.tbx", "practical4")
arcpy.TraffordModel_practical4(Burglaries, Distance, Buildings, Out)

# Sort data by "Join_Count" field:
# arcpy.AddMessage("Sorting output data.")
# arcpy.Sort_management(Out, Sorted_Out, [["Join_Count", "DESCENDING"]])
'''
I get the following error here, which I have not been able to solve:
"Traceback (most recent call last):
  File "Z:\GEOG5790\practical4\traffordmodelscript.py", line 41, in <module>
    arcpy.Sort_management(Out, Sorted_Out, [["Join_Count", "DESCENDING"]])
  File "c:\program files (x86)\arcgis\desktop10.6\arcpy\arcpy\management.py", line 4591, in Sort
    raise e
ExecuteError: ERROR 999999: Error executing function.
Cannot acquire a lock.
Cannot acquire a lock.
Failed to execute (Sort)."
But this should not matter, as the same symbology will be applied to the data whether it
has been sorted or not.
'''

# SYMBOLOGY:
# Make a new layer from the sorted crime data:
newlayer = arcpy.mapping.Layer(Out)
# Make a new layer from the example layer file:
layerFile = arcpy.mapping.Layer(wkspc + "/albertsquare/buildings.lyr")
# Update the data layer with the symbology from the example layer file:
arcpy.mapping.UpdateLayer(df, newlayer, layerFile, True)
# Print layer's symbology type to screen to check that it is "UNIQUE_VALUES":
arcpy.AddMessage(newlayer.symbologyType)
# Coloured by the values in the "Join_Count" field:
# THIS LINE IS UNNECESSARY AS THE APPLIED SYMBOLOGY ALREADY USES THE "Join_Count" FIELD:
# newlayer.symbology.valueField = "Join_Count"
# Add all unique values from the "Join_Count" field to the symbology:
# newlayer.symbology.addAllValues()
'''
Get error here:
Traceback (most recent call last):
  File "Z:\GEOG5790\practical4\traffordmodelscript.py", line 78, in <module>
    newlayer.symbology.addAllValues()
  File "c:\program files (x86)\arcgis\desktop10.6\arcpy\arcpy\_mapping.py", line 1375, in addAllValues
    return convertArcObjectToPythonObject(self._arc_object.addAllValues(*gp_fixargs((), True)))
RuntimeError

Tried to use the following instead to obtain the unique values from the file,
but I get an error saying 'cannot acquire a lock':

values = []
rows = arcpy.da.SearchCursor(newlayer, ["Join_Count"])
for row in rows:
    values.append(row[0])
newlayer.symbology.classValues = values
'''
newlayer.symbology.showOtherValues = True
# Add data layer to the map at the TOP of the dataframe:
arcpy.mapping.AddLayer(df, newlayer, "TOP")

# Refresh view and Table of Contents to ensure user is seeing most up-to-date view:
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

'''
Other functions I tried to apply the example layer's symbology:
arcpy.MakeFeatureLayer_management(Out, Out_lyr)
arcpy.SaveToLayerFile_management(Out_lyr, Out_lyr)
arcpy.ApplySymbologyFromLayer_management(newlayer, layerFile)
'''

