import os
import pandas as pd
from PIL import Image

def convert_csv_to_yolo(csv_file, labels_output_folder, images_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(labels_output_folder):
        os.makedirs(labels_output_folder)

    # Read CSV file
    try:
        df = pd.read_csv(csv_file)
        print(f"Successfully read CSV file: {csv_file}")
    except FileNotFoundError:
        print(f"CSV file not found: {csv_file}")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Create a dictionary to collect labels for each image
    image_labels = {}

    # Iterate over each row in the CSV
    for index, row in df.iterrows():
        try:
            # Update these variables to match your actual CSV column names
            image_name = row['filename']
            # Convert the class name to a numeric ID
            class_name = row['class']
            class_id = 0 if class_name == "Graffiti" else -1  # Replace with appropriate ID or handling

            # Skip the row if the class is not valid
            if class_id == -1:
                print(f"Unknown class '{class_name}' in row {index}. Skipping.")
                continue

            x_min = row['xmin']
            y_min = row['ymin']
            x_max = row['xmax']
            y_max = row['ymax']

            # Use the width and height from the CSV if available
            img_width = row['width']
            img_height = row['height']

            # Convert to YOLO format
            x_center = ((x_min + x_max) / 2) / img_width
            y_center = ((y_min + y_max) / 2) / img_height
            width = (x_max - x_min) / img_width
            height = (y_max - y_min) / img_height

            # YOLO label format: class_id x_center y_center width height
            yolo_label = f"{class_id} {x_center} {y_center} {width} {height}"

            # Collect the labels for each image
            if image_name not in image_labels:
                image_labels[image_name] = []
            image_labels[image_name].append(yolo_label)

        except KeyError as ke:
            print(f"Missing key in CSV file: {ke}. Skipping row {index}.")
            continue
        except Exception as e:
            print(f"Error processing row {index}: {e}. Skipping row.")
            continue

    # Save labels to files
    for image_name, labels in image_labels.items():
        label_filename = os.path.splitext(image_name)[0] + '.txt'
        label_filepath = os.path.join(labels_output_folder, label_filename)
        print(f"Saving label to: {label_filepath}")

        # Use write mode ('w') to ensure only correct data is saved
        with open(label_filepath, 'w') as f:
            for label in labels:
                f.write(label + '\n')

# Example usage for training labels
if __name__ == "__main__":
    # Convert training labels
    convert_csv_to_yolo(
        csv_file='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/bounding_boxes/train_labels.csv',
        labels_output_folder='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/data/train/labels',
        images_folder='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/data/train/images'
    )

    # Convert testing labels
    convert_csv_to_yolo(
        csv_file='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/bounding_boxes/test_labels.csv',
        labels_output_folder='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/data/test/labels',
        images_folder='C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/data/test/images'
    )
