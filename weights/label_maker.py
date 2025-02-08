import json
import os

with open("../TACO/data/annotations.json", "r") as f:
    data = json.load(f)

os.makedirs("labels", exist_ok=True)

for img in data["images"]:
    img_id = img["id"]
    img_path = img["file_name"]
    img_name = os.path.splitext(img_path)[0]
    
    subdir = os.path.dirname(img_path)
    label_dir = os.path.join("labels", subdir)
    os.makedirs(label_dir, exist_ok=True)
    
    label_path = os.path.join(label_dir, f"{os.path.basename(img_name)}.txt")
    
    with open(label_path, "w") as label_file:
        for ann in data["annotations"]:
            if ann["image_id"] == img_id:
                category_id = ann["category_id"]
                x, y, w, h = ann["bbox"]
                width = img["width"]
                height = img["height"]
                
                x_center = (x + w/2) / width
                y_center = (y + h/2) / height
                norm_w = w / width
                norm_h = h / height
                
                label_file.write(f"{category_id} {x_center} {y_center} {norm_w} {norm_h}\n")