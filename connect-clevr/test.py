import os
import json

for k,file_name in enumerate(os.listdir("./")):
    if "test" in file_name:
        continue
    with open("./"+file_name, "rb") as f:
        ans = list(f)
    print(k, file_name)
    ans = [json.loads(_.decode("utf-8", "ignore")) for _ in ans]
    images_dict_list=[]
    image_names = []
    utter_dict = ""
    for _ in ans:
        if "utterance" in _:
            utter_dict = _
        else:
            image_names.append(_["image_filename"])
            images_dict_list.append(_)
    #
    # open jsons
    print(utter_dict)
    open_jsons = []
    for image_name in image_names:
        json_name = "../meta_data_jsons/"+image_name.split(".")[0]+".json"
        f = open(json_name, "r")
        open_jsons.append(json.load(f))
    #

    with open(file_name, "w") as f:
        f.write(json.dumps(utter_dict)+"\n")
        #f.write("\n")
        for open_json in open_jsons:
            f.write(json.dumps(open_json)+"\n")
            



