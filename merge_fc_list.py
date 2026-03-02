"""
Script Name: Merge Feature Classes with Selected Fields

Description:
This script merges a list of feature classes from a geodatabase into a single new feature class.
Only specific fields are mapped from the source feature classes to the output:
    - sdsFeatureName
    - sdsFeatureDescription
    - narrative

Functionality:
1. Loops through the user-specified list of feature classes to merge.
2. Uses ArcPy FieldMappings to ensure that the specified fields are mapped correctly.
3. Creates a new feature class in the same geodatabase with the merged features and mapped fields.
4. Prints a success message if the merge completes or an error message if it fails.

Inputs:
- gdb_path: Path to the geodatabase containing the feature classes.
- feature_classes_to_merge: List of feature class names to include in the merge.
- output_fc: Name of the output merged feature class.

Outputs:
- A new feature class in the geodatabase with all selected features merged.
- Only the mapped fields (sdsFeatureName, sdsFeatureDescription, narrative) are included in the output.

Requirements:
- ArcGIS with ArcPy installed.
- The input feature classes must exist in the specified geodatabase.
- The specified fields must exist in the input feature classes; missing fields are skipped during mapping.

Usage:
- Update the gdb_path, feature_classes_to_merge, and output_fc variables.
- Run the script in an ArcGIS Python environment.
"""



import arcpy
import os

# -----------------------------
# Inputs
# -----------------------------
gdb_path = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb" 
arcpy.env.workspace = gdb_path

# List of feature classes to merge
feature_classes_to_merge = [
'Oct_2020_TCE_Plumes',
'SS028_Feb2022_TCE_Area_C',
'SS028_Feb2022_TCE_Area_B',
'SS028_Feb2022_VC_Area_A',
'SS028_Feb2022_VC_Area_B',
'SS032_Feb2022_TCE_Area_W128',
'SS032_Feb2022_VC_Area_MW06V2',
'SS028_May2022_VC_Area_A',
'SS028_May2022_VC_Area_A_round',
'VC_2020_Plume',
'VC_2020_Plume_MW06',
'SS028_Feb2022_VC_Area_C',
'SS028_Feb2022_VC_Area_E',
'SS028_Feb2022_TCE_Area_E',
'SS028_Area_A_OCT23_VC',
'SS028_Area_A_OCT23_VC_scrub',
'SS028_Oct_23_TCE_B',
'SS028_Oct_23_VC_B',
'SS028_Oct_23_VC_B_scrub',
'SS028_Area_B_OCT23_TCE_scrub',
'SS028_Area_B_OCT23_TCE',
'SS028_Area_B_OCT23_TCE_scrub2',
'SS028_Oct_23_TCE_C',
'SS028_Area_C_OCT23_TCE_scrub',
'SS028_Area_C_OCT23_VC_scrub',
'SS028_Area_C_OCT23_VC',
'SS028_Area_E_OCT23_VC_scrub',
'SS028_Area_E_OCT23_VC',
'SS028_Area_E_OCT23_TCE_scrub',
'SS028_Area_E_OCT23_TCE',
'MW06TCE_1023',
'MW06_VC_1023',
'MW06_VC_1023_orig',
'W128_TCE_1023',
'W128_VC_1023',
'SS028_Area_A_OCT23_VC_Jun24Revise',
'SS028_Area_E_OCT23_TCE_Jun24Rev',
'Contour_SS028_A_VC_1024',
'Contour_SS028_B_TCE_1_Buffer',
'VC2021Plume',
'Contour_SSI_TCE1',
'SS028_May2022_TCE_Area_B',
'SS028_May2022_TCE_Area_B_Merged',
'SS028_May2022_VC_Area_B',
'SS028_May2022_VC_Area_B_merged',
'SS028_May2022_VC_AreaA',
'SS028_May2022_VC_AreaA_merged',
'SS028_May2022_VC_Area_C',
'SS028_May2022_VC_Area_C_merged',
'SS028_May2022_TCE_Area_C',
'SS028_May2022_TCE_Area_C_merged',
'SS028_May2022_TCE_Area_E_pol',
'SS028_May2022_VC_Area_E',
'SS028_May2022_VC_Area_E_merge',
'SS028_May2022_TCE_Area_E_merge',
'SS032_MW06_May2022_VC_Oct',
'SS032_MW06_May2022_VC_Merge',
'SS032_W128_May2022_TCE',
'SS032_W128_May2022_TCE_merge',
'SS032_W128_May2022_VC',
'SS028_TCE_Area_A_Plume',
'SS028_VC_Area_A_Plume',
'SS028_TCE_Area_C_Plume',
'SS028_TCE_Area_C_Plume_adj',
'SS028_VC_Area_C_Plume',
'SS028_TCE_Area_B_Plume',
'SS028_TCE_Area_B_Plume_adj',
'SS028_TCE_Area_B_Plume_scrubbed',
'SS028_VC_Area_B_Plume',
'SS028_VC_Area_E_Plume',
'SS028_TCE_Area_E_Plume',
'SS032_TCE_MW06_Plume',
'SS032_VC_W128_Plume',
'SS032_TCE_W128_Plume',
'SS032_VC_MW06_Plume',
'CVOC_Plume102022',
'SS032_May2023_VC',
'Area_B_May2023_VC',
'Area_B_May2023_TCE',
'Area_B_May2023_TCE_5',
'Area_B_May2023_TCE_Scrubbed',
'Area_B_May2023_VC_Scrubbed',
'October_2022_TCE',
'May_2022_TCE',
'COC_Plume'
    # Add more as needed
]

# Output feature class name
output_fc = "PotentialContaminationSite_Merged"  # Name of the output merged feature class

# -----------------------------
# Field mapping
# -----------------------------
field_mappings = arcpy.FieldMappings()

# For each field we want to keep in the output
fields_to_map = [
'sdsFeatureDescription',
'sdsFeatureName',
'narrative'
]

for field in fields_to_map:
    fm = arcpy.FieldMap()
    for fc in feature_classes_to_merge:
        # Only add the field if it exists in the source FC
        existing_fields = [f.name for f in arcpy.ListFields(fc)]
        if field in existing_fields:
            fm.addInputField(fc, field)
    # Rename output field to standard name
    out_field = fm.outputField
    out_field.name = field
    fm.outputField = out_field
    field_mappings.addFieldMap(fm)

# -----------------------------
# Merge
# -----------------------------
try:
    arcpy.Merge_management(feature_classes_to_merge, output_fc, field_mappings)
    print(f"Successfully merged into {output_fc}")
except Exception as e:
    print(f"Error during merge: {e}")