import arcpy

def add_date_field_to_featureclasses(geodatabase_path, featureclass_list):
    """
    Adds a TEXT field named 'Date' to each feature class in featureclass_list
    if it exists in the provided geodatabase and the field does not already exist.

    :param geodatabase_path: Path to the input geodatabase (str)
    :param featureclass_list: List of feature class names (list of str)
    """

    # Set workspace
    arcpy.env.workspace = geodatabase_path

    # Get all feature classes in the geodatabase (including within feature datasets)
    all_fcs = []
    datasets = arcpy.ListDatasets(feature_type='feature') or []
    datasets.append('')  # Include standalone feature classes

    for ds in datasets:
        fcs = arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fcs:
            if ds:
                all_fcs.append(f"{ds}/{fc}")
            else:
                all_fcs.append(fc)

    for fc in all_fcs:
        fc_name = fc.split("/")[-1]

        if fc_name in featureclass_list:
            fields = [field.name for field in arcpy.ListFields(fc)]

            if "narrative" not in fields:
                arcpy.AddField_management(
                    in_table=fc,
                    field_name="narrative",
                    field_type="TEXT",
                    field_length=255
                )
                print(f"Added 'narrative' field to {fc}")
            else:
                print(f"'narrative' field already exists in {fc}")

if __name__ == "__main__":
    # ---- USER INPUTS ----
    input_gdb = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"
    input_featureclasses = [
'GW_Flow',
'CAFB_2020_GWE',
'GW_FlowDirection',
'CAFB_Feb2022_GWE',
'CAFB_2022Feb_GWE',
'CAFB_2022Feb_GWE_SS032',
'CAFB_2022May_GWE',
'CAFB_2022May_GWE_SS028_adj',
'Kriging_contour_Feb2022',
'CAFB_2022Feb_Kriging_GWE',
'CAFB_2022Feb_GWE_Smooth',
'CAFB_Feb2022_SS032_GWE_half',
'Contour_SS028_sans113',
'CAFB_OCT_2023_GWE',
'Contour_Oct2023_V1',
'CAFB_OCT_2023_GWE_Baseline',
'Contour_Oct2023_V2',
'Contour_Oct2023_V2_Scrubbed',
'Contour_Oct2023_V2_Scrubbed_17JAN23',
'CAFB_OCT_2023_GWE_17Jan23',
'CAFB_OCT_2023_GWE_19JAN24',
'CAFB_OCT_2023_GWE_19JAN24_Baseline',
'Contour_Oct2023_V2_Smoothed',
'CAFB_OCT_2023_Flow_Direction',
'Contour_Oct2023_half',
'CAFB_2024May_Contour',
'CAFB_2024May_Contour_adj',
'CAFB_2024May_Contour_SS032',
'CAFB_Oct2024_GWE',
'CAFB_2024Oct_GWE',
'CAFB_2024Oct_GWE_1ft',
'CAFB_2024Oct_GWE_1ft_PG',
'CAFB_2025MayGWE_org',
'CAFB_2025MayGWE_1',
'CAFB_24Oct_GWE_1ft_adj',
'GWE052025_base',
'GWE_SSI_Adj',
'CAFB_2025Nov_GWE_SS032_lines',
'CAFB_2025Nov_GWE_SS028_lines',
'SS032_GWE_May2022',
'May_2022_Elevation_Scrubbed',
'May_2022_Elevation_SS032',
'Basewide_Contour_Oct2022',
'SS032_Contour_Oct2022',
'SS028_Contour_Oct2022',
'LF009_Contour_Oct2022',
'SS028_Contour_Oct2022_smoothed_half',
'Basewide_Contour_Oct2022_scrubbed',
'Basewide_ShallowUpper_Contour_Oct2022',
'Basewide_DeeperUpper_Contour_Oct2022',
'Basewide_Contour_Oct2022_smoothed',
'LF005_07_12_Contour_Oct2022',
'LF006_Contour_Oct2022',
'LF006_Contour_Oct2022_V2',
'LF009_10_Contour_Oct2022',
'SS032_Contour_Oct2022V1',
'SS032_Contour_Oct2022V2',
'SS032_Contour_Oct2022V4',
'Basewide_Contour_Oct2022_Aquifer1',
'Aquifer_1_Basewide_contours',
'Basewide_Contour_Oct2022_smoothed_1ft',
'CAFB_May2023_GWE',
'SS032_May2023_GWE',
'SS028_May2023_GWE',
'SS028_May2023_GWE_scrubbed',
'CAFB_May2023_Contour_Adj1',
'SS032_May2023_GWE_Adj1',
'SS032_May2023_GWE_Adj2',
'CAFB_May2023_Contour_Adj2',
'CAFB_May2023_Contour_Adj3',
'SS028_May2023_GWE_Adj3_Scrub'
]
    # ---------------------

    add_date_field_to_featureclasses(input_gdb, input_featureclasses)
