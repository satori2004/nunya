
"""
Code can be used to create new fields in all the feature classes in a given database; 
Primary use case: add sdsFeatureName and sdsFeatureDescription fields to all FCs in a gdb file. 
"""


# import arcpy
# import os

# # Path to the geodatabase
# gdb_path = r"C:\path\to\your\geodatabase.gdb"

# # Set the workspace to the geodatabase
# arcpy.env.workspace = gdb_path

# # List all feature classes in the geodatabase
# feature_classes = arcpy.ListFeatureClasses()

# # Loop through each feature class
# for fc in feature_classes:
#     try:
#         # Define the field names
#         sdsFeatureName_field = "sdsFeatureName"
#         sdsFeatureDescription_field = "sdsFeatureDescription"
        
#         # Check if the field already exists before adding
#         fields = [field.name for field in arcpy.ListFields(fc)]
        
#         # Add the 'sdsFeatureName' field if it doesn't already exist
#         if sdsFeatureName_field not in fields:
#             arcpy.AddField_management(fc, sdsFeatureName_field, "TEXT", field_length=255)
#             print(f"Added field '{sdsFeatureName_field}' to {fc}")
        
#         # Add the 'sdsFeatureDescription' field if it doesn't already exist
#         if sdsFeatureDescription_field not in fields:
#             arcpy.AddField_management(fc, sdsFeatureDescription_field, "TEXT", field_length=255)
#             print(f"Added field '{sdsFeatureDescription_field}' to {fc}")

#     except Exception as e:
#         print(f"Error processing {fc}: {str(e)}")



#------------------#
#loops thorugh all feature classes and feature datasets in a geodatabase and adds sdsFeatureName and sdsFeatureDescription fields to each fc
# checks if the field already exists before attempting to add it, and prints a message for each field added or skipped
#------------------#    

import arcpy
import os

# Path to the geodatabase
gdb_path = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"

# Set workspace
arcpy.env.workspace = gdb_path

# List feature datasets (include root)
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets else ['']

for ds in datasets:
    feature_classes = arcpy.ListFeatureClasses(feature_dataset=ds)

    for fc in feature_classes:
        try:
            # Build full path and display name
            if ds:
                fc_path = os.path.join(gdb_path, ds, fc)
                display_name = f"{ds}\\{fc}"
            else:
                fc_path = os.path.join(gdb_path, fc)
                display_name = fc

            # Define field names
            sdsFeatureName_field = "sdsFeatureName"
            sdsFeatureDescription_field = "sdsFeatureDescription"
            narrative_field = "narrative"

            # Get current fields
            existing_fields = [field.name for field in arcpy.ListFields(fc_path)]

            # Check and add sdsFeatureName
            if sdsFeatureName_field in existing_fields:
                print(f"Field '{sdsFeatureName_field}' already exists in {display_name} — skipping.")
            else:
                arcpy.AddField_management(fc_path, sdsFeatureName_field, "TEXT", field_length=255)
                print(f"Added field '{sdsFeatureName_field}' to {display_name}")

            # Refresh field list (optional but safest practice)
            existing_fields = [field.name for field in arcpy.ListFields(fc_path)]

            # Check and add sdsFeatureDescription
            if sdsFeatureDescription_field in existing_fields:
                print(f"Field '{sdsFeatureDescription_field}' already exists in {display_name} — skipping.")
            else:
                arcpy.AddField_management(fc_path, sdsFeatureDescription_field, "TEXT", field_length=255)
                print(f"Added field '{sdsFeatureDescription_field}' to {display_name}")

             # Check and add narrative field
            if narrative_field in existing_fields:
                print(f"Field '{narrative_field}' already exists in {display_name} — skipping.")
            else:
                arcpy.AddField_management(fc_path, narrative_field, "TEXT", field_length=255)
                print(f"Added field '{narrative_field}' to {display_name}")

        except Exception as e:
            print(f"Error processing {display_name}: {str(e)}")


