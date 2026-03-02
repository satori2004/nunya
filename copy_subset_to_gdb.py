# import arcpy
# import os

# # ---------- INPUTS ----------
# source_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB_old.gdb"
# target_gdb = r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\ColumbusAFB.gdb"

# arcpy.env.overwriteOutput = False

# objects_to_copy = [
# 'LF006_Kernel_Oct2022',
# 'LF009_010_GWLOct2022RasterV2',
# 'MW06_102023_TCE',
# 'MW06_102023_VC',
# 'Natural_CAFB1',
# 'Natural_Oct2023_V1',
# 'Natural_Oct2023_V2',
# 'Natural_Oct2023_V3',
# 'SS028_A_OCT24',
# 'SS028_AreaA_OCT23_VC',
# 'SS028_AreaC_OCT23_TCE',
# 'SS028_AreaC_OCT23_TCE_V2',
# 'SS028_AreaC_OCT23_VC',
# 'SS028_AreaE_OCT23_TCE',
# 'SS028_AreaE_OCT23_VC',
# 'SS028_GWEOct2022Raster_34points',
# 'SS028_May2023_TCE_Area_B_Raster',
# 'SS028_May2023_TCE_Area_C_Raster',
# 'SS028_May2023_VC_Area_B_Raster',
# 'SS028_May2023_VC_Area_C_Raster',
# 'SS028_OCT2022_TCE_Area_B_Raster',
# 'SS028_OCT2022_TCE_Area_C_Raster',
# 'SS028_OCT2022_TCE_Area_E_Raster',
# 'SS028_OCT2022_VC_Area_B_Raster',
# 'SS028_OCT2022_VC_Area_C_Raster',
# 'SS028_OCT2022_VC_Area_E_Raster',
# 'SS028_OCT2023_TCE_Area_B_Raster',
# 'SS028_OCT2023_VC_Area_B_Raster',
# 'SS028_Oct2022_TCE_Area_A_Raster',
# 'SS028_Oct2022_VC_Area_A_Raster',
# 'SS028_sansW113',
# 'SS032_GWEOct2022Raster_V1',
# 'SS032_GWEOct2022Raster_V2',
# 'SS032_GWEOct2022Raster_V3',
# 'SS032_GWEOct2022Raster_V4',
# 'SS032_GWE_Oct2022Raster_V4',
# 'SS032_May2023_DCE_MW06_Raster',
# 'SS032_May2023_DCE_W128_Raster',
# 'SS032_May2023_TCE_MW06_Raster',
# 'SS032_May2023_TCE_W128_Raster',
# 'SS032_May2023_VC_MW06_Raster',
# 'SS032_May2023_VC_W128_Raster',
# 'SS032_OCT2022_TCE_MW06_Raster',
# 'SS032_OCT2022_TCE_W128_Raster',
# 'SS032_OCT2022_VC_MW06_Raster',
# 'SS032_OCT2022_VC_W128_Raster',
# 'SSI_TCE',
# '_B_TCE_Oct24'
# ]




# # ---------- COPY ----------
# for obj in objects_to_copy:

#     source_path = os.path.join(source_gdb, obj)
#     target_path = os.path.join(target_gdb, obj)

#     if not arcpy.Exists(source_path):
#         print(f"SKIPPED (not in source): {obj}")
#         continue

#     if arcpy.Exists(target_path):
#         print(f"SKIPPED (already in target): {obj}")
#         continue

#     arcpy.Copy_management(source_path, target_path)
#     print(f"Copied: {obj}")

# print("\nList-based copy completed.")







#----------------------
#copy raster from folder to another
#----------------------


import shutil
from pathlib import Path

# Source and destination paths
src = Path(r"C:\Shared\Box\Fed_DOD\USACE-Savannah\2018-2022_REAT ERS W912HN18D1002\TO W912HN-21-F-1030 - MS Group ORC\17.0 GIS\Imagery\CAFB.sid")
dst = Path(r"C:\Users\JoshMcAteer\OneDrive - ctico\Documents\Projects\CLMBS\Imagery\CAFB.sid")

# Copy the file (preserves metadata)
shutil.copy2(src, dst)

print("File copied successfully.")

