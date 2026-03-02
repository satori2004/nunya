import os

gdb_path = r"C:\Shared\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\KI_Sawyer\DoD_KISAWYER\BRAC_KISAWYER_3101\BRAC_KISAWYER_3101.gdb"  # <-- change this

for root, dirs, files in os.walk(gdb_path):
    for filename in files:
        #if filename.endswith(".lock") and "JMCA" in filename:
        if filename.endswith(".lock"):
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Could not delete {file_path}: {e}")
