import os
import json

compositional = []
local = []
cancel = []
som = os.listdir("./meta_data")
for file in som:
    if "jsonl" in file:
        with open(f"./meta_data/{file}", "r") as f:
            #
            dicts = list(f)
        dicts = [json.loads(_) for _ in dicts]
        print(dicts[0])
        #dicts[0]['utterance'] = dicts[0]['utterance'].replace("new ", "")
        if 'compos' in dicts[0]['type']:
            compositional.append(file)
        elif 'local' in dicts[0]['type']:
            local.append(file)
        else:
            cancel.append(file)
	
        #if "direct " in dicts[0]['type']:
        #    #
        #    dicts[0]['type'] = dicts[0]['type'].replace("direct ", "")
with open(f"compositional.txt", "w") as f:
    for file in compositional[:200]:
        f.write(file)
        f.write("\n")

with open(f"local.txt", "w") as f:
    for file in local[:200]:
        f.write(file)
        f.write("\n")
            
with open(f"cancel.txt", "w") as f:
    for file in cancel[:200]:
        f.write(file)
        f.write("\n")
