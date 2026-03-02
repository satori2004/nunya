#--------------------------------
# Print the names of all the ojects in a file geodatabase.
#--------------------------------


import arcpy

arcpy.env.workspace = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB.gdb"

# List all feature classes in the workspace
fc_list = arcpy.ListFeatureClasses()

# List all feature datasets in the workspace
fd_list = arcpy.ListDatasets(feature_type='feature')  # 'feature' will list feature datasets

# List all tables in the workspace
table_list = arcpy.ListTables()

# Print feature classes
for fc in fc_list:
    # print("Feature Class: " + fc)
    print(fc)

# Print feature datasets and their feature classes
for fd in fd_list:
    print("Feature Dataset: " + fd)
    feature_classes_in_fd = arcpy.ListFeatureClasses(feature_dataset=fd)  # List feature classes in the dataset
    for fc in feature_classes_in_fd:
        # print("  Feature Class in Dataset: " + fc)
        print(fc)

# Print tables
for table in table_list:
    # print("Table: " + table)
    print(table)

# List all rasters in the workspace
raster_list = arcpy.ListRasters()

# Print rasters
for raster in raster_list:
    # print("Raster: " + raster)
    print(raster)


# --------------------------------
# Print the names of all the tables in a file geodatabase.
# --------------------------------

# import arcpy

# # Path to the geodatabase
# gdb_path = r"C:\Shared\Box\Commercial\Duke Energy\Duke Atlas Files\G Drive Files\GIBSON\GW Statistics\GIS\Gibson\GIS\Gibson_Database.gdb"

# arcpy.env.workspace = gdb_path

# # List and print all tables
# tables = arcpy.ListTables()

# if tables:
#     for table in tables:
#         print(table)
# else:


# --------------------------------
# Rename a geodatabase
# --------------------------------


# import os

# old_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB_new.gdb"
# new_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB.gdb"

# os.rename(old_gdb, new_gdb)

# print("Geodatabase renamed successfully.")




#--------------------------------
# create feature class for gdb. 
#-------------------------------- 

# import arcpy

# # Set workspace (update to your geodatabase or folder)
# workspace = r"C:\Shared\Box\Fed_DOD\USACE-Louisville\W912QR-19-D-0052 - CTI-TPMC-LATA\TO W912QR-20-F-0273 Great Lakes ORC\7.0 Drawings&Specifications\Figures\QAPP Figures\Default.gdb"
# arcpy.env.workspace = workspace

# # Feature class name
# fc_name = "Landfill_Crack"

# # Spatial reference: NAD 1983 StatePlane Ohio South FIPS 3402 (US Feet)
# spatial_ref = arcpy.SpatialReference(3735)

# # Create line feature class
# arcpy.management.CreateFeatureclass(
#     out_path=workspace,
#     out_name=fc_name,
#     geometry_type="POLYLINE",
#     spatial_reference=spatial_ref
# )

# # Add Landfill_ID (text field)
# arcpy.management.AddField(
#     in_table=fc_name,
#     field_name="Landfill_ID",
#     field_type="TEXT",
#     field_length=50
# )

# # Add Length_ft (double field)
# arcpy.management.AddField(
#     in_table=fc_name,
#     field_name="Length_ft",
#     field_type="DOUBLE"
# )

# print("Feature class 'Landfill_Crack' created with Ohio South StatePlane (US Feet).")





# #--------------------------
# #copy files from one folder to another
# #--------------------------

# import os

# def copy_folder(source, destination):
#     # Create destination folder if it doesn't exist
#     if not os.path.exists(destination):
#         os.makedirs(destination)

#     for item in os.listdir(source):
#         source_path = os.path.join(source, item)
#         destination_path = os.path.join(destination, item)

#         if os.path.isfile(source_path):
#             # Copy file manually
#             with open(source_path, 'rb') as src_file:
#                 with open(destination_path, 'wb') as dest_file:
#                     dest_file.write(src_file.read())

#         elif os.path.isdir(source_path):
#             # Recursively copy subfolder
#             copy_folder(source_path, destination_path)

# # Example usage
# source_folder = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\Imagery"
# destination_folder = r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\CLMBS"

# copy_folder(source_folder, destination_folder)

# print("Folder contents copied successfully.")
