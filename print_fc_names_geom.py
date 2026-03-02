import arcpy
import os

def print_geometry_types(workspace, fc_names):
    arcpy.env.workspace = workspace
    print(f"\nWorkspace: {workspace}")
    print("=" * 50)

    # List all feature datasets in the workspace
    datasets = arcpy.ListDatasets(feature_type='feature') or []

    for fc_name in fc_names:
        found = False

        # --- Check standalone feature classes ---
        if fc_name in arcpy.ListFeatureClasses():
            desc = arcpy.Describe(fc_name)
            print(f"\nFeature Class: {fc_name}")
            print("Feature Dataset: None (Standalone)")
            print(f"Geometry Type: {desc.shapeType}")
            found = True

        # --- Check feature datasets ---
        if not found:
            for dataset in datasets:
                fcs_in_dataset = arcpy.ListFeatureClasses(feature_dataset=dataset) or []
                if fc_name in fcs_in_dataset:
                    full_path = os.path.join(workspace, dataset, fc_name)
                    desc = arcpy.Describe(full_path)
                    print(f"\nFeature Class: {fc_name}")
                    print(f"Feature Dataset: {dataset}")
                    print(f"Geometry Type: {desc.shapeType}")
                    found = True
                    break

        if not found:
            print(f"\nFeature Class: {fc_name} not found in workspace!")

if __name__ == "__main__":
    # Example workspace and list of feature class names
    workspace = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"
    fc_names = [
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
'SS028May2022_AreaC',
'SS028_May2022_VC_Area_C',
'SS028_May2022_VC_Area_C_merged',
'SS028_May2022_TCE_Area_C',
'SS028_May2022_TCE_Area_C_merged',
'SS028_May2022_TCE_Area_E',
'SS028_May2022_TCE_Area_E_pol',
'SS028_May2022_VC_Area_E',
'SS028_May2022_VC_Area_E_merge',
'SS028_May2022_TCE_Area_E_merge',
'SS032_MW06_May2022_VC_Oct',
'SS032_MW06_May2022_VC_Merge',
'SS032_W128_May2022_TCE',
'SS032_W128_May2022_TCE_merge',
'SS032_W128_May2022_VC',
'SS028_May2022_Area_E_COCs',
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
'SS032_TCE_VC_Oct2022',
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

    print_geometry_types(workspace, fc_names)