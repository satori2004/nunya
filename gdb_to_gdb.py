"""
This script copies all major data types from a source file geodatabase
to a target file geodatabase, including:

- Feature datasets
- Feature classes (inside and outside feature datasets)
- Tables
- Raster datasets
- Mosaic datasets
"""

import arcpy
import os

# ----------------------------------------------------------
# USER VARIABLES
# ----------------------------------------------------------
source_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB.gdb"
target_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB_new.gdb"

overwrite_existing = True
# ----------------------------------------------------------

arcpy.env.overwriteOutput = overwrite_existing

print("Starting geodatabase copy...")
print(f"Source GDB: {source_gdb}")
print(f"Target GDB: {target_gdb}")

# ----------------------------------------------------------
# 1. COPY FEATURE DATASETS + THEIR FEATURE CLASSES
# ----------------------------------------------------------
arcpy.env.workspace = source_gdb
fds_list = arcpy.ListDatasets(feature_type="feature")

for fds in fds_list:
    source_fds = os.path.join(source_gdb, fds)
    target_fds = os.path.join(target_gdb, fds)

    if not arcpy.Exists(target_fds):
        desc = arcpy.Describe(source_fds)
        print(f"Creating Feature Dataset: {fds}")
        arcpy.CreateFeatureDataset_management(
            target_gdb, fds, desc.spatialReference
        )

    arcpy.env.workspace = source_fds
    for fc in arcpy.ListFeatureClasses():
        print(f"  Copying Feature Class: {fds}/{fc}")
        arcpy.CopyFeatures_management(
            os.path.join(source_fds, fc),
            os.path.join(target_fds, fc)
        )

# ----------------------------------------------------------
# 2. COPY STANDALONE FEATURE CLASSES
# ----------------------------------------------------------
arcpy.env.workspace = source_gdb
print("Copying standalone Feature Classes...")

for fc in arcpy.ListFeatureClasses():
    print(f"  Copying Feature Class: {fc}")
    arcpy.CopyFeatures_management(
        os.path.join(source_gdb, fc),
        os.path.join(target_gdb, fc)
    )

# ----------------------------------------------------------
# 3. COPY TABLES
# ----------------------------------------------------------
print("Copying Tables...")

for table in arcpy.ListTables():
    print(f"  Copying Table: {table}")
    arcpy.CopyRows_management(
        os.path.join(source_gdb, table),
        os.path.join(target_gdb, table)
    )

# ----------------------------------------------------------
# 4. COPY RASTER DATASETS
# ----------------------------------------------------------
print("Copying Raster Datasets...")

for raster in arcpy.ListRasters():
    print(f"  Copying Raster: {raster}")
    arcpy.CopyRaster_management(
        os.path.join(source_gdb, raster),
        os.path.join(target_gdb, raster)
    )

# ----------------------------------------------------------
# 5. COPY MOSAIC DATASETS
# ----------------------------------------------------------
print("Copying Mosaic Datasets...")

for mosaic in arcpy.ListDatasets("", "Mosaic"):
    print(f"  Copying Mosaic Dataset: {mosaic}")
    arcpy.Copy_management(
        os.path.join(source_gdb, mosaic),
        os.path.join(target_gdb, mosaic)
    )

print("Geodatabase copy completed successfully.")

