import arcpy
import re
import os

# -----------------------------
# Geodatabase path
# -----------------------------
gdb_path = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"  # Update this
arcpy.env.workspace = gdb_path

# -----------------------------
# List of feature classes to process (exact names)
# -----------------------------
fc_names_to_process = [
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

]

# -----------------------------
# Helper functions
# -----------------------------
def extract_date(name):
    patterns = [
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[_]?\d{2,4}',
        r'\b\d{4}\b',
        r'\b\d{2}23\b',
        r'\b\d{6}\b'
    ]
    for pattern in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            return match.group(0)
    return "None"

def extract_analyte(name):
    analytes = ['TCE', 'VC', 'COC', 'COCs', 'CVOC']
    tokens = re.split(r'[^A-Za-z0-9]+', name.upper())
    found = [a for a in analytes if a in tokens]
    if not found:
        return "None"
    return " & ".join(sorted(set(found)))

# -----------------------------
# Main loop: feature datasets
# -----------------------------
feature_datasets = arcpy.ListDatasets(feature_type='Feature') or []
feature_datasets.append(None)  # include root of GDB

for fd in feature_datasets:
    if fd:
        workspace = os.path.join(gdb_path, fd)
        arcpy.env.workspace = workspace
        print(f"Processing feature dataset: {fd}")
    else:
        workspace = gdb_path
        arcpy.env.workspace = workspace
        print(f"Processing root of GDB")

    # List feature classes in this workspace/dataset
    fcs = arcpy.ListFeatureClasses() or []

    # Filter feature classes by the user-provided list
    fcs_to_update = [fc for fc in fcs if fc in fc_names_to_process]

    for fc in fcs_to_update:
        print(f"  Updating feature class: {fc}")

        # Ensure fields exist
        fields = [f.name for f in arcpy.ListFields(fc)]
        if "sdsFeatureName" not in fields:
            arcpy.AddField_management(fc, "sdsFeatureName", "TEXT", field_length=255)
        if "sdsFeatureDescription" not in fields:
            arcpy.AddField_management(fc, "sdsFeatureDescription", "TEXT", field_length=255)

        # Check for contour min/max
        min_field = "ContourMin" if "ContourMin" in fields else None
        max_field = "ContourMax" if "ContourMax" in fields else None

        cursor_fields = ["sdsFeatureName", "sdsFeatureDescription"]
        if min_field and max_field:
            cursor_fields += [min_field, max_field]

        with arcpy.da.UpdateCursor(fc, cursor_fields) as cursor:
            for row in cursor:
                analyte = extract_analyte(fc)
                date = extract_date(fc)

                # Contour values
                if min_field and max_field:
                    min_val = row[2] if row[2] is not None else "None"
                    max_val = row[3] if row[3] is not None else "None"
                else:
                    min_val = "None"
                    max_val = "None"

                # Update fields
                row[0] = f"{analyte}; {date}; {min_val} – {max_val}"
                row[1] = "Groundwater Plume"

                cursor.updateRow(row)

print("Selected feature classes updated successfully.")