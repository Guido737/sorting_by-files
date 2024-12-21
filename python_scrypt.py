
import os
import shutil
import argparse
FILE_CATEGORIES = {
    'docs': ['.doc', '.docx', '.txt', '.rtf'],
    'pdf': ['.pdf'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'audio': ['.mp3', '.wav', '.aac', '.flac'],
    'spreadsheets': ['.xls', '.xlsx', '.csv'],
    'presentations': ['.ppt', '.pptx'],
    'archives': ['.zip', '.tar', '.tar.gz', '.rar', '.7z'],
}

def create_category_directory(source_dir,category):
    category_dir = os.path.join(source_dir, category)
    if not os.path.exists(category_dir):
        try:
            os.makedirs(category_dir)
            print(f'Created directory {category_dir}')
        except OSError as e:
            print(f'Error creating directory "{category_dir}": {e}')
            return None
    return category_dir
    
def move_file(file, category_dir):
    try:
        destination = os.path.join(category_dir, os.path.basename(file))
        shutil.move(file, destination)
        print(f"Moved: {file} -> {destination}")
    except Exception as e:
        print(f'Error moving file "{file}": {e}')
        
def sort_files(source_dir):
    if not os.listdir(source_dir):
        print("The source directory is empty.")
        return
    others_dir = create_category_directory(source_dir,"others")
    if not others_dir:
        return
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if not os.path.isfile(file_path) or filename.startswith("."):
            continue
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_dir = create_category_directory(source_dir,category)
                if category_dir:
                    move_file(file_path, category_dir)
                    moved = True
                    break
        if not moved:
            move_file(file_path, others_dir)

def get_arguments():
    parser = argparse.ArgumentParser(description = "Sort files by type,like a Developer.")
    parser.add_argument("source_dir",help = "Path to the source directory containing files to be sorted.")
    args = parser.parse_args()
    return args.source_dir
    
def main():
    source_dir = get_arguments()
    if not os.path.isdir(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return
    sort_files(source_dir)
    print("Files have been sorted.")

if __name__ == '__main__':
    main()
