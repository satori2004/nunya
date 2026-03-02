import arcpy
import os

def gdb_to_shapefiles(gdb_path, output_folder):
    arcpy.env.workspace = gdb_path
    feature_classes = arcpy.ListFeatureClasses()

    if not feature_classes:
        print("No feature classes found in the geodatabase.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for fc in feature_classes:
        output_shp = os.path.join(output_folder, f"{fc}.shp")
        print(f"Converting {fc} -> {output_shp}")
        arcpy.FeatureClassToFeatureClass_conversion(fc, output_folder, f"{fc}.shp")

    print("Conversion complete!")

if __name__ == "__main__":
    # Prompt user for inputs
    # gdb_path = input("Enter the path to the .gdb file: ").strip()
    # output_folder = input("Enter the folder path where shapefiles should be saved: ").strip()
    gdb_path = r"C:\Shared\Box\Commercial\Johnson Controls\JCI Saline, Monroe St\900-CAD-GIS\920-GIS or Graphics\Monroe_GIS\Monroe_GIS.gdb"  # Example path
    output_folder = r"C:\Shared\Box\Commercial\Johnson Controls\JCI Saline, Monroe St\900-CAD-GIS\920-GIS or Graphics\Monroe_GIS\gdb_to_shapefile"  # Example output folder

    gdb_to_shapefiles(gdb_path, output_folder)
