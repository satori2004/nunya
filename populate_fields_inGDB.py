"""
Script Name: Populate Narrative Field

Description:
This script populates the 'narrative' field in specified feature classes
within a geodatabase. For each feature class provided in the input list,
the script updates all records so that the 'narrative' field contains
the value 'Source:' followed by the feature class name.

The script supports feature classes stored at the root level of the
geodatabase as well as those contained within feature datasets.
"""

import arcpy
import os

def populate_narrative_field(gdb_path, featureclass_list):
    arcpy.env.workspace = gdb_path

    for fc in featureclass_list:

        # Find the full path (handles feature datasets automatically)
        fc_path = None
        for dirpath, dirnames, filenames in arcpy.da.Walk(gdb_path, datatype="FeatureClass"):
            if fc in filenames:
                fc_path = os.path.join(dirpath, fc)
                break

        if not fc_path:
            print(f"{fc} not found.")
            continue

        # Ensure field exists
        field_names = [f.name for f in arcpy.ListFields(fc_path)]
        if "narrative" not in field_names:
            print(f"'narrative' field does not exist in {fc}")
            continue

        # Only the feature class name (not the path)
        value = f"Source:{fc}"

        with arcpy.da.UpdateCursor(fc_path, ["narrative"]) as cursor:
            for row in cursor:
                row[0] = value
                cursor.updateRow(row)

        print(f"Updated narrative field in {fc}")

if __name__ == "__main__":
    gdb = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"
    featureclasses = [
'SiteBoundary',
'Roads',
'LF005_007_012_Wells',
'SiteBoundary_LF006',
'InstallationArea',
'TreatmentArea',
'HydroSubDivide',
'SS032_Well',
'SS032_MW06_Well',
'SiteWells',
'GPS_points05082022',
'SS032_TreatmentArea',
'CAFB_MW_Complete',
'CAFB_Feb2022_GWE',
'Shallow_wells',
'Oct_2020_TCE_Plumes',
'Oct_2020_GWE',
'CAFB_2022Feb_GWE_SS028',
'GW_FlowDirection_OCT2020',
'CAFB_Feb2022_GWE_half',
'Fall2022_TCE_VC',
'SS028_Feb2022_TCE_Area_C',
'SS028_Feb2022_TCE_Area_B',
'SS028_Feb2022_VC_Area_A',
'SS028_Feb2022_VC_Area_B',
'GW_Well_COCs_Feb2022',
'SS032_Feb2022_TCE_Area_W128',
'SS032_Feb2022_VC_Area_MW06V2',
'CAFB_May2022_GWE',
'SS028_May2022_VC_Area_A',
'SS028_May2022_VC_Area_A_round',
'GW_Wells_Area_A',
'LF009_Park',
'wLineMaine_L',
'MowedAreas',
'VC_2020_Plume',
'VC_2020_Plume_MW06',
'SS028_Feb2022_VC_Area_C',
'SS028_Feb2022_VC_Area_E',
'SS028_Feb2022_TCE_Area_E',
'FEB2022GWL_SS032',
'HRSC_sampleLOC',
'UtilityCoridor',
'CAFB_OCT_2023_GWE',
'CAFB_OCT_2023_GWE_Baseline',
'CAFB_OCT_2023_GWE_17Jan23',
'CAFB_OCT_2023_SS028_COCs',
'SS028_Area_A_OCT23_VC',
'SS028_Area_A_OCT23_VC_scrub',
'SS028_Oct_23_TCE_B',
'SS028_Oct_23_VC_B',
'SS028_Oct_23_VC_B_scrub',
'Est_Plume',
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
'CAFB_OCT2023_COC',
'MW06TCE_1023',
'MW06_VC_1023',
'MW06_VC_1023_orig',
'W128_TCE_1023',
'W128_VC_1023',
'SS028_Area_A_OCT23_VC_Jun24Revise',
'SS028_Area_E_OCT23_TCE_Jun24Rev',
'CAFB_AFFF',
'CAFB_Oct2024_GWE',
'HRSC_CoordsT',
'HRSC_TempWell',
'HRSC_TempWellHRSC_Fig3_TW',
'New_Monitoring_WellNMW',
'Wells_2024_table_XYTableToPoint',
'CAFB_AreaB_Wells2024',
'CAFB_MW_Oct2024',
'CAFB_MW_OCT24',
'Contour_SS028_A_VC_1024',
'Contour_SS028_B_TCE_1_Buffer',
'VC2021Plume',
'Cross_Section',
'CAFB_25MayGWE',
'Well_Merge',
'Well_Merge_Merge',
'Contour_SSI_TCE1',
'CAFB_2025Nov_GWE_SS032_pts',
'CAFB_2025Nov_GWE_SS028_pts',
'SS028May2022_AreaB',
'SS032_MW06_May2022',
'SS028_May2022_TCE_Area_B',
'SS028_May2022_TCE_Area_B_Merged',
'SS028_May2022_VC_Area_B',
'SS028_May2022_VC_Area_B_merged',
'SS028_May2022_VC_AreaA',
'SS028_May2022_VC_AreaA_merged',
'SS028May2022_AreaC',
'SS028_May2022_VC_Area_C',
'SS028_May2022_VC_Area_C_merged',
'SS028_May2022_TCE_Area_C',
'SS028_May2022_TCE_Area_C_merged',
'SS028May2022_AreaE',
'SS028_May2022_TCE_Area_E',
'SS028_May2022_TCE_Area_E_pol',
'SS028_May2022_VC_Area_E',
'SS028_May2022_VC_Area_E_merge',
'SS028_May2022_TCE_Area_E_merge',
'SS032_MW06_May2022_const',
'SS032_MW06_May2022_VC_Oct',
'SS032_MW06_May2022_VC_Merge',
'SS032_W128_May2022',
'SS032_W128_May2022_TCE',
'SS032_W128_May2022_TCE_merge',
'SS032_W128_May2022_VC',
'May_2022_GWL_Scrubbed',
'SS028_May2022_Area_E_COCs',
'MW_GWE_Oct2022',
'MW_LF006_GWE_Oct2022',
'SS032_MW_GWE_Oct2022_V4',
'SS028_TCE_VC_Oct2022',
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
'Aquifer_1_wells',
'SS032_TCE_VC_Oct2022',
'SS032_TCE_MW06_Plume',
'SS032_VC_W128_Plume',
'SS032_TCE_W128_Plume',
'SS032_VC_MW06_Plume',
'CVOC_Plume102022',
'CAFB_May2023_MW',
'SS032_May2023_MW_COCs',
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

    populate_narrative_field(gdb, featureclasses)
