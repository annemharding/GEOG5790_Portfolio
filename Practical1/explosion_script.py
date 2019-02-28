# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
Anne Harding, 12/02/2019
GEOG5790 - Practical 1 - ModelBuilder
Script to buffer input feature and intersect with other input features.
# ---------------------------------------------------------------------------

# Import arcpy module:
import arcpy

# Script arguments
buffer_feature = arcpy.GetParameterAsText(0)
buffer_distance = arcpy.GetParameterAsText(1)
intersect_features = arcpy.GetParameterAsText(2)
output_intersect = arcpy.GetParameterAsText(3)
if output_intersect == '#' or not output_intersect:
    output_intersect = "\\\\ds.leeds.ac.uk\\student\\student42\\ee13amh\\ArcGIS\\Default.gdb\\Intersect" # provide a default value if unspecified

# Local variables:
output_buffered_feature = "Buffer"

# Process: Buffer
arcpy.Buffer_analysis(buffer_feature, output_buffered_feature, buffer_distance, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis([intersect_features, output_buffered_feature], output_intersect, "ALL", "", "INPUT")

