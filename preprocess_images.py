import os
from pathlib import Path
import cv2
from preprocessing import preprocess

source_folder = "sign_data"
destination_folder = "sign_data_processed"

Path(destination_folder).mkdir(parents=True, exist_ok=True)

for root, dirs, files in os.walk(source_folder):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = cv2.imread(file_path)
            if image is not None:
                # Apply preprocess function
                processed_image = preprocess(image, 256, 256)

                # Ensure image data type and range are suitable for saving
                if processed_image.dtype != 'uint8':
                    processed_image = (processed_image * 255).astype('uint8')

                relative_path = Path(os.path.relpath(file_path, source_folder)).as_posix()
                output_path = Path(destination_folder, relative_path).as_posix()
                os.makedirs(Path(output_path).parent, exist_ok=True)

                success = cv2.imwrite(output_path, processed_image)
                if success:
                    print(f"Saved processed image to {output_path}")
                else:
                    print(f"Failed to save image at {output_path}")

print("Preprocessing complete. All preprocessed images are saved in 'sign_data_processed' folder.")
