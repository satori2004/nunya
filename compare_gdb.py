# import arcpy
# import os  



# def compare_feature_classes(gdb1, gdb2):
#     """
#     Compare the feature classes (by name) in two geodatabases to check if they are identical or different.
    
#     Parameters:
#     - gdb1: Path to the first geodatabase
#     - gdb2: Path to the second geodatabase
    
#     Returns:
#     - A message indicating whether the feature classes are identical or different.
#     """
    
#     # Get the feature classes from both geodatabases
#     feature_classes_gdb1 = arcpy.ListFeatureClasses("*", "ALL", gdb1) or []  # Return empty list if None
#     feature_classes_gdb2 = arcpy.ListFeatureClasses("*", "ALL", gdb2) or []  # Return empty list if None
    
#     # Step 1: Compare the feature classes between the two geodatabases
#     feature_classes_gdb1_set = set(feature_classes_gdb1)
#     feature_classes_gdb2_set = set(feature_classes_gdb2)
    
#     # Compare the two sets to find differences
#     missing_in_gdb2 = feature_classes_gdb1_set - feature_classes_gdb2_set
#     missing_in_gdb1 = feature_classes_gdb2_set - feature_classes_gdb1_set
    
#     # Print the feature classes that are missing in each geodatabase
#     if missing_in_gdb2:
#         print(f"Feature classes present in GDB1 but not GDB2: {missing_in_gdb2}")
#     if missing_in_gdb1:
#         print(f"Feature classes present in GDB2 but not GDB1: {missing_in_gdb1}")
    
#     # Step 2: If no missing feature classes, print that they are identical
#     if not missing_in_gdb2 and not missing_in_gdb1:
#         print("Feature classes in GDB1 and GDB2 are identical.")


# # Usage example
# gdb1 = r"C:\Users\jmcateer\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\Grissom\DGI\Basemap-TCRA-Goby-TP\FigureGIS\GDB\GIS\GrissomARB_CTI.gdb"
# gdb2 = r"C:\Users\jmcateer\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\Grissom\DGI\Basemap-TCRA-Goby-TP\GIS\GrissomARB_CTI.gdb"

# compare_feature_classes(gdb1, gdb2)



#----------------------
#all objects in databases
#----------------------

import arcpy 
import os


"""
Compare the contents of two file geodatabases, including: standalone feature classes, tables, fcs in feature datasets, rasters. 
"""

def get_gdb_contents(gdb_path):
    """Return a set of all objects in a geodatabase"""
    arcpy.env.workspace = gdb_path
    objects = set()

    # Standalone feature classes
    for fc in arcpy.ListFeatureClasses():
        objects.add(fc)

    # Feature datasets and their feature classes
    for fd in arcpy.ListDatasets(feature_type="feature"):
        objects.add(fd)  # include dataset itself
        for fc in arcpy.ListFeatureClasses(feature_dataset=fd):
            objects.add(os.path.join(fd, fc))  # keep dataset structure

    # Tables
    for table in arcpy.ListTables():
        objects.add(table)

    # Rasters
    for raster in arcpy.ListRasters():
        objects.add(raster)

    return objects


# ---- INPUT GDB PATHS ----
gdb1 = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB.gdb"
gdb2 = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB_new.gdb"

# Get contents
gdb1_objects = get_gdb_contents(gdb1)
gdb2_objects = get_gdb_contents(gdb2)

# Compare
only_in_gdb1 = gdb1_objects - gdb2_objects
only_in_gdb2 = gdb2_objects - gdb1_objects

# ---- PRINT RESULTS ----
print("\nObjects ONLY in GDB 1:")
if only_in_gdb1:
    for obj in sorted(only_in_gdb1):
        print("  " + obj)
else:
    print("  None")

print("\nObjects ONLY in GDB 2:")
if only_in_gdb2:
    for obj in sorted(only_in_gdb2):
        print("  " + obj)
else:
    print("  None")