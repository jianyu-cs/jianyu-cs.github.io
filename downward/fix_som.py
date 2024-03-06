import os

som = os.listdir("./SoMs")
for file in som:
    os.rename("./SoMs/"+file, "./SoMs/"+file.replace("SoM_", ""))

