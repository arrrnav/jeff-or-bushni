import os, json
import random

IMG_PATH = 'archive\\images\\images'
CHOSEN_PATH = "dogs.json"

chosen_dogs = {}

for breed_path in os.listdir(IMG_PATH):
    breed_full_path = os.path.join(IMG_PATH, breed_path)
    # if os.path.isdir(breed_full_path):
    print(f"Processing breed: {breed_path}\n\t{len(os.listdir(breed_full_path))} images found.")
    
    # Randomly select 3 images from each breed
    images = os.listdir(breed_full_path)  
    selected_images = random.sample(images, 3)
    chosen_dogs[breed_full_path] = selected_images

json_data = json.dumps(chosen_dogs, indent=4)
with open(CHOSEN_PATH, 'w') as f:
    f.write(json_data)

print(f"{len(os.listdir(IMG_PATH))} breeds processed.")
