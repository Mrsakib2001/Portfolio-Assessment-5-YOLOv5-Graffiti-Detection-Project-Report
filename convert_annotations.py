import os


def convert_annotations(input_folder, output_folder):
    """
    Converts given annotations to YOLO format.
    :param input_folder: Directory containing original annotation files.
    :param output_folder: Directory to save YOLO formatted annotation files.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Track if annotations are converted successfully
    converted_count = 0

    # Iterate over each annotation file in the input folder
    for annotation_file in os.listdir(input_folder):
        if annotation_file.endswith('.txt'):
            input_path = os.path.join(input_folder, annotation_file)
            output_path = os.path.join(output_folder, annotation_file)

            try:
                with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
                    for line in infile:
                        data = line.strip().split()
                        if len(data) < 5:
                            print(f"Warning: Skipping line in {annotation_file} due to incorrect format: {line}")
                            continue

                        class_id = int(data[0])
                        x_center = float(data[1])
                        y_center = float(data[2])
                        width = float(data[3])
                        height = float(data[4])

                        # Format in YOLO style
                        yolo_annotation = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
                        outfile.write(yolo_annotation)

                    print(f"Converted {annotation_file} successfully.")
                    converted_count += 1

            except Exception as e:
                print(f"Error processing {annotation_file}: {e}")

    if converted_count == 0:
        print("No files were converted. Please check the input folder and format.")
    else:
        print(f"Successfully converted {converted_count} annotation files.")


if __name__ == "__main__":
    # Use absolute paths to avoid path issues
    input_folder = 'C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/data/annotations/'
    output_folder = 'C:/Users/61449/PycharmProjects/YOLOv5_Graffiti_Detection/yolo_annotations/'

    # Convert annotations to YOLO format
    convert_annotations(input_folder, output_folder)
