# import arcpy
# arcpy.env.workspace = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"
# datasets = arcpy.ListDatasets(feature_type='feature')
# datasets = [''] + datasets if datasets is not None else []

# for ds in datasets:
#     for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
#         print(fc)



#------------------#
# prints names of featuredatasets and feature classes in a geodatabase
#------------------#


import arcpy

arcpy.env.workspace = r"C:\Users\JoshMcAteer\OneDrive - ctico\GIS - GIS Files\CAFB_SDSFIE_ETL\ColumbusAFB_copy.gdb"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else ['']

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        if ds:  # Feature class is inside a feature dataset
            print(f"{ds}\\{fc}")
        else:   # Feature class is in the root of the geodatabase
            print(fc)


