import os, json
import random
import shutil

IMG_PATH = 'archive\\images\\images'
CHOSEN_PATH = "dogs.json"
DOGS_DIR = 'chosen_dogs'

def compile_dogs():
    """
    Compile a JSON file with 3 image paths randomly selected 
    from each breed directory
    """
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

def main():
    with open(CHOSEN_PATH, 'r') as f:
        dogs = json.load(f)
        print(f"Loaded {len(dogs)} breeds from {CHOSEN_PATH}")
        for breed_path, images in dogs.items():
            for image_file in images:
                # copy the file into a new directory
                src = os.path.join(breed_path, image_file)
                # breed path is the last segment of the path
                dest = os.path.join(DOGS_DIR, breed_path.split('\\')[-1], image_file)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(src, dest)
                print(f"Copied {src} to {dest}")
            
if __name__ == "__main__":
    main()