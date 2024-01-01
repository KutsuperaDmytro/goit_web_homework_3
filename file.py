import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder):
    extension_dict = defaultdict(list)

    def process_file(file_path):
        file_name, file_extension = os.path.splitext(file_path)
        extension_dict[file_extension].append(file_path)

    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(process_file, file_path)

    for extension, files in extension_dict.items():
        print(f"Extension: {extension}, Files: {files}")

if __name__ == "__main__":
    folder_path = "D:/pycharm/processing_1"
    process_folder(folder_path)