#copy .gdb file from one location to another


import shutil
from pathlib import Path

src_gdb = Path(r"C:\Shared\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\KI_Sawyer\DoD_KISAWYER\BRAC_KISAWYER_3101\BRAC_KISAWYER_3101.gdb")
dst_gdb = Path(r"C:\Shared\Box\Fed_DOD\AFCEC\Midwest BECOS\2 - Midwest BECOS TO1and2\15.0 GIS\KI_Sawyer\DoD_KISAWYER\BRAC_KISAWYER_3101\BRAC_KISAWYER_3101_new.gdb") #creates new .gdb file (no need to create one prior to running script)

# Copy entire geodatabase
shutil.copytree(src_gdb, dst_gdb)

print("Geodatabase copied successfully.")
