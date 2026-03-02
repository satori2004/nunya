"""
Code used to reproject all the feature classes from one geodatabase to another geodatabase. 
Inputs are the paths to both geodatabases, original spatial reference (EPSG), and new spatial reference (EPSG)
"""


import arcpy
import os

# ---- User Inputs ----
input_gdb = 
output_gdb = 

##Alpena
# input_sr = arcpy.SpatialReference(102689)  # NAD 1983 StatePlane Michigan Central FIPS 2112 Feet (EPSG: 26912)
# output_sr = arcpy.SpatialReference(32617)  # WGS 1984 UTM Zone 17N (EPSG: 32617)  (Alpena)

##Capital
# input_sr = arcpy.SpatialReference(3436) # NAD 1983 StatePlane Illinois West FIPS 1202 (US Feet)
# output_sr = arcpy.SpatialReference(32616)  # WGS_1984_UTM_Zone_16N  (Capital)

##Kellogg
# input_sr = arcpy.SpatialReference(102690) # NAD 1983 StatePlane Michigan South FIPS 2113 (US Feet)
# output_sr = arcpy.SpatialReference(32616)  # WGS_1984_UTM_Zone_16N  (Kellogg)


##Peoria
input_sr = arcpy.SpatialReference(3436) # NAD 1983 StatePlane Illinois West FIPS 1202 (US Feet)
output_sr = arcpy.SpatialReference(32616)  # WGS_1984_UTM_Zone_16N  (Peoria)
transformation = "WGS_1984_(ITRF00)_To_NAD_1983"  # Geographic transformation

# Create output GDB if it doesn't exist
if not arcpy.Exists(output_gdb):
    arcpy.CreateFileGDB_management(os.path.dirname(output_gdb), os.path.basename(output_gdb))

# Set environment
arcpy.env.workspace = input_gdb

# List all feature classes (not tables)
feature_classes = arcpy.ListFeatureClasses()

# Loop through feature classes and reproject
for fc in feature_classes:
    print(f"Reprojecting: {fc}")
    in_fc = os.path.join(input_gdb, fc)
    out_fc = os.path.join(output_gdb, fc)
    
    # Get spatial reference of input FC (optional for checking)
    desc = arcpy.Describe(in_fc)
    in_sr = desc.spatialReference
    
     
    # Reproject with geographic transformation
    arcpy.Project_management(in_fc, out_fc, output_sr, transformation)
    print(f" - Done: {out_fc}")

print("All Done!")






### get the factory code for a feature class: 

fc_path = r"C:\path\to\your\geodatabase.gdb\your_feature_class"

# Get the spatial reference object
desc = arcpy.Describe(fc_path)
sr = desc.spatialReference

# Print the spatial reference name and WKID (factory code)
print("Spatial Reference Name:", sr.name)
print("Factory Code (WKID):", sr.factoryCode)




# ##Print out the factory (WKID) for each FC in a geodatabase

import arcpy

arcpy.env.workspace = "C:\\Shared\\Box\\Fed_DOD\\USACE-Louisville\\W912QR-19-D-0047 - ATI-CTI JV LLC\\TO-W912QR-20-F0393-IL PFAS RI\\7.0 Drawings&Specifications\\GIS\\IL_PFAS\\Figures\\Figures for RI Report\\RI Report ArcGIS Project\\Capital_ANGB_RI_Report_ArcGIS_Pro_Project\\Capital_RI_Only_FCs.gdb"

fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    desc = arcpy.Describe(fc)
    sr = desc.spatialReference
    print(f"{fc}: ", sr.factoryCode)



