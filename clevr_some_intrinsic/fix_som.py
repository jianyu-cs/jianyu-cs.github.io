import os

som = os.listdir("./SoMs")
for file in som:
    os.rename(file, "./SoMs/"+file.replace("SoM_", ""))

