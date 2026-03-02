import arcpy
import os
import sys


def rename_file_gdb(old_gdb_path, new_gdb_path):
    if not old_gdb_path.lower().endswith(".gdb"):
        raise ValueError("Old path is not a .gdb")

    if not new_gdb_path.lower().endswith(".gdb"):
        raise ValueError("New path must end with .gdb")

    if not arcpy.Exists(old_gdb_path):
        raise FileNotFoundError(f"GDB not found: {old_gdb_path}")

    if arcpy.Exists(new_gdb_path):
        raise FileExistsError(f"Target GDB already exists: {new_gdb_path}")

    # Release ArcGIS locks
    arcpy.ClearWorkspaceCache_management()

    # Rename geodatabase
    arcpy.Rename_management(old_gdb_path, new_gdb_path)


if __name__ == "__main__":
    # Example usage (replace with sys.argv or script tool parameters)
    old_gdb = r"C:\Shared\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\KI_Sawyer\KISAWYER_new.gdb"
    new_gdb = r"C:\Shared\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\KI_Sawyer\KISAWYER.gdb"

    try:
        rename_file_gdb(old_gdb, new_gdb)
        print(f"Successfully renamed:\n{old_gdb}\n→ {new_gdb}")
    except Exception as e:
        print(f"Failed to rename geodatabase:\n{e}")
        sys.exit(1)
