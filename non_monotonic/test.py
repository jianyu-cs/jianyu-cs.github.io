import jacinle
import argparse
from jaclearn.visualize.html_table import HTMLTableVisualizer, HTMLTableColumnDesc
import json
import random
import os

# parser = argparse.ArgumentParser()
# parser.add_argument('--start_idx', default=0)
# parser.add_argument('--type', default="cancel_direct_implicature")
# args = parser.parse_args()

def main():
    meta_list = []
    for item in os.listdir("./meta_data"):
        if "checkpoint" in item:
            continue
        temp_item = item.rstrip(".jsonl").rstrip('.jsonl.swp').split("CLEVR_")[1]
        #if int(temp_item) >= 0 and int(temp_item) <= 100 and "jsonl" in item:
        if "jsonl" in item and int(temp_item) < 200:
            meta_list.append(item)
        #elif int(temp_item) >= 300 and int(temp_item) <= 400 and "jsonl" in item:
        #    meta_list.append(item)
    meta_list = list(set(meta_list))
        
    visualizer = HTMLTableVisualizer('./html_visualizer', f'Non-monotonic Embedded Implicature Visualization, CLEVR Direct, Intrinsic Attributes, 200')
    with visualizer.html(), visualizer.table('In this reference game, the speaker will generate a statement to describe two images, and both the speaker and you will be rewarded if you can correctly identify both referent images. Please proceed by selecting your answers based on the corresponding numerical image index.', [
        HTMLTableColumnDesc('text', 'Text', 'raw'),
        HTMLTableColumnDesc('text1', 'ID', 'raw'),
        HTMLTableColumnDesc('image1', 'Image 1', 'image'),
        HTMLTableColumnDesc('image2', 'Image 2', 'image'),
        HTMLTableColumnDesc('image3', 'Image 3', 'image'),
        HTMLTableColumnDesc('answer', 'Answer', 'raw'),
        #HTMLTableColumnDesc('type', 'Implicature Type', 'raw'),
    ]):
        for k, file_name in enumerate(meta_list): #os.listdir("./meta_data/"):
            #image1_filename = f'./images/CLEVR_00000{int(start_idx)}.png'
            #image2_filename = f'./SoMs/CLEVR_00000{int(start_idx)}.png'
            json_filename = f'./meta_data/{file_name}'
            #if start_idx >= 10:
            #    #image1_filename = f'./images/CLEVR_0000{int(start_idx)}.png'
            #    #image2_filename = f'./SoMs/CLEVR_0000{int(start_idx)}.png'
            #    json_filename = f'./meta_120/{file_name}'
            #if start_idx >= 100:
            #    #image1_filename = f'./images/CLEVR_000{int(start_idx)}.png'
            #    #image2_filename = f'./SoMs/CLEVR_000{int(start_idx)}.png'
            #    json_filename = f'./meta_120/{file_name}'
            #if start_idx >= 1000:
            #    json_filename = f'./meta_120/{file_name}'

            with open(json_filename, "r") as f:
                data = list(f)
            data = [json.loads(_) for _ in data]
            images = []
            utterance = ""
            impli_type = ""
            for item in data:
                if "image_filename" in item:
                    image_filename = item['image_filename']
                    images.append(os.path.join("./SoMs", "SoM_"+image_filename))
                if "utterance" in item:
                    utterance = item["utterance"]
                    impli_type = item["type"]
                    
                
            #with open(json_filename, 'r') as f:
            #    ans = json.load(f)
            #data = jacinle.load(json_filename)
            
            
            text = f'<b>Utterance:</b> {utterance}'

            referent1 = images[0]
            random.shuffle(images)
            referent1_id = images.index(referent1)
            #referent2_id = images.index(referent2)
            #if referent1_id > referent2_id:
            #    referent1_id, referent2_id = referent2_id, referent1_id
            
            answer = f'<b>Referent Image ID:</b> {referent1_id+1}, {impli_type}'
            
            #text = f'<b>Utterance:</b> {text1}'
            #answer = f'<b>Referents:</b> Image {ans_ids[0]+1}, {ans_ids[1]+1}<br><b>Type:</b> {implicature_type}'
            #type_ = f'<b>Type:</b> {implicature_type}'
            print(images, json_filename)

            visualizer.row(text1=str(k), image1=images[0], image2=images[1], image3=images[2], text=text, answer=answer)


if __name__ == '__main__':
    main()
