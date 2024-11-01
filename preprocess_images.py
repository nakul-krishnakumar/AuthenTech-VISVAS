import os
from pathlib import Path
import cv2
from preprocessing import preprocess

source_folder = "D:\\AuthenTech Viswas Project\\sign_data"
destination_folder = "D:\\AuthenTech Viswas Project\\sign_data_processed"

Path(destination_folder).mkdir(parents=True, exist_ok=True)

for root, dirs, files in os.walk(source_folder):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = cv2.imread(file_path)
            if image is not None:
                processed_image = preprocess(image)
                
                relative_path = os.path.relpath(file_path, source_folder)
                output_path = os.path.join(destination_folder, relative_path)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                cv2.imwrite(output_path, processed_image)
                print(f"Saved processed image to {output_path}")

print("Preprocessing complete. All preprocessed images are saved in 'sign_data_processed' folder.")
