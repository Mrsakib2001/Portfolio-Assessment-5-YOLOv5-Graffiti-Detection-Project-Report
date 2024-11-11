import os

# Path to your directories
train_dir = "C:/Users/61449/PycharmProjects/YOLO_Graffiti_Detection/data/train_yolo_labels"
test_dir = "C:/Users/61449/PycharmProjects/YOLO_Graffiti_Detection/data/test_yolo_labels"

# Function to rename files
def rename_annotation_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # Remove the .txt extension, add .jpg to match the image name
            new_filename = filename.replace('.txt', '.JPG.txt')
            # Create the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed {filename} to {new_filename}")

# Rename files in both train and test directories
rename_annotation_files(train_dir)
rename_annotation_files(test_dir)
