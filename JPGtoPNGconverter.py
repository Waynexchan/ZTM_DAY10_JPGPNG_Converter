import sys
import os
from PIL import Image

# grab first and second arguments
OPEN_folder = sys.argv[1]
SAVE_folder = sys.argv[2]
#check if new/ exists, if not create
if not os.path.isdir(SAVE_folder):
    os.mkdir(SAVE_folder)
    print(f'Folder {SAVE_folder} was created')
else:
    print(f'Folder {SAVE_folder} already exist')
#loop through Pokedex
for image in os.listdir(OPEN_folder):
    photo_name = os.path.splitext(image)[0]
    if image.lower().endswith('.jpg'):
        image_path = os.path.join(OPEN_folder,image)
        img = Image.open(image_path)
        save_path = os.path.join(SAVE_folder,photo_name + '.png')
        img.save(save_path)
    else:
        print('Support JPG file only')
#convert images to png
#save to the new folder



