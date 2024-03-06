import os
import json

som = os.listdir("./meta_data")
for file in som:
    if "jsonl" in file:
        with open(f"./meta_data/{file}", "r") as f:
            #
            dicts = list(f)
        dicts = [json.loads(_) for _ in dicts]
        print(dicts[0])
        dicts[0]['utterance'] = dicts[0]['utterance'].replace("new ", "")
        
        if "direct " in dicts[0]['type']:
            #
            dicts[0]['type'] = dicts[0]['type'].replace("direct ", "")
        with open(f"./meta_data/{file}", "w") as f:
            for dict_ in dicts:
                f.write(json.dumps(dict_))
                f.write("\n")
            

