import jacinle
import shutil
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
    implicature_type = "Direct Implicature Contextual Cancellation"
    if not os.path.exists('../updated_coco/'):
        os.mkdir('../updated_coco/')
        
    if not os.path.exists('../updated_coco/images/'):
        os.mkdir('../updated_coco/images/')
    if not os.path.exists('../updated_coco/meta_data/'):
        os.mkdir('../updated_coco/meta_data/')

    temp = os.listdir("../updated_coco/meta_data/")
    len_temp = len(temp)
        
    visualizer = HTMLTableVisualizer('../updated_coco/html_visualizer_cancel', f'Connective Implicature Contextual Cancellation Visualization, Natural Domain, 100')
    with visualizer.html(), visualizer.table('In this reference game, the speaker will generate a statement to describe two images, and both the speaker and you will be rewarded if you can correctly identify both referent images. Please proceed by selecting your answers based on the corresponding numerical image index.',[
            HTMLTableColumnDesc('text', 'Text', 'raw'),
            HTMLTableColumnDesc('idx', 'Idx', 'raw'),
            HTMLTableColumnDesc('image1', 'Image 1', 'image'),
            HTMLTableColumnDesc('image2', 'Image 2', 'image'),
            HTMLTableColumnDesc('image3', 'Image 3', 'image'),
            HTMLTableColumnDesc('image4', 'Image 4', 'image'),
            HTMLTableColumnDesc('image5', 'Image 5', 'image'),
            HTMLTableColumnDesc('answer', 'Answer', 'raw'),
            #HTMLTableColumnDesc('type', 'Implicature Type', 'raw'),
    ]):
        for k, file_name in enumerate(os.listdir("./cancel_meta/")):
            print(k)
            if k>99:
                break
            #image1_filename = f'./images/CLEVR_00000{int(start_idx)}.png'
            #image2_filename = f'./SoMs/CLEVR_00000{int(start_idx)}.png'
            json_filename = f'./cancel_meta/{file_name}'
            new_json_filename = 'MSCOCO_%%0%dd.jsonl' % 6 % (len_temp+k-1)
            print(new_json_filename)
            
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
            game_setup = 'You are in a reference game. The speaker will generate an utterance to refer to two referent images and he/ she will be rewarded if you can successfully pick all two referent images. So now, please select your answers by referencing the corresponding numerical image index.'
            for item in data:
                if "image_filename" in item:
                    image_filename = item['image_filename']

                    images.append(os.path.join("./images", image_filename))
                if "utterance" in item:
                    utterance = item['utterance'].replace("It contains", "The image shows") #" shows ".join(item["utterance"].split("shows"))

            #if not os.path.exists('./updated_images/'):
            #    os.mkdir('./updated_images/')
            #if not os.path.exists('./updated_meta_data/'):
            #    os.mkdir('./updated_meta_data/')
            for image in images:
                shutil.copy(image, os.path.join('../updated_coco/images/', image.split('/')[-1]))
            shutil.copy(json_filename, os.path.join('../updated_coco/meta_data/', new_json_filename))
            #with open(json_filename, 'r') as f:
            #    ans = json.load(f)
            #data = jacinle.load(json_filename)
            #utterance = utterance
            
            text = f'<b>Game:</b> {game_setup}<br><b>Speaker:</b> {utterance}'

            referent1, referent2 = images[0], images[1]
            random.shuffle(images)
            referent1_id = images.index(referent1)
            referent2_id = images.index(referent2)
            if referent1_id > referent2_id:
                referent1_id, referent2_id = referent2_id, referent1_id

            
            answer = f'<b>Referent Image ID:</b> {referent1_id+1}, {referent2_id+1}'
            
            #text = f'<b>Utterance:</b> {text1}'
            answer = f'<b>Referents:</b> Image {referent1_id+1}, {referent2_id+1}<br><b>Type:</b> {implicature_type}'
            #type_ = f'<b>Type:</b> {implicature_type}'

            visualizer.row(idx=k+1, image1=images[0], image2=images[1], image3=images[2], image4=images[3], image5=images[4], text=text, answer=answer)


if __name__ == '__main__':
    main()
